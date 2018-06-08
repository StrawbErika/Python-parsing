import re
import json
from bs4 import BeautifulSoup

# cleans html tags
def clean_html(raw_html):
    clean = re.compile('<.*?>')
    cleantxt = re.sub(clean, '', raw_html)
    return cleantxt

# converts dict to json
def to_json(dictionary):
    return json.dumps(dictionary)

# returns the list of all complete answers 
def get_all_answers(soup, upvotes, list_of_all_comments):
    answer_list = []
    count = 0
    answer = soup.find_all("div", class_="answercell post-layout--right")
    
    # goes through the list of answer contents it found
    while(count != len(answer)):
        ans=answer[count].contents
        # given list of upvotes & comments, it passes it to get_complete_answer
        answer_list.append(get_complete_answer(ans, upvotes[count+1], list_of_all_comments[count+1], soup))
        count=count+1
    return answer_list

# given the whole answer contents it finds the description & puts it in the dict 
def get_complete_answer(answer_contents, upvote, comments, soup):
    authors = []
    authors.append(get_authors(answer_contents, 3, 0, soup))
    description = clean_html(str(answer_contents[1].find_all("p")).strip("[]"))
    upvote = clean_html(str(upvote))
    answer_data = {
        "Description" : description,
        "Authors" : authors, 
        "Upvote" : upvote,
        "Comments": comments
    }
    return answer_data

# finds the author given the content
def get_authors(content, author_position, count, soup):
    author_content = content[author_position].find_all("div", class_="user-details")
    auth = author_content[count].contents
    final_author = clean_html(str(auth[1].contents).strip("[]"))
    return final_author

# gets all post contents
def get_all_posts(soup):
    comment_list = []
    all_posts =soup.find_all("div", class_="post-layout")
    j = 0
    
    # goes through all the posts
    while(j != len(all_posts)):
        comment_list.append(get_all_comments(all_posts[j], soup)) 
        j = j + 1
    return comment_list

# given the post it finds all the comments 
def get_all_comments(comment_container, soup):
    list_of_comments = []
    comment = comment_container.find_all("div", class_="comment-text js-comment-text-and-form")
    comment_upvote =  clean_html(str(comment_container.find("div", class_="comment-score")))
    num = 0
 
    # goes through the list of comments
    while(num != len(comment)):
        # passes each comment container
        list_of_comments.append(get_comments(comment[num], soup, comment_upvote))
        num = num + 1
    return list_of_comments

# get complete comments given comment contents
def get_comments(comment, soup, upvote):
    comment_body = comment.find("div", class_="comment-body")
    content = clean_html(str(comment_body.find("span", class_="comment-copy")))
    author = clean_html(str(comment_body.find("a", class_="comment-user")))
    complete_comment = {
        "Content" : content,
        "Author" : author, 
        "Upvote" : upvote
    }
    return complete_comment

# get complete question
def get_question(upvote, comment, soup):
    # whole question content
    question = soup.find_all("div", class_="postcell post-layout--right")
    question_title = str(soup.title.contents).strip("[]") 
    question_contents = question[0].contents
    question_description = clean_html(str(question_contents[1].find_all("p")).strip("[]"))

    question_authors = []
    q_author_content = question_contents[5].find_all("div", class_="user-details")
    i = 0
    
    # goes through author contents
    while(i != len(q_author_content)):
        get_authors(question_contents, 5, i, soup)
        question_authors.append(get_authors(question_contents, 5, i, soup))
        i=i+1
 
    question_data = {
        "Question" : question_title,
        "Description" : question_description,
        "Authors" : question_authors, 
        "Upvote" :  upvote,
        "Comments" : comment
    }
    return question_data
