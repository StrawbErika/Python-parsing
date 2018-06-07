import urllib.request
with urllib.request.urlopen('https://stackoverflow.com/questions/24458163/what-are-the-parameters-for-sklearns-score-function') as response:
   html = response.read()

file = open("stackoverflow.txt","w") 
file.write(str(html))
file.close() 