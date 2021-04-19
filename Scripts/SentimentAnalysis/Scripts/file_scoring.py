import math
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
sia = SentimentIntensityAnalyzer()

def run_scoring(file_data):
    filename = file_data[0]
    print("Running: " + filename)
    lines = score_prep(filename)
    pol_data = polarity_data(lines)
    subj_data = subjectivity_data(lines)
    file_data[6] = pol_data
    file_data[7] = subj_data
    file_data[8] = pol_data[1]
    return file_data


def score_prep(filename):
    filename = filename[:-4]
    path = "TXTs/FPNarratives/"
    filename = path + filename + '.txt'
    with open(filename,'r') as f:
        lines= f.readlines()
    new_lines = []
    for line in lines:
        new_lines.append(TextBlob(line))
    return new_lines

def polarity_data(lines):
    pol_data = []
    pol_avg = pos_lines = neg_lines = neu_lines = pos_avg = neg_avg = neu_avg = all_lines = 0
    fin_desig = ''
    for line in lines:
        all_lines += 1
        vader_result = sia.polarity_scores(line)
        vader_comp = vader_result['compound']        # {'pos': 0, 'compound': 0, 'neu': 0, 'neg': 0} - vader format
        pol_avg += vader_comp
        if vader_comp > 0.05:
            pos_lines += 1
            pos_avg += vader_result['pos']
        elif vader_comp < -0.05:
            neg_lines += 1
            neg_avg += vader_result['neg']
        else:
            neu_lines += 1
            neu_avg += vader_result['neu']
    pos_avg = pos_avg / pos_lines
    neg_avg = neg_avg / neg_lines
    if neu_lines != 0:
        neu_avg = neu_avg / neu_lines
    pol_avg = pol_avg / all_lines
    if pol_avg > 0.05:
        fin_desig = 'pos'
    elif pol_avg < 0.05:
        fin_desig = 'neg'
    else:
        fin_desig = 'neu'
    pol_data.extend([pol_avg,all_lines,fin_desig,pos_avg,pos_lines,neg_avg,neg_lines,neu_avg,neu_lines])
    return pol_data

def subjectivity_data(lines):
    subj_data = []
    subj_avg = all_lines = sub_avg = sub_lines = obj_avg = obj_lines = 0
    dec_list = [0,0,0,0,0,0,0,0,0,0,0]
    fin_desig = ''
    for line in lines:
        all_lines += 1
        desig = line.sentiment.subjectivity
        subj_avg += desig
        if desig > .5:
            sub_avg += desig
            sub_lines += 1
        else:
            obj_avg += desig
            obj_lines += 1

        desig = math.floor(desig * 10)
        dec_list[desig] += 1
    sub_avg = sub_avg / sub_lines
    obj_avg = obj_avg / obj_lines
    subj_avg = subj_avg / all_lines
    if subj_avg > .5:
        fin_desig = 'sub'
    else:
        fin_desig = 'obj'
    subj_data.extend([subj_avg,all_lines,fin_desig,sub_avg,sub_lines,obj_avg,obj_lines,dec_list])
    return subj_data