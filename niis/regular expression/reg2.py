import re
result=re.findall(r'\d','123ab56c')
print(result)

import re
result=re.findall(r'\d+','123ab56c')
print(result)

import re
result=re.findall(r'\d+','abc12356')
print(result)