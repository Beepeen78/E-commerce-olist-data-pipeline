import os
from pathlib import Path

def print_tree(start_path, max_level=3, indent="    "):
    for root, dirs, files in os.walk(start_path):
        level = root.replace(start_path, "").count(os.sep)
        if level > max_level:
            continue
        print(f"{indent * level}{os.path.basename(root)}/")
        sub_indent = indent * (level + 1)
        for file in files:
            print(f"{sub_indent}{file}")

print("Current directory structure:")
print_tree(".", max_level=4)  # Adjust max_level as needed