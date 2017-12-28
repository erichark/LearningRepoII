'''
Created on Dec 23, 2017

@author: Eric
'''

import re
from _hashlib import new

string = "'I AM NOT YELLING', she said. Though we knew it not to be true."
print(string)
new = re.sub('[^A-Z]', '', string)
print(new)