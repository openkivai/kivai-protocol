import sys
import os

# Dynamically add the kivai-protocol root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

try:
    from kivai_sdk.kivai_validator import validate_command
    print("Import successful!")
except ImportError as e:
    print(f"Import failed: {e}")
