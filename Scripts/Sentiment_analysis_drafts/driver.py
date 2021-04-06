from functions import *
from mass_file_processing_functions import *

print ("Running files with topic-specific sentences...")
file_score_list_topic = topic_get_file()
prelim_stats(file_score_list_topic)
make_csv(file_score_list_topic,1)

print ("Running files without...")
file_score_list = topic_get_file()
prelim_stats(file_score_list)
make_csv(file_score_list,1)


# while (True):
#     num = int(input("Enter the number of a document, up to 151. Enter -1 to end: ")) - 1
#     if (num != -2):
#         console_display(num)
#     elif (num == -2):
#         exit(0)

