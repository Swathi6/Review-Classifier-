import os
import glob
from nltk import NaiveBayesClassifier
from nltk.corpus.reader import CategorizedPlaintextCorpusReader
import nltk
from nltk.corpus import wordnet as wn
import sys

Feature_Set={}


training_directory= "reviews"
Training_Corpus = CategorizedPlaintextCorpusReader(training_directory, r'pos|neg.*\.txt$', cat_pattern='(\w+)/*')

testing_directory= "reviews"
Testing_Corpus  = CategorizedPlaintextCorpusReader(testing_directory, r'pos|neg.*\.txt$', cat_pattern='(\w+)/*')



Training_Corpus_Text=nltk.RegexpTokenizer('\w+').tokenize(Training_Corpus.raw())
Positive_Corpus_Text=nltk.RegexpTokenizer('\w+').tokenize(Training_Corpus.raw(categories="pos"))
Negative_Corpus_Text=nltk.RegexpTokenizer('\w+').tokenize(Training_Corpus.raw(categories="neg"))

Training_Vocabulary = nltk.FreqDist(w.lower() for w in Training_Corpus_Text)
Positive_Vocabulary = nltk.FreqDist(w.lower() for w in Positive_Corpus_Text)
Negative_Vocabulary = nltk.FreqDist(w.lower() for w in Negative_Corpus_Text)


pos_den=float(len(Positive_Corpus_Text))+float(len(Positive_Vocabulary.keys()))
neg_den=float(len(Negative_Corpus_Text))+float(len(Negative_Vocabulary.keys()))

for word, tag in nltk.pos_tag(Training_Vocabulary.keys()[:500]):
    if tag=="JJ" or tag=="RB":
        if word in Positive_Vocabulary.keys():
                    Feature_Set[word, "pos"]=(float((Positive_Vocabulary.freq(word)*len(Positive_Corpus_Text))+1)/float(pos_den))
        else:
                    Feature_Set[word, "pos"]=(float(1/float(pos_den)))
              
        if word in Negative_Vocabulary.keys():
                    Feature_Set[word, "neg"]=(float((Negative_Vocabulary.freq(word)*len(Negative_Corpus_Text))+1)/float(neg_den))
        else:
                    Feature_Set[word, "neg"]=(float(1/float(neg_den)))      


file=open('model_file.txt', 'w')
file.write("Feature words\tCategory\tProb(given_word|category)\n")
for word, cat in Feature_Set.keys():
    file.write(str(word))
    file.write("\t\t")
    file.write((str(cat)))
    file.write("\t\t")
    file.write(str(Feature_Set[word,cat]))
    file.write("\n")

file.close()

Classification_Accuracy=0
    
for file in Testing_Corpus.fileids():
    pos_prob=1
    neg_prob=1
    real_category=Testing_Corpus.categories([file])
    
    for word, cat in Feature_Set:
        if word in Testing_Corpus.words([file]):
            if cat=="pos":
                pos_prob=Feature_Set[word, cat]*float(pos_prob)*10000
            else:    
                neg_prob=Feature_Set[word, cat]*float(neg_prob)*10000
        
    if float(pos_prob)>=float(neg_prob):
        derived_category="['pos']"
    else:
        derived_category="['neg']"
        
    if str(real_category)==str(derived_category):
        Classification_Accuracy=Classification_Accuracy + 1

print "Feature set is stored in model_file"
   
Classification_Accuracy=(float(Classification_Accuracy)/200 )*100
print "Classification_Accuracy:" + str(Classification_Accuracy) + "%"
 

        


