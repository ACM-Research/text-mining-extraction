import textstat
import re
from pathlib import Path

outF = open('output.txt', 'w')
def analyze(fileName):
	# convert to one long, massive string with spaces so algo can find words
	input_file = Path(fileName).read_text(encoding='utf8')
	input_file = input_file.replace('\n', '')
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

	#outF.write(fileName[51:] + ': ' + str(textstat.flesch_reading_ease(input_file)) + ' ' + str(textstat.flesch_kincaid_grade(input_file)) + '\n')
	outF.write(fileName[105:] + ' ' + str(textstat.flesch_reading_ease(input_file)) + ' ' + str(textstat.flesch_kincaid_grade(input_file)) + '\n')

	# 417 political news articles from BBC
	# 386 entertainment news articles from BBC