from functions import *


doclist, docnames = getdocs()
sia = SentimentIntensityAnalyzer()

def get_file():
    class file_scores:
        def __init__(self, title, designation, score,pos_val,neg_val,neu_val):
            self.title = title
            self.designation = designation
            self.score = score
            self.pos_val = pos_val
            self.neg_val = neg_val
            self.neu_val = neu_val


        def __repr__(self):
            return "title: \"% s\", designation: \"% s\", score: \"% s\", pos_val: \"% s\", neg_val: \"% s\",neu_val: \"% s\"" % (self.title,self.designation,self.score,self.pos_val,self.neg_val,self.neu_val)

    file_score_list = []
    max = int(input("How many files will we be running today?     "))
    showrun = input("Would you like to see the digit of the document running while the program runs? y/n     ")
    print(str(max) + " files running...")
    i = 0
    for thing in docnames:
        blob = display_get_file_ready(i,1)
        designation,score,pos_val,neg_val,neu_val = detailed_get_scores(1,blob)
        file_score_list.append(file_scores(thing,designation,score,pos_val,neg_val,neu_val))
        i += 1
        if showrun == 'y':
            print(str(i)+"... ",end="")
        if i == max:
            print ("\nHit " + str(max) + " files!\n")
            break

    txt_input = input("\nSave to .txt file? y/n: ")
    if txt_input == 'y':
        with open('Full_Document_Scores.txt', 'w') as out:
            for thing in file_score_list:
                out.write(str(thing))
                out.write("\n")

    return file_score_list

def prelim_stats(file_score_list):
    print ("These are statistics about the files you ran.")
    num_of_pos,num_of_neu,num_of_neg,num_of_bneu = 0,0,0,0
    for thing in file_score_list:
        if thing.designation == "neu":
            num_of_neu += 1
        if thing.designation == "pos":
            num_of_pos += 1
        if thing.designation == "neg":
            num_of_neg += 1
        if thing.designation == "balanced_neu":
            num_of_bneu += 1

    print("Number of 'Balanced' Neutral Documents: " + str(num_of_bneu))
    print("Number of Primarily Neutral Documents: " + str(num_of_neu))
    print("Number of Primarily Positive Documents: " + str(num_of_pos))
    print("Number of Primarily Negative Documents: " + str(num_of_neg))
    doc_desig_list = [num_of_bneu,num_of_neu,num_of_pos,num_of_neg]
    return doc_desig_list

def make_csv(file_score_list,topic):
    if topic == 1:
        filename = 'topic_doc_designations_csv.csv'
    else:
        filename = 'doc_designations_csv.csv'
    with open(filename, mode='w') as desig_csv:
        docwriter = csv.writer(desig_csv,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        docwriter.writerow(["Title","Designation","Score","Pos_Val","Neg_Val","Neu_Val"])
        for thing in file_score_list:
            docwriter.writerow([thing.title,thing.designation,thing.score,thing.pos_val,thing.neg_val,thing.neu_val])






def topic_get_file():
    class file_scores:
        def __init__(self, title, designation, score,pos_val,neg_val,neu_val):
            self.title = title
            self.designation = designation
            self.score = score
            self.pos_val = pos_val
            self.neg_val = neg_val
            self.neu_val = neu_val


        def __repr__(self):
            return "title: \"% s\", designation: \"% s\", score: \"% s\", pos_val: \"% s\", neg_val: \"% s\",neu_val: \"% s\"" % (self.title,self.designation,self.score,self.pos_val,self.neg_val,self.neu_val)

    file_score_list = []
    max = int(input("How many files will we be running today?     "))
    showrun = input("Would you like to see the digit of the document running while the program runs? y/n     ")
    print(str(max) + " files running...")
    i = 0
    for thing in docnames:
        blob = display_get_file_ready(i,1)
        topic_blob = new_blob(blob)
        designation,score,pos_val,neg_val,neu_val = topic_detailed_get_scores(1,topic_blob)
        file_score_list.append(file_scores(thing,designation,score,pos_val,neg_val,neu_val))
        i += 1
        if showrun == 'y':
            print(str(i)+"... ",end="")
        if i == max:
            print ("\nHit " + str(max) + " files!\n")
            break

    txt_input = input("\nSave to .txt file? y/n: ")
    if txt_input == 'y':
        with open('Full_Document_Scores_(topic-modelled).txt', 'w') as out:
            for thing in file_score_list:
                out.write(str(thing))
                out.write("\n")

    return file_score_list