import textstat
import re
from pathlib import Path

input_file = Path(r'F:\Documents\code\ACM Research\flesch-scores\texts\fpn-blackford-blackford.txt').read_text(encoding='utf8')
input_file = input_file.replace('\n', ' ')
input_file = input_file.replace('*', '')
found = re.findall(r'\[(.*?)\]', input_file)

input_file = input_file.replace('[', '')
input_file = input_file.replace(']', '')
i = 0
while i < len(found):
	input_file = input_file.replace(found[i], '')
	i += 1


print('Reading ease is ' + str(textstat.flesch_reading_ease(input_file)))
print('Score is ' + str(textstat.flesch_kincaid_grade(input_file)))
print(input_file)
print(found)