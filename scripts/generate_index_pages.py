#!/usr/bin/env python3
"""
Generate index.html pages for artifact directories dynamically.
This script discovers available schema types from the project directory and creates appropriate index pages.
"""

import sys
from pathlib import Path
from typing import List, Dict

from schema_utils import format_schema_name, get_schema_description, get_schema_sort_key, is_main_schema


def discover_schemas(project_dir: Path) -> List[Dict[str, str]]:
    """Discover available schema types from the project directory."""
    schemas = []

    if not project_dir.exists():
        print(f"Warning: {project_dir} does not exist", file=sys.stderr)
        return schemas

    for subdir in sorted(project_dir.iterdir(), key=lambda p: get_schema_sort_key(p.name)):
        if subdir.is_dir():
            schema_id = subdir.name
            schemas.append({
                "id": schema_id,
                "name": format_schema_name(schema_id),
                "description": get_schema_description(schema_id)
            })

    return schemas


def generate_root_index() -> str:
    """Generate root index.html that redirects to docs."""
    return """<!DOCTYPE html>
<html>
<head>
  <title>OSC-EM Schema Artifacts</title>
  <meta http-equiv="refresh" content="0; url=https://osc-em.github.io/oscem-schemas/artifacts.html">
</head>
<body>
  <p>Redirecting to <a href="https://osc-em.github.io/oscem-schemas/artifacts.html">artifacts documentation</a>...</p>
</body>
</html>"""


def generate_version_index(version: str, schemas: List[Dict[str, str]]) -> str:
    """Generate index.html for a specific version."""
    # Separate main and supporting schemas
    main_schemas = [s for s in schemas if is_main_schema(s['id'])]
    supporting_schemas = [s for s in schemas if not is_main_schema(s['id'])]
    
    # Build HTML for main schemas
    main_html_items = []
    for schema in main_schemas:
        main_html_items.append(
            f'      <li><a href="{schema["id"]}/">{schema["name"]}</a> '
            f'<span class="description">- {schema["description"]}</span></li>'
        )
    
    # Build HTML for supporting schemas  
    supporting_html_items = []
    for schema in supporting_schemas:
        supporting_html_items.append(
            f'      <li><a href="{schema["id"]}/">{schema["name"]}</a> '
            f'<span class="description">{schema["description"]}</span></li>'
        )

    main_html = '\n'.join(main_html_items)
    supporting_html = '\n'.join(supporting_html_items)
    version_title = "Latest Version" if version == "latest" else f"Version {version}"
    
    return f"""<!DOCTYPE html>
<html>
<head>
  <title>OSC-EM Schema Artifacts - {version_title}</title>
  <style>
    body {{ font-family: Arial, sans-serif; max-width: 900px; margin: 50px auto; padding: 20px; }}
    h1 {{ color: #333; }}
    h2 {{ color: #555; margin-top: 30px; margin-bottom: 10px; font-size: 1.3em; }}
    .intro {{ color: #666; margin: 20px 0; }}
    ul {{ list-style: none; padding: 0; }}
    li {{ margin: 10px 0; }}
    a {{ color: #0094ab; text-decoration: none; font-size: 18px; }}
    a:hover {{ text-decoration: underline; }}
    .description {{ color: #666; font-size: 14px; margin-left: 10px; }}
    .back-link {{ margin-top: 30px; }}
    .separator {{ border-top: 1px solid #ddd; margin: 25px 0; }}
  </style>
</head>
<body>
  <h1>OSC-EM Schema Artifacts - {version_title}</h1>
  <p class="intro">Select a schema type to browse the generated artifacts:</p>
  <h2>Main Technique Schemas</h2>
  <ul>
    {main_html}
  </ul>
  <div class="separator"></div>
  <h2>Supporting Schemas</h2>
  <ul>
    {supporting_html}
  </ul>
  <div class="separator"></div>
  <p class="back-link"><a href="https://osc-em.github.io/oscem-schemas/artifacts/">Back to all versions</a></p>
</body>
</html>"""


def main():
    if len(sys.argv) < 3:
        print("Usage: generate_index_pages.py <project_dir> <output_dir> [version]", file=sys.stderr)
        return 1

    project_dir = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])
    version = sys.argv[3] if len(sys.argv) > 3 else "latest"

    print(f"Generating index pages for version: {version}")
    print(f"Project directory: {project_dir}")
    print(f"Output directory: {output_dir}")

    schemas = discover_schemas(project_dir)
    print(f"Found {len(schemas)} schema type(s): {', '.join(s['id'] for s in schemas)}")

    # Create output directory if needed
    output_dir.mkdir(parents=True, exist_ok=True)

    # Generate index page
    index_html = generate_version_index(version, schemas)
    index_file = output_dir / "index.html"
    index_file.write_text(index_html)
    print(f"Generated {index_file}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
