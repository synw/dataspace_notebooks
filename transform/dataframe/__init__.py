import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[2]
sys.path.append(str(root))
