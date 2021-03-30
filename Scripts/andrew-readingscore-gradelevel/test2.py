import re

text = 'This is a test string with in it. This has some * * * in i*t. This has some [asdfsef] in it.'

try:
    found = re.search(r'\[([*]+)\]', text).group(1)
except AttributeError:
    # AAA, ZZZ not found in the original string
    found = '' # apply your error handling

text = text.replace('[', ' ')
text = text.replace(']', ' ')
text = text.replace(found, ' ')
print(text)