import urllib.request
import re
from bs4 import BeautifulSoup
import json

def to_json(dictionary):
    return json.dumps(dictionary)


def get_authors(content, author_position, count):
    author_content = content[author_position].find_all("div", class_="user-details")
    auth = author_content[count].contents
    final_author = clean_html(str(auth[1].contents).strip("[]"))
    return final_author

def get_complete_answer(answer_contents, upvote, comments):
    authors = []
    authors.append(get_authors(answer_contents, 3, 0))
    description = clean_html(str(answer_contents[1].find_all("p")).strip("[]"))
    upvote = clean_html(str(upvote))
    answer_data = {
        "Description" : description,
        "Authors" : authors, 
        "Upvote" : upvote,
        "Comments": comments
    }
    return answer_data

def get_comments(comment):
    comment_body = comment.find("div", class_="comment-body")
    comment_content = comment_body.find("span", class_="comment-copy")
    comment_author = comment_body.find("a", class_="comment-user")
    complete_comment = {
        "Content" : clean_html(str(comment_content)),
        "Author" : clean_html(str(comment_author))
    }
    return complete_comment

def get_all_comments(comment_container):
    list_of_comments = []
    comment = comment_container.find_all("div", class_="comment-text js-comment-text-and-form")
    num = 0
    while(num != len(comment)):
        list_of_comments.append(get_comments(comment[num]))
        num = num + 1
    return list_of_comments

def clean_html(raw_html):
    clean = re.compile('<.*?>')
    cleantxt = re.sub(clean, '', raw_html)
    return cleantxt

with urllib.request.urlopen('https://stackoverflow.com/questions/26660654/how-do-i-print-the-key-value-pairs-of-a-dictionary-in-python/26660785') as response:
   html = response.read()

soup = BeautifulSoup(html, 'html.parser')

def get_all_posts(store):
    all_posts =soup.find_all("div", class_="post-layout")
    j = 0
    while(j != len(all_posts)):
        list_of_all_comments.append(get_all_comments(all_posts[j])) 
        j = j + 1
        
list_of_all_comments = []
data = {}
question_data = {}

get_all_posts(list_of_all_comments)

def get_question(upvote, comment):
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
    question_data = {
        "Question" : question_title,
        "Description" : question_description,
        "Authors" : question_authors, 
        "Upvote" :  upvote,
        "Comments" : comment
    }

upvotes = soup.find_all("span", class_="vote-count-post")

get_question(clean_html(str(upvotes[0])), list_of_all_comments[0])    

list_of_answers = []
count = 0
answer = soup.find_all("div", class_="answercell post-layout--right")
while(count != len(answer)):
    ans=answer[count].contents
    list_of_answers.append(get_complete_answer(ans, upvotes[count+1], list_of_all_comments[count+1]))
    count=count+1


data[str(question_data)] = list_of_answers

print(to_json(data))
file = open("answers.txt","w") 
file.write("Questions" + "\n")
for k, v in data.items():
    file.write(str(k) + "\n" + "\n")
    file.write("Answers" + "\n")
    for x in v:
        file.write("\n")
        for a, b in x.items():
            file.write(str(a) + " ")
            file.write(str(b) + "\n")
file.close() 
