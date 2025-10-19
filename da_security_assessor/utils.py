import yaml
import sys
from pathlib import Path

def load_config(config_path: str):
    """Load YAML configuration file."""
    path = Path(config_path)
    if not path.exists():
        print(f"[ERROR] Config file not found: {config_path}", file=sys.stderr)
        sys.exit(1)
    try:
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
            return data
    except yaml.YAMLError as e:
        print(f"[ERROR] Failed to parse YAML: {e}", file=sys.stderr)
        sys.exit(1)
