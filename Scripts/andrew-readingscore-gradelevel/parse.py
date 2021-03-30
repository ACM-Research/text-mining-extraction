from function import analyze
import glob

for filepath in glob.iglob(r'F:\Documents\code\ACM Research\flesch-scores\texts\*.txt'):
	analyze(filepath)

