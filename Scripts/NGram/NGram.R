library(tm)
library(ggplot2)
library(reshape2)
library(wordcloud)
library(RWeka)

path = "./Documents"
dir = DirSource(paste(path,"./texts",sep=""), encoding = "UTF-8")
corpus = Corpus(dir)
length(corpus)
corpus[1]

corpus.ng = tm_map(corpus,removeWords,c(stopwords(),"s","ve"))
corpus.ng = tm_map(corpus.ng,removePunctuation)
corpus.ng = tm_map(corpus.ng,removeNumbers)

BigramTokenizer <- function(x) NGramTokenizer(x, Weka_control(min = 2, max = 2))
tdm.bigram = TermDocumentMatrix(corpus.ng, control = list(tokenize = BigramTokenizer))
freq = sort(rowSums(as.matrix(tdm.bigram)),decreasing = TRUE)
freq.df = data.frame(word=names(freq), freq=freq)
head(freq.df, 20)

pal=brewer.pal(8,"Blues")
pal=pal[-(1:3)]

wordcloud(freq.df$word,freq.df$freq,max.words=100,random.order = F, colors=pal)

ggplot(head(freq.df,15), aes(reorder(word,freq), freq)) +
  geom_bar(stat = "identity") + coord_flip() +
  xlab("Bigrams") + ylab("Frequency") +
  ggtitle("Most frequent bigrams")

TrigramTokenizer <- function(x) NGramTokenizer(x, Weka_control(min = 3, max = 3))
tdm.trigram = TermDocumentMatrix(corpus.ng,
                                 control = list(tokenize = TrigramTokenizer))

freq = sort(rowSums(as.matrix(tdm.trigram)),decreasing = TRUE)
freq.df = data.frame(word=names(freq), freq=freq)
head(freq.df, 20)

wordcloud(freq.df$word,freq.df$freq,max.words=100,random.order = F, colors=pal)

ggplot(head(freq.df,15), aes(reorder(word,freq), freq)) +   
  geom_bar(stat="identity") + coord_flip() + 
  xlab("Trigrams") + ylab("Frequency") +
  ggtitle("Most frequent trigrams")
