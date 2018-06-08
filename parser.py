import urllib.request
from bs4 import BeautifulSoup
from functions import *
from filewriter import *

with urllib.request.urlopen('https://stackoverflow.com/questions/30484028/file-handling-in-gui') as response:
   html = response.read()

soup = BeautifulSoup(html, 'html.parser')        

#complete quest: answer pair
data = {}

#gets all upvotes in the whole page
upvotes = soup.find_all("span", class_="vote-count-post")

# gets all posts 
list_of_all_comments = get_all_posts(soup)

# gets the complete question
complete_question = get_question(clean_html(str(upvotes[0])), list_of_all_comments[0], soup)    

# gets all answers
list_of_answers =  get_all_answers(soup, upvotes, list_of_all_comments)

data[str(complete_question)] = list_of_answers
data_json = to_json(data)

write_to_file(data_json)