import re

format = re.compile('^\d+\s+\w+\s*$')

print format.match('13 a qwe')

