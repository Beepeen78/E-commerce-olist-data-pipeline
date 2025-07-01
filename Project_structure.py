import os
from pathlib import Path

def generate_tree(start_path, max_level=5, indent='    '):
    """Generate a visual tree of the project structure"""
    tree = []
    for root, dirs, files in os.walk(start_path):
        level = root.replace(str(start_path), '').count(os.sep)
        if level > max_level:
            continue
            
        # Add directory
        indent_str = indent * level
        tree.append(f"{indent_str}{os.path.basename(root)}/")
        
        # Add files
        sub_indent = indent * (level + 1)
        for f in files:
            tree.append(f"{sub_indent}{f}")
    return '\n'.join(tree)

def verify_critical_files(start_path):
    """Check for essential project files"""
    required = [
        'data/__init__.py',
        'data/database/__init__.py',
        'data/database/connectors.py',
        'dashboards/__init__.py',
        'setup.py'
    ]
    
    missing = []
    for file in required:
        if not (start_path / file).exists():
            missing.append(file)
    
    return missing

if __name__ == "__main__":
    project_root = Path(__file__).parent
    
    print("\nPROJECT STRUCTURE:")
    print(generate_tree(project_root))
    
    print("\nCRITICAL FILE CHECK:")
    missing_files = verify_critical_files(project_root)
    if missing_files:
        print("❌ Missing files:")
        for f in missing_files:
            print(f"- {f}")
    else:
        print("✅ All critical files present")
    
    print("\nPYTHON PATH:")
    import sys
    for path in sys.path:
        if str(project_root) in path:
            print(f"✔ {path}")
            break
    else:
        print("❌ Project root not in Python path")