#!/usr/bin/env python3
"""
Update the artifacts.md page with the latest versioned artifacts.
This script is run during the release workflow to automatically add new versions.
"""

import sys
import re
from pathlib import Path


def update_artifacts_page(version: str, repo: str = "osc-em/oscem-schemas"):
    """Update perm_docs/artifacts.md with a new version entry."""

    artifacts_file = Path(__file__).parent.parent / "perm_docs" / "artifacts.md"

    if not artifacts_file.exists():
        print(f"Error: {artifacts_file} not found", file=sys.stderr)
        sys.exit(1)

    content = artifacts_file.read_text()

    # Check if this version already exists
    if f"[{version}]" in content:
        print(f"{version} already exists in artifacts.md, skipping update")
        return
    # Create the new version section
    version_section = f"""- [{version}](https://osc-em.github.io/oscem-schemas/artifacts/{version}/)"""
    # Find the "## Available Versions" section and insert after it, at the top of the list
    pattern = r"(## Available Versions\n\n)"

    if not re.search(pattern, content):
        print("Error: Could not find '## Available Versions' section", file=sys.stderr)
        sys.exit(1)

    updated_content = re.sub(
        pattern,
        f"\\1{version_section}",
        content
    )

    artifacts_file.write_text(updated_content)
    print(f"Added version {version} to artifacts.md")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    version = sys.argv[1]
    update_artifacts_page(version)
