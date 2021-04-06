from matplotlib import pyplot as plt
import csv

def show_data(filename):
    data_list = []
    pos_list = []
    neg_list = []
    neu_list = []
    with open(filename,'r') as doc:
        data = csv.reader(doc)
        for row in data:
            data_list.append(row)
    #['Title', 'Designation', 'Score', 'Pos_Val', 'Neg_Val', 'Neu_Val', 'Number']
    data_list.remove(data_list[0])
    print (data_list)
    num_pos = num_neu = num_neg = 0
    for i in data_list:
        num_pos += float(i[3])
        num_neg += float(i[4])
        num_neu += float(i[5])

    designation = [num_pos,num_neg,num_neu]
    print (designation)
    name = ["pos","neg","neu"]

    plt.figure(figsize=(10, 7))
    plt.pie(designation, labels=name)
    plt.show()

show_data('doc_designations_csv.csv')
show_data('topic_doc_designations_csv.csv')