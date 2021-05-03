# Interpreting Historical Data Using Text-Mining Extraction

## Poster
![poster.png](./poster.png)
## Purpose
The purpose of this project is to learn more about civilians’ perspectives during the Civil War era in America using methods of information retrieval and clustering alongside syntactical analysis and lexical semantics. Along with coming to historical conclusions, this project seeks to develop relevant and descriptive tools for historical text-mining and evaluate their efficacy for our particular data source.

## Data



## Methods

### Flesch Reading Ease
This script processes a directory of .txt files and uses the textstat library to calculate the Flesch Reading Ease score for each document. A separate script processes .csv files of the scores and generates a box plot. The other libraries and datasets used can be seen in the readme in the scripts subfolder.
### Topic Modelling
This script finds common and context relevant words and groups them into clusters to find topics within texts. A Latent Dirichlet Model (LDA) is used to map the words into the clusters. Output files include comparisons by gender, military affiliation, and impact of religion on text.
### N-Grams
This script finds recurring bi-grams (two word combinations) and tri-grams (three word combinations) within the text to find common ideas within the texts. The program keeps tally of the bi-grams and tri-grams then returns the most common and relevant ones.
### Sentiment Analysis
These scripts calculate the Polarity (Positive/Neutral/Negative attitude) and Subjectivity (Emotional-Factual content) within a text. The program calculates both scores and keeps track in a csv file. Graphs included are across demographics.

## Results
 - Black authors wrote about topics pertaining to improving living standards for African-Americans, such as education, religion, and family life.
 - Writing complexity was standard across different demographics including economic class, race, and gender
 - Our programs can process the entire dataset (150 documents) in ~10 minutes, vs. our manual annotation process which took ~3 months
## Conclusion
The programs we created allowed us to establish preliminary conclusions based on the corpus. They also helped us and will help future historians to better understand general perspectives and the context of a document without having to read it first. In the future, our next course of action would be to implement ways to detect false positives, such as sarcasm, in analyzed documents. Sentences with positive connotations, but negative language skewed our results. Detection of false positives would help to alleviate the issue and create more accurate analyses.
## Contributors

- [Sophie Horner](https://github.com/hornersc)
- [Andrew Tran](https://github.com/nartmobile)
- [Pavan Govu](https://github.com/pavangovu)
- [Pax Gole](https://github.com/paxgole)
- [Abby Thomas](https://github.com/thomasabigail) - Research Lead
- [Brian Nguyen](https://github.com/briannoogin) - Graduate Advisor
- [Dr. Karen Mazidi](https://github.com/kjmazidi) - Faculty Advisor
