from file_scoring import *
import csv

def open_database(csvfile):
    with open(csvfile,'r') as f:
        lines = f.readlines()
    cr = list(csv.reader(lines))
    cr.remove(cr[0])
    file_matrix = []
    # [['Filename','Race','Gender','Economic Status','Military Status',
    #                     'Religious/Spiritual Content',
    #                     'Polarity Data'[pol_avg,all_lines,fin_desig,pos_avg,pos_lines,neg_avg,neg_lines,neu_avg,neu_lines],
    #                     'Subjectivity Data'[subj_avg,all_lines,fin_desig,sub_avg,sub_lines,obj_avg,obj_lines,dec_list],
    #                     'Number of Lines']]
    for thing in cr:
        lst = []
        pol_data = []
        sub_data = []
        demdata = thing[8]
        race = demdata[6]
        gender = demdata[16]
        ec_stat = demdata[35]
        ml_stat = demdata[54]
        rs_cont = demdata[85]
        lst.extend([thing[0],race,gender,ec_stat,ml_stat,rs_cont,pol_data,sub_data,0])
        file_matrix.append(lst)
    return file_matrix

def modify_matrix(file_matrix):
    for file_data in file_matrix:
        idx = file_matrix.index(file_data)
        file_matrix[idx] = run_scoring(file_data)
    return file_matrix

def write_csv(file_matrix):
    with open('fpn_csv_data.csv','w') as f:
        field_names = ['Filename','Race','Gender','Economic Status','Military Status','Religious/Spiritual Content',
                        'pol_avg','pol_fin_desig','pos_avg','pos_lines','neg_avg','neg_lines','neu_avg','neu_lines',
                       'subj_avg','subj_fin_desig','sub_avg','sub_lines','obj_avg','obj_lines','dec_list',
                       'Number of Lines']
        w = csv.DictWriter(f, fieldnames=field_names)
        for document in file_matrix:
            w.writerow({'Filename':document[0],'Race':document[1],'Gender':document[2],'Economic Status':document[3],
                        'Military Status':document[4],'Religious/Spiritual Content':document[5],
                        'pol_avg':document[6][0],'pol_fin_desig':document[6][2],'pos_avg':document[6][3],'pos_lines':document[6][4],
                        'neg_avg':document[6][5],'neg_lines':document[6][6],'neu_avg':document[6][7],'neu_lines':document[6][8],
                        'subj_avg':document[7][0],'subj_fin_desig':document[7][2],'sub_avg':document[7][3],'sub_lines':document[7][4],
                        'obj_avg':document[7][5],'obj_lines':document[7][6],'dec_list':document[7][7],
                        'Number of Lines':document[8]})


file_matrix = open_database('Annotations Spreadsheet.xlsx - toc.csv')
file_matrix = modify_matrix(file_matrix)
write_csv(file_matrix)

print ("Done!")
