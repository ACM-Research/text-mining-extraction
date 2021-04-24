from function import analyze
import config as cfg
import glob

for filepath in glob.iglob(cfg.data["directory"]):
	analyze(filepath)
