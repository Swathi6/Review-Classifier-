Review-Classifier-
==================

This project aim to classify reviews from goodreads.com as positive/negative based on the text semantic analysis. 

Currently the project has two python programs. 

Extract_reviews: This program asks for the user to provide a book_name prefixed with goodreads book ID. 
The program uses BeautifulSoup and web scrapping techniques to extract the book reviews and the original ratings. 
The reviews are stored in small text files according to the original corresponding rating provided with the review.

Naive Bayes Classifier: This program reads the review files. 
Performs naive bayes classification using the review files as both training and test data. 
The classification accuracy of this program is just a measurement on how good the program was able to correctly classify.

Goal: The future goal of the project is to introduce techniques to improve the classification accuracy of Naive Bayes Classifier program of course.
New algorithmic techinques will be added. 
Monte carlo simulations will be conducted.

The eventual goal is to build a classifier which could classify with high percentage of efficiency on a varying range of review sets.

The project is built on Python 2.7.
The project uses nltk, BeautifulSoup, numpy, re.
