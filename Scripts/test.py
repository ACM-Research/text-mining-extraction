from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import requests, csv, urllib.request

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


sia = SentimentIntensityAnalyzer()
def run_sentiment(num):
    if num > 150:
        num = 149
    elif num < 0:
        num = 0
    response = requests.get(doclist[num])
    response.encoding = "utf-8"
    file = response.text
    blob = TextBlob(file)
    print ("Your file name is: \"" + docnames[num] + "\"\n")

    def Vbynum_subj(divisor, remainder,print_status):
        count,subj_count,call_count = 0,0,0
        for sentence in blob.sentences:
            if (count % divisor == remainder):
                a = sia.polarity_scores(sentence)
                val = a["compound"]
                if val != 0:
                    subj_count += val
                    call_count += 1
            count += 1
        subj_count = subj_count / call_count
        if print_status == 0:
            print(str(call_count) + ", by remainder " + str(remainder) + "'s and divisor " + str(divisor) + "'s: " + str(subj_count))
        return subj_count

    def print0textblob():
        count = 0
        for sentence in blob.sentences:
            a = sentence.sentiment.subjectivity
            b = sentence.sentiment.polarity
            if (a and b) == 0:
                print (sentence + "\n")
        return count

    def Vget0():
        count = 0
        for sentence in blob.sentences:
            a = sia.polarity_scores(sentence)
            if a == 0:
                count += 1
            return count

    def get0():
        count = 0
        for sentence in blob.sentences:
            a = sentence.sentiment.subjectivity
            b = sentence.sentiment.polarity
            if (a and b) == 0:
                count += 1
        return count

    def bynum_subj(divisor, remainder,print_status):
        count,subj_count,call_count = 0,0,0
        for sentence in blob.sentences:
            if (count % divisor == remainder):
                a = sentence.sentiment.subjectivity
                if a != 0:
                    subj_count += a
                    call_count += 1
            count += 1
        subj_count = subj_count / call_count
        if print_status == 0:
            print(str(call_count) + ", by " + str(remainder) + "'s and " + str(divisor) + "'s: " + str(subj_count))
        return subj_count

    def bynum_pol(divisor, remainder,print_status):
        count,pol_count,call_count = 0,0,0
        for sentence in blob.sentences:
            if (count % divisor == remainder):
                a = sentence.sentiment.polarity
                if a != 0:
                    pol_count += a
                    call_count += 1
            count += 1
        pol_count = pol_count / call_count
        if print_status == 0:
            print(str(call_count) + ", by " + str(remainder) + "'s and " + str(divisor) + "'s: " + str(pol_count))
        return pol_count

    def console_display():
        print ("First, with TextBlob")
        print ("The number of sentences without a value are " + str(get0()) + "\n")
        bynum_subj(2,0,0)
        bynum_subj(2,1,0)
        bynum_subj(3,0,0)
        bynum_subj(5,0,0)
        bynum_subj(7,0,0)
        bynum_subj(1,0,0)

        avg_subj = (bynum_subj(2,0,1) + bynum_subj(2,1,1) + bynum_subj(3,0,1) + bynum_subj(5,0,1) + bynum_subj(7,0,1) + bynum_subj(1,0,1)) / 6
        print ("Subjetivity with TextBlob is " + str(avg_subj) + "\n")

        bynum_pol(2,0,0)
        bynum_pol(2,1,0)
        bynum_pol(3,0,0)
        bynum_pol(5,0,0)
        bynum_pol(7,0,0)
        bynum_pol(1,0,0)

        avg_pol = (bynum_pol(2,0,1) + bynum_pol(2,1,1) + bynum_pol(3,0,1) + bynum_pol(5,0,1) + bynum_pol(7,0,1) + bynum_pol(1,0,1)) / 6
        print ("Polarity with TextBlob is " + str(avg_pol))

        print ("\n" +"Next, with Vader")
        print ("The number of sentences without a value are " + str(Vget0()) + "\n")
        Vbynum_subj(2,0,0)
        Vbynum_subj(2,1,0)
        Vbynum_subj(3,0,0)
        Vbynum_subj(5,0,0)
        Vbynum_subj(7,0,0)
        Vbynum_subj(1,0,0)

        avg_subj = (Vbynum_subj(2,0,1) + Vbynum_subj(2,1,1) + Vbynum_subj(3,0,1) + Vbynum_subj(5,0,1) + Vbynum_subj(7,0,1) + Vbynum_subj(1,0,1)) / 6
        print ("Subjetivity with Vader is " + str(avg_subj))

    get0()
    print0textblob()
    # console_display()
    # def txt_export(): - next step is a complete, exportable file with all the data for the selected text

while (True):
    num = int(input("Enter the number of a document, up to 151. Enter -1 to end: ")) - 1
    if (num != -2):
        run_sentiment(num)
    elif (num == -2):
        exit(0)