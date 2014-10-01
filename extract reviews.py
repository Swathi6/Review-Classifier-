from bs4 import BeautifulSoup
import requests
import re
import os


#get the book name and make a beautifulsoup from goodreads.com
book_name = raw_input("Enter the book_name:")
url = requests.get("http://www.goodreads.com/book/show/" +book_name)
soup = BeautifulSoup(url.text)

#create positive and negative review files
positive_reviews = open("positive_reviews.txt", 'w')
negative_reviews = open("negative_reviews.txt", 'w')


reviews = soup.find_all('div', attrs={"class": "left bodycol"})
index = 0

for review in reviews:
    index = index + 1
    for rating in review.find_all('a', attrs={'class':re.compile(r"\bstaticStars\b")}):        
        review_rating = rating.text[0]
    for content in review.find_all('div', attrs={"class": "reviewText stacked"}):
        actual_content= content.find_all('span')[-1]
        review_text = actual_content.text
    if review_rating == '1' or review_rating == '2':       
        file_name = "neg." + str(index) +".txt"
    else:
        file_name = "pos." + str(index) + ".txt"
    if not os.path.exists("reviews"):
        os.makedirs("reviews")
    file_name = os.path.join("reviews", file_name)    
    review_file = open(file_name, 'w')
    review_file.write(review_text.encode('ascii', 'ignore'))
    review_file.close()


    

    

'''
for rating in soup.find_all('div', attrs={"class": "reviewHeader uitext stacked"}):
        for rank in rating.find_all('a', attrs={'class':re.compile(r"\bstaticStars\b")}):
                print rank[0]


for review in soup.find_all('div', attrs={"class": "reviewText stacked"}):
        print review.text

'''

    

