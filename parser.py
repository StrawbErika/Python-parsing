import urllib.request
import re
from bs4 import BeautifulSoup

with urllib.request.urlopen('https://stackoverflow.com/questions/24458163/what-are-the-parameters-for-sklearns-score-function') as response:
   html = response.read()

soup = BeautifulSoup(html, 'html.parser')

data = {}
list_of_answers = []

 
count = 0
answer = soup.find_all("div", class_="answercell post-layout--right")
while(count != len(answer)):
    ans=answer[count].contents
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', str(ans[1].find_all("p")).strip("[]"))
    list_of_answers.append(cleantext)
    count=count+1

data[str(soup.title.contents).strip("[]")] = list_of_answers

file = open("answers.txt","w") 
file.write(str(data))
file.close() 
