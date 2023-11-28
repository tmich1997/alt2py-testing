print("SUCCESSFULLY IMPORTED ALT2PY")
import sys
for i in sys.path:
    print(i)

import _utils.Aggregators as Aggs
from tools import GenerateRows
print(GenerateRows)
