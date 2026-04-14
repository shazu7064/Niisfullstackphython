import re
result=re.split(r'\d+','abc123def456')
print(result)


import re
result=re.split(r'\D+','abc123def456')
print(result)