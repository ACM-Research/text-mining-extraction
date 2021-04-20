This is info about each script in this folder.
  1. test.py - Test Version of the basic sentiment script


## Flesch-Kincaid Grade Level and Flesch Reading Ease
This script processes a directory of .txt files and performs Flesch-Kincaid Grade Level and Flesch Reading Ease calculations on them.

- It has been designed with this dataset in mind, where the original data contains publisher and 3rd party corrections contained within brackets []. The dataset also has artifacts of '*' characters and newlines for formatting. The script removes these characters and messages because they are not representative of what was actually written by the author.

- The script then merges the entire text file into one string, which is then run through [textstat](https://github.com/shivam5992/textstat). The script returns these values into two columns in the output.txt, the first for Reading Level and the second for Grade Level.

## Sentiment Analysis - Polarity and Subjectivity
Libraries used:
 - VADER Sentiment
 - TextBlob
 - csv
 - matplotlib
 - ast

This folder contains 3 scripts - file_prep, file_score, file_display. File prep prepares the toc.csv file and creates a matrix for the data. File score scores each sentence of each document and returns the information to the original matrix. File display contains a series of functions to call and create pie charts for display and saves them as png.
