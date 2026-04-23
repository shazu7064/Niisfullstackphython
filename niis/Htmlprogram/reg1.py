import re
#re.match()- Checks for a match only at the beginning of the string
result= re.match(r'\d+','123ab56c')
print(result.group()) # output:123


import re
result=re.match(r'\d+','123ab56c')
print(result.group())

import re
result=re.search(r'\d+','123ab56c')
print(result.group())
