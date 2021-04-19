import csv
import matplotlib.pyplot as plt
import ast

csv_file = open('fpn_csv_data.csv','r')
reader = csv.reader(csv_file)
data_file = open('fpn_txt_results.txt','w')

def write_dem_data(data_set):
    reader = data_set
    race_data = [0, 0, 0]
    races = ["White", "Black", "Mixed"]

    gender_data = [0, 0]
    genders = ["Female", "Male"]

    economic_data = [0, 0, 0]
    economic_statuses = ['Upper', "Middle", "Lower"]

    military_data = [0,0]
    military_statuses = ["Yes","No"]

    religious_data = [0,0]
    religious_statuses = ["Yes","No"]

    for row in reader:

        # race
        if row[1] == 'W':
            race_data[0] += 1
        elif row[1] == 'B':
            race_data[1] += 1
        elif row[1] == 'M':
            race_data[2] += 1
        # gender
        if row[2] == 'F':
            gender_data[0] += 1
        elif row[2] == 'M':
            gender_data[1] += 1
        # economic status
        if row[3] == 'U':
            economic_data[0] += 1
        elif row[3] == 'M':
            economic_data[1] += 1
        elif row[3] == 'P':
            economic_data[2] += 1
        # military status
        if row[4] == 'Y':
            military_data[0] += 1
        elif row[4] == 'N':
            military_data[1] += 1
        # religious content
        if row[5] == 'Y':
            religious_data[0] += 1
        elif row[5] == 'N':
            religious_data[1] += 1

    data_file.write("Basic Demographic Data: \n")
    data_file.write(str(race_data)+' '+str(races)+'\n'+str(gender_data)+' '+str(genders)+'\n'+
                    str(economic_data)+' '+str(economic_statuses)+'\n'+
                    str(military_data)+' '+str(military_statuses)+'\n'+
                    str(religious_data)+' '+str(religious_statuses)+'\n')
    return race_data,races,gender_data,genders,economic_data,economic_statuses,military_data,\
           military_statuses,religious_data,religious_statuses

def datachart(data,labels,title):
    plt.pie(data, labels=labels, autopct='%.2f%%')
    plt.title(title)
    # plt.show()
    title = title + '.png'
    plt.savefig(title)

def pol_data(reader,status,titleseed,attributeindex):
    data_set = reader
    data = [0,0,0]
    for row in data_set:
        if row[attributeindex] == str(status):
            data[0] += int(row[9])
            data[1] += int(row[11])
            data[2] += int(row[13])
    title = "Polarity Data By " + titleseed + " - " + status
    labels = ['Positive', 'Negative', 'Neutral']
    datachart(data, labels, title)

def sub_data(reader,status,titleseed,attributeindex):
    data_set = reader
    data = [0,0,0,0,0]
    for row in data_set:
        if row[attributeindex] == str(status):
            ls = ast.literal_eval(row[20])
            data[0] += (ls[0] + ls[1])
            data[1] += (ls[2] + ls[3])
            data[2] += (ls[4] + ls[5])
            data[3] += (ls[6] + ls[7])
            data[4] += (ls[8] + ls[9] + ls[10])
    title = "Subjectivity Data By " + titleseed + " - " + status
    labels = ['Objective','Mostly Objective','Either Objective or Subjective','Mostly Subjective','Subjective']
    datachart(data, labels, title)


# sub_data(reader,'W',"Race",1)
# sub_data(reader,'B',"Race",1)
# sub_data(reader,'M',"Race",1)
#
# sub_data(reader,'F',"Gender",2)
# sub_data(reader,'M',"Gender",2)
#
# sub_data(reader,'U',"Economic Status",3)
# sub_data(reader,'M',"Economic Status",3)
# sub_data(reader,'P',"Economic Status",3)
#
# sub_data(reader,'Y',"Military Status",4)
# sub_data(reader,'N',"Military Status",4)
#
# sub_data(reader,'Y',"Religious Content",5)
# sub_data(reader,'N',"Religious Content",5)


# pol_data(reader,'W',"Race",1)
# pol_data(reader,'B',"Race",1)
# pol_data(reader,'M',"Race",1)
#
# pol_data(reader,'F',"Gender",2)
# pol_data(reader,'M',"Gender",2)
#
# pol_data(reader,'U',"Economic Status",3)
# pol_data(reader,'M',"Economic Status",3)
# pol_data(reader,'P',"Economic Status",3)
#
# pol_data(reader,'Y',"Military Status",4)
# pol_data(reader,'N',"Military Status",4)
#
# pol_data(reader,'Y',"Religious Content",5)
# pol_data(reader,'N',"Religious Content",5)

# race_data,races,gender_data,genders,economic_data,economic_statuses,military_data,\
#            military_statuses,religious_data,religious_statuses = write_dem_data(reader)


csv_file.close()
data_file.close()