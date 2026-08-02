#!/usr/bin/env python3
"""
add_project.py
--------------
Interactive helper for Ryan's portfolio site.

It does two things in one pass:
  1. Builds a new project detail page (Projects/<filename>.html) using the
     same structure as matlab_app.html / Pendulum.html.
  2. Inserts a matching tile into Portfolio.html so the project shows up
     on the main "Featured Projects" grid, linking to the new page.

Usage:
    Run this from the root of your portfolio repo (the folder that
    contains Portfolio.html and the Projects/ folder):

        python3 add_project.py

    Answer the prompts. You can add as many content blocks (paragraphs
    and images) as you like, in whatever order you want them to appear.

Notes:
    - Image paths you enter should be relative to the Projects/ folder,
      the same way the existing pages do it, e.g.:
          ../assets/img/my_photo.jpg
    - Nothing is overwritten without confirmation.
"""

import os
import sys

PORTFOLIO_FILE = "Portfolio.html"
PROJECTS_DIR = "Projects"
INSERT_MARKER = "<!-- Add more project sections as needed -->"

DETAIL_PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" type="text/css" href="../css/project_style.css">
</head>{collapsible_style}
<body>
    <section class="project-details">
        <h2>{title}</h2>
        <div class="container">
{content}
{dropdowns}
            <br>
            <br>

            <a href="../Portfolio.html" class="button">Back to Projects</a>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2024 Ryan Lemker. All rights reserved.</p>
        </div>
    </footer>
{collapsible_script}
</body>
</html>
"""

# Matches the inline <style> block used in Pendulum.html for the
# collapsible "dropdown" sections.
COLLAPSIBLE_STYLE = """
<style type="text/css">

/* Reset body and html margins */
body, html {
    margin: 0;
    padding: 0;
    width: 100%;
}

/* Full-width container for the collapsible section */
.collapsible-container {
    width: 100%;
    margin: 0;
    padding: 0;
    background-color: #f5f5f5;
}

/* Style for the collapsible header */
.collapsible {
    color: black;
    cursor: pointer;
    padding: 18px;
    width: 100%;
    text-align: left;
    font-size: 18px;
    font-weight: bold;
    border: none;
    box-sizing: border-box;
    margin: 0;
}

/* Active state and hover effect */
.active, .collapsible:hover {
    background-color: #e0e0e0;
}

/* Style for the collapsible content */
.content {
    padding: 18px;
    display: none;
    overflow: hidden;
    background-color: #f1f1f1;
    width: 100%;
    box-sizing: border-box;
    font-size: 16px;
    margin: 0;
}
</style>"""

COLLAPSIBLE_SCRIPT = '    <script src="../js/scripts.js"></script>'

TILE_TEMPLATE = """            <div class="project">
                <h3>{title}</h3>
                <p>{description}</p>
                <a href="Projects/{filename}">View Project</a>
            </div>
"""


def prompt(text, default=None):
    suffix = f" [{default}]" if default is not None else ""
    val = input(f"{text}{suffix}: ").strip()
    if not val and default is not None:
        return default
    return val


def yes(text, default="n"):
    return prompt(text, default).lower().startswith("y")


def collect_content_blocks(indent="            ", heading="Now build the page content."):
    """Interactively build the ordered list of paragraphs / images for a
    block of the page. Reused both for the main body and for the inside
    of each dropdown section (with deeper indent)."""
    blocks = []
    print(f"\n{heading} Add blocks one at a time.")
    while True:
        print("\nAdd a block:")
        print("  1) Paragraph")
        print("  2) Image (with optional caption)")
        print("  3) Done")
        choice = prompt("Choice", "3")

        if choice == "1":
            text = prompt("Paragraph text")
            blocks.append(f"{indent}<p>{text}</p>")

        elif choice == "2":
            img_path = prompt("Image path (relative to Projects/, e.g. ../assets/img/foo.jpg)")
            alt = prompt("Alt text", "Project image")
            width = prompt("Image width (%)", "50")
            caption = prompt("Caption (leave blank for none)", "")
            blocks.append(
                f'{indent}<img src="{img_path}" alt="{alt}" style="width: {width}%;">'
            )
            if caption:
                blocks.append(
                    f'{indent}<h3 style="text-align: center;">{caption}</h3>'
                )
        else:
            break

    return "\n".join(blocks)


def collect_dropdown_sections():
    """Interactively build a set of collapsible/dropdown sections, matching
    the "Process" section style used in Pendulum.html (numbered headers
    like '1. Mechanical Design' that expand to show details)."""
    if not yes("\nAdd a collapsible 'Process' section (dropdowns like on the Pendulum page)?"):
        return None

    section_heading = prompt("Heading above the dropdowns", "Process")

    dropdowns = []
    count = 1
    while True:
        default_title = f"{count}. Step"
        dropdown_title = prompt(f"Dropdown #{count} title", default_title)
        body = collect_content_blocks(
            indent="      ",
            heading=f"Content inside '{dropdown_title}'.",
        )
        dropdowns.append((dropdown_title, body))
        count += 1
        if not yes("Add another dropdown?"):
            break

    items_html = []
    for dropdown_title, body in dropdowns:
        items_html.append(
            f'  <div class="collapsible">{dropdown_title}</div>\n'
            f'  <div class="content">\n{body}\n  </div>'
        )

    dropdown_block = (
        "<hr>\n"
        f"<h2>{section_heading}</h2>\n"
        '<div class="collapsible-container">\n'
        + "\n\n\n\n".join(items_html)
        + "\n</div>\n"
        "<hr>"
    )
    return dropdown_block


def build_detail_page(title, content, dropdown_block=None):
    has_dropdowns = dropdown_block is not None
    return DETAIL_PAGE_TEMPLATE.format(
        title=title,
        content=content,
        dropdowns=dropdown_block if has_dropdowns else "",
        collapsible_style=COLLAPSIBLE_STYLE if has_dropdowns else "",
        collapsible_script=COLLAPSIBLE_SCRIPT if has_dropdowns else "",
    )


def write_detail_page(filename, html):
    os.makedirs(PROJECTS_DIR, exist_ok=True)
    path = os.path.join(PROJECTS_DIR, filename)

    if os.path.exists(path):
        if not yes(f"{path} already exists. Overwrite?"):
            print("Aborted — no files were changed.")
            sys.exit(1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

    return path


def insert_tile_into_portfolio(title, description, filename):
    if not os.path.exists(PORTFOLIO_FILE):
        print(f"Could not find {PORTFOLIO_FILE} in the current directory.")
        sys.exit(1)

    with open(PORTFOLIO_FILE, "r", encoding="utf-8") as f:
        portfolio_html = f.read()

    tile_html = TILE_TEMPLATE.format(
        title=title, description=description, filename=filename
    )

    if INSERT_MARKER in portfolio_html:
        portfolio_html = portfolio_html.replace(
            INSERT_MARKER, tile_html + "            " + INSERT_MARKER
        )
    else:
        # Fallback: insert right before the closing </div> of the last
        # </section> if the marker comment has been removed/edited.
        idx = portfolio_html.rfind("</section>")
        if idx == -1:
            print("Could not find a safe place to insert the new tile.")
            print("Add it manually using this snippet:\n")
            print(tile_html)
            sys.exit(1)
        portfolio_html = portfolio_html[:idx] + tile_html + portfolio_html[idx:]

    with open(PORTFOLIO_FILE, "w", encoding="utf-8") as f:
        f.write(portfolio_html)


def main():
    print("=== Add New Portfolio Project ===\n")

    title = prompt("Project title (e.g. 'Launch Controller System')")
    tile_description = prompt("Short description for the portfolio tile")
    default_filename = title.lower().replace(" ", "_").replace("/", "-") + ".html"
    filename = prompt("Detail page filename", default_filename)

    content = collect_content_blocks()
    dropdown_block = collect_dropdown_sections()
    detail_html = build_detail_page(title, content, dropdown_block)

    detail_path = write_detail_page(filename, detail_html)
    insert_tile_into_portfolio(title, tile_description, filename)

    print("\nDone!")
    print(f"  - New detail page: {detail_path}")
    print(f"  - Tile added to:   {PORTFOLIO_FILE}")
    print("\nDon't forget to git add / commit / push on your feature branch.")


if __name__ == "__main__":
    main()
