# debug_import.py
import sys
from pathlib import Path

def debug_imports():
    # Print Python path
    print("\nPYTHON PATH:")
    for p in sys.path:
        print(f" - {p}")
    
    # Verify file existence
    project_root = Path(__file__).parent
    print("\nFILE VERIFICATION:")
    print(f"data/__init__.py exists: {(project_root/'data'/'__init__.py').exists()}")
    print(f"data/database/__init__.py exists: {(project_root/'data'/'database'/'__init__.py').exists()}")
    print(f"data/database/connectors.py exists: {(project_root/'data'/'database'/'connectors.py').exists()}")
    
    # Test absolute import
    sys.path.insert(0, str(project_root))
    try:
        from ecommerce_oltp.data.database.connectors import get_engine
        print("\nâœ… ABSOLUTE IMPORT SUCCESS!")
        return True
    except ImportError as e:
        print(f"\nâŒ ABSOLUTE IMPORT FAILED: {e}")
        return False

if __name__ == "__main__":
    debug_imports()
