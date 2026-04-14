import re
txt="The rain in spain"
x=re.findall("[a-d]",txt)
print(x)



import re
txt="The rain in spain"
x=re.findall("[^a-z]",txt)
print(x)


import re
txt="The ra16283in in sp4a916n"
x=re.findall("[0-7]",txt)
print(x)

import re
txt="The ra16283in in sp4a9i6n"
x=re.findall("[0-9][a-z]",txt)
print(x)


import re
txt="The ra169in in sp4a95872i6n"
x=re.findall("[0-9][0-9]",txt)
print(x)

import re
txt="The ra16283in in sp4a9i6n"
x=re.findall("[0-7]",txt)
print(x)

import re
txt="The ra169in in sp4a95872i6n"
x=re.findall("[0-9]{3}",txt)
print(x)

import re
txt="The ra169in in sp4a95872i6n"
x=re.findall("[0-9]+",txt)
print(x)