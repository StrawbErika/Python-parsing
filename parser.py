import urllib.request
import re
from bs4 import BeautifulSoup

def cleanhtml(raw_html):
    clean = re.compile('<.*?>')
    cleantxt = re.sub(clean, '', raw_html)
    return cleantxt

with urllib.request.urlopen('https://stackoverflow.com/questions/24458163/what-are-the-parameters-for-sklearns-score-function') as response:
   html = response.read()

soup = BeautifulSoup(html, 'html.parser')

data = {}
list_of_answers = []

count = 0
answer = soup.find_all("div", class_="answercell post-layout--right")
while(count != len(answer)):
    ans=answer[count].contents
    list_of_answers.append(cleanhtml(str(ans[1].find_all("p")).strip("[]")))
    count=count+1

question_data = {}

question = soup.find_all("div", class_="postcell post-layout--right")
questions = str(soup.title.contents).strip("[]") 
question_contents = question[0].contents
description = cleanhtml(str(question_contents[1].find_all("p")).strip("[]"))

question_authors = []
author_content = question_contents[5].find_all("div", class_="user-details")
i = 0
while(i != len(author_content)):
    auth=author_content[i].contents
    question_authors.append(str(auth[1].contents).strip("[]"))
    i=i+1

upvote = cleanhtml(str(soup.find("span", class_="vote-count-post")))
# print()
question_data = {
    "Question" : questions,
    "Description" : description,
    "Authors" : question_authors, 
    "Upvote" : upvote
}

data[str(question_data)] = list_of_answers
print(data)

file = open("answers.txt","w") 
file.write(str(question))
file.close() 

