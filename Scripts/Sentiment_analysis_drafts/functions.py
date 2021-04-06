from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import requests
import csv, urllib.request

topic_list =  ['preacher', 'brother', 'soldier', 'independence', 'boston', 'peace', 'responsibility', 'guilty', 'preach', 'regard', 'law', 'faith', 'nation', 'sentiment', 'war', 'attended', 'marched', 'negro', 'spirit', 'belief', 'race', 'truth', 'medical', 'young', 'principle', 'meal', 'married', 'humanity', 'company', 'london', 'officer', 'question', 'camp', 'university', 'congregation', 'south', 'foot', 'washington', 'commander', 'entertainment', 'command', 'headquarters', 'gun', 'attack', 'troop', 'english', 'bishop', 'constitution', 'battle', 'southern', 'methodist', 'orleans', 'state', 'sin', 'political', 'corp', 'government', 'dab', 'treasury', 'slave', 'freedom', 'big', 'academy', 'friend', 'confederate', '1864', 'people', 'power', 'water', 'front', 'order', 'college', 'daughter', 'matter', 'lieutenant', 'individual', 'crime', 'desire', 'philadelphia', 'slavery', 'life', 'character', 'policy', 'colonel', 'tuskegee', 'bonaparte', 'conviction', 'march', 'fact', 'case', 'family', 'vote', 'men', 'hon', 'great', 'estate', 'future', 'church', 'room', 'trunk', 'general', 'army', 'hot', 'firing', 'york', 'secession', 'meeting', 'fort', 'judgment', 'lincoln', 'mule', 'brigade', 'force', 'large', 'deed', 'opinion',  'moral', 'position', 'captain', 'captured', 'god', 'infantry', 'regiment', 'sherman', 'school', 'richmond', 'gate', 'true', 'division', 'wounded', 'enemy', 'student', 'gen.', 'wealthy', 'devotion', 'jackson', 'work', 'artillery', 'sermon', 'teacher', 'cavalry', 'dollar', 'federal', 'rev', 'city', 'ignorant', 'county', 'human', 'home', 'capture', 'rear', 'prisoner', 'man', 'house', 'money', 'sympathy', 'professor', 'battery', 'evil', 'letter']

# don't touch, just the listmaker
def getdocs():
    url = 'https://raw.githubusercontent.com/ACM-Research/text-mining-extraction/main/first-person-narratives-american-south/data/toc.csv'
    response = urllib.request.urlopen(url)
    lines = [l.decode('utf-8') for l in response.readlines()]
    cr = csv.reader(lines)

    doclist = []
    docnames = []
    for row in cr:
        doclist.append(row[5])
        docnames.append(row[2])
    doclist.remove('URL(text-only)')
    docnames.remove('Title')
    return doclist, docnames

doclist, docnames = getdocs()

sia = SentimentIntensityAnalyzer()

# gets individual file and creates blob
def display_get_file_ready(num,print_status):
    if num > 150:
        num = 149
    elif num < 0:
        num = 0
    response = requests.get(doclist[num])
    response.encoding = "utf-8"
    file = response.text
    blob = TextBlob(file)
    if (print_status == 0):
        print ("\nYour file name is: \"" + docnames[num] + "\"")
    return blob

def get0(print_status,blob):
    noval = 0
    for sentence in blob.sentences:
        a = sia.polarity_scores(sentence)
        val_comp = a["compound"]
        if val_comp == 0.0:
            noval += 1
    if print_status == 0:
            print("Number of sentences with compound score of 0 is: " + str(noval) + "\n")
    return noval

def agg_sen_vals(print_status,blob):
    docvals = []
    for sentence in blob.sentences:
        a = sia.polarity_scores(sentence)
        docvals.append(a)
    print("There are a total of " + str(len(docvals)) + " values.")
    if (print_status == 0):
        print (docvals)

def new_blob(blob):
    topic_blob = []
    for sentence in blob.sentences:
        for word in topic_list:
            if word in sentence:
                if sentence not in topic_blob:
                    topic_blob.append(str(sentence))
    return topic_blob

def topic_detailed_get_scores(print_status,blob):
    exp_neu,nonex_pos,nonex_neg,pos,neu,neg,comp,comp_total = 0,0,0,0,0,0,0,0
    for sentence in blob:
        a = sia.polarity_scores(sentence)
        val_comp = a["compound"]

        scores = [a["pos"],a["neu"],a["neg"]]
        largest = max(scores)
        if (scores.index(largest) == 0):
            pos += 1
        if (scores.index(largest) == 1):
            neu += 1
        if (scores.index(largest) == 2):
            neg += 1

        if (scores[0] > scores[2]):
            nonex_pos += 1
        elif (scores[0] == scores[2]):
            exp_neu += 1

        else:
            nonex_neg += 1

        comp_total += val_comp
        comp += 1

    comp_total = comp_total / comp

    if print_status == 0:
        print("Compound Total: " + str(comp_total))
        print("Neutral Sentences: " + str(neu))
        print("Explicitly Positive Sentences: " + str(pos))
        print("Explicitly Negative Sentences: " + str(neg))
        print("Explicitly Neutral Sentences: " + str(exp_neu))
        print("Leaning Positive Sentences: " + str(nonex_pos))
        print("Leaning Negative Sentences: " + str(nonex_neg) + "\n")

    if (nonex_neg > nonex_pos):
        score = (nonex_neg / comp) * 100
        return "neg",score,(nonex_pos/comp),(nonex_neg/comp),(exp_neu/comp)
    elif (nonex_pos > nonex_neg):
        score = (nonex_pos / comp) * 100
        return "pos",score,(nonex_pos/comp),(nonex_neg/comp),(exp_neu/comp)
    elif (nonex_pos == nonex_pos):
        score = (neu / comp) * 100
        return "balanced-neu",score,(nonex_pos/comp),(nonex_neg/comp),(exp_neu/comp)
    else:
        score = (neu / comp) * 100
        return "neu",score,(nonex_pos/comp),(nonex_neg/comp),(exp_neu/comp)

def detailed_get_scores(print_status,blob):
    exp_neu,nonex_pos,nonex_neg,pos,neu,neg,comp,comp_total = 0,0,0,0,0,0,0,0
    for sentence in blob.sentences:
        a = sia.polarity_scores(sentence)
        val_comp = a["compound"]

        scores = [a["pos"],a["neu"],a["neg"]]
        largest = max(scores)
        if (scores.index(largest) == 0):
            pos += 1
        if (scores.index(largest) == 1):
            neu += 1
        if (scores.index(largest) == 2):
            neg += 1

        if (scores[0] > scores[2]):
            nonex_pos += 1
        elif (scores[0] == scores[2]):
            exp_neu += 1

        else:
            nonex_neg += 1

        comp_total += val_comp
        comp += 1

    comp_total = comp_total / comp

    if print_status == 0:
        print("Compound Total: " + str(comp_total))
        print("Neutral Sentences: " + str(neu))
        print("Explicitly Positive Sentences: " + str(pos))
        print("Explicitly Negative Sentences: " + str(neg))
        print("Explicitly Neutral Sentences: " + str(exp_neu))
        print("Leaning Positive Sentences: " + str(nonex_pos))
        print("Leaning Negative Sentences: " + str(nonex_neg) + "\n")

    if (nonex_neg > nonex_pos):
        score = (nonex_neg / comp) * 100
        return "neg",score,(nonex_pos/comp),(nonex_neg/comp),(exp_neu/comp)
    elif (nonex_pos > nonex_neg):
        score = (nonex_pos / comp) * 100
        return "pos",score,(nonex_pos/comp),(nonex_neg/comp),(exp_neu/comp)
    elif (nonex_pos == nonex_pos):
        score = (neu / comp) * 100
        return "balanced-neu",score,(nonex_pos/comp),(nonex_neg/comp),(exp_neu/comp)
    else:
        score = (neu / comp) * 100
        return "neu",score,(nonex_pos/comp),(nonex_neg/comp),(exp_neu/comp)

def console_display(num):
    blob = display_get_file_ready(num,0)
    topic_blob = new_blob(blob)
    topic_detailed_get_scores(0,topic_blob)
    get0(0,blob)
    detailed_get_scores(0,blob)
