# https://www.rithmschool.com/blog

import requests
from csv import writer
from bs4 import BeautifulSoup

response = requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup(response.text,"html.parser")
articles = soup.find_all("article")

with open("blof_data.csv","w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["Title","Link","Date and Time"])


    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text()
        url = (a_tag["href"])
        date = article.find("time")["datetime"]
        csv_writer.writerow([title,url,date])

    
