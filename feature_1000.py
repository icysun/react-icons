import os
import sys
from typing import List

def list_icon_files(directory: str) -> List[str]:
    """List all icon files in a given directory."""
    icon_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.svg') or file.endswith('.png'):
                icon_files.append(os.path.join(root, file))
    return icon_files

def check_icon_names(directory: str, old_icon_names: List[str]) -> bool:
    """Check if all old icon names are present in the directory."""
    icon_files = list_icon_files(directory)
    missing_icons = [name for name in old_icon_names if not any(name in file for file in icon_files)]
    return not missing_icons

def main():
    # Define the directory where the icons are stored
    icon_directory = 'path/to/icon/directory'
    # Define the old icon names that should be present
    old_icon_names = ['LuXCircle', 'LuXAnotherIcon']

    try:
        # Check if old icon names are present
        if check_icon_names(icon_directory, old_icon_names):
            print("All old icon names are present.")
        else:
            print("Missing icons:", old_icon_names)
            sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

# Test cases
if __name__ == "__main__":
    main()