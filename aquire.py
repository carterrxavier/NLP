from requests import get
from bs4 import BeautifulSoup
import os


def get_articles(website_list):
    article_list = []
    
    for website in website_list:
        file_name = 'articles/' + website.replace('/','_')  + 'article.txt'
        file_name2 = 'articles/' + website.replace('/','_')  + 'title.txt'
        
        
        if os.path.isfile(file_name):
            with open(file_name) as f:
                article = f.read()
                
                
        if os.path.isfile(file_name2):
            with open(file_name2) as f:
                title = f.read()
                dictionary = {'title': title, 'content': article}
                article_list.append(dictionary)
        
    
                
                
        else:
            # otherwise go fetch the data
            url = website
            headers = {'User-Agent': 'Codeup Data Science'}
            response = get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find('h1', class_ = 'jupiterx-post-title')
            article = soup.find('div', class_='jupiterx-post-content')
            dictionary = {'title': title.text, 'content': article.text}
            
            article_list.append(dictionary)
            with open(file_name, 'w') as f:
                f.write(article.text)
            with open(file_name2, 'w') as f:
                f.write(title.text)
            
            
        
    return article_list


    
    