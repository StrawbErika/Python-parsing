import urllib.request
import re
from bs4 import BeautifulSoup

def get_authors(content, author_position, count):
    author_content = content[author_position].find_all("div", class_="user-details")
    auth = author_content[count].contents
    final_author = clean_html(str(auth[1].contents).strip("[]"))
    return final_author

def get_complete_answer(answer_contents):
    authors = []
    authors.append(get_authors(answer_contents, 3, 0))
    description = clean_html(str(answer_contents[1].find_all("p")).strip("[]"))
    answer_data = {
        "Description" : description,
        "Authors" : authors, 
        # "Upvote" : upvote
    }
    return answer_data

def clean_html(raw_html):
    clean = re.compile('<.*?>')
    cleantxt = re.sub(clean, '', raw_html)
    return cleantxt

with urllib.request.urlopen('https://stackoverflow.com/questions/24458163/what-are-the-parameters-for-sklearns-score-function') as response:
   html = response.read()

soup = BeautifulSoup(html, 'html.parser')

data = {}

question_data = {}

question = soup.find_all("div", class_="postcell post-layout--right")
question_title = str(soup.title.contents).strip("[]") 
question_contents = question[0].contents
question_description = clean_html(str(question_contents[1].find_all("p")).strip("[]"))

question_authors = []
q_author_content = question_contents[5].find_all("div", class_="user-details")
i = 0
while(i != len(q_author_content)):
    get_authors(question_contents, 5, i)
    question_authors.append(get_authors(question_contents, 5, i))
    i=i+1

question_upvote = clean_html(str(soup.find("span", class_="vote-count-post")))
question_data = {
    "Question" : question_title,
    "Description" : question_description,
    "Authors" : question_authors, 
    "Upvote" :  question_upvote
}


list_of_answers = []

count = 0

answer = soup.find_all("div", class_="answercell post-layout--right")

while(count != len(answer)):
    ans=answer[count].contents
    list_of_answers.append(get_complete_answer(ans))
    count=count+1

data[str(question_data)] = list_of_answers
print(data)

file = open("answers.txt","w") 
file.write(str(question_authors))
file.close() 

