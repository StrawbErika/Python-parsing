import urllib.request
from bs4 import BeautifulSoup
from functions import *
from filewriter import *

with urllib.request.urlopen('file:///home/shortcake/Desktop/OJT/parsing/stackoverflow.html') as response:
   html = response.read()

soup = BeautifulSoup(html, 'html.parser')
        
data = {}
upvotes = soup.find_all("span", class_="vote-count-post")
list_of_all_comments = get_all_posts(soup)
complete_question = get_question(clean_html(str(upvotes[0])), list_of_all_comments[0], soup)    
list_of_answers =  get_all_answers(soup, upvotes, list_of_all_comments)

data[str(complete_question)] = list_of_answers
data_json = to_json(data)

write_to_file("answers.txt", data_json)