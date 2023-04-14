import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
#print("P", file.parents[2])
#_dsl = file.parents[2] / "dataspace"
#print("DSL", _dsl)
sys.path.append(str(root))
#sys.path.append(str(_dsl))
#sys.path.append(str(_dsl / "dataspace"))
