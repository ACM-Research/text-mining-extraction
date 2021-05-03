# N-Grams and Wordcloud Generation
An n-gram is a continuous sequence of n items from a given sample of text or speech. This script is designed to process a set of documents and performs various N-Gram calculations on them. After importing and installing the necessary libraries, the script is provided the path to the subdirectory containing all the historic documents in .txt format. These documents have been downloaded prior to the script being run. Then, with the necessary resources loaded, the script begins by “cleaning” all the text documents. This preprocessing includes removing stopwords, removing punctuation, and removing numbers, all of which would otherwise hinder the calculations. After that, the script begins the actual n-gram analysis, where it algorithmically goes through all the text documents and keeps a tally of all the bigram (two word phrases) and trigrams (three word phrases) in the document. Once it has made the necessary calculations, the script then plots the top 20 bigrams and trigrams as both a bar graph and a wordcloud for visualization. Meaningless prepositional phrases are also selectively discarded.

## Libraries Used

- [tm](https://cran.r-project.org/web/packages/tm/index.html)
- [ggplot2](https://cran.r-project.org/web/packages/ggplot2/index.html)
- [reshape2](https://cran.r-project.org/web/packages/reshape2/index.html)
- [wordcloud](https://cran.r-project.org/web/packages/wordcloud/)
- [Rweka](https://cran.r-project.org/web/packages/RWeka/index.html)

## Datasets Used

- [First-Person Narratives of the American South](https://docsouth.unc.edu/fpn/)
