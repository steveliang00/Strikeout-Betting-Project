import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup


date = "2022-06-20" #yyyy-mm-dd format

URL = ("https://www.fangraphs.com/leaders.aspx?pos=all&stats=pit&lg=all&qual=0&type=8&season=2022&month=0&season1=2022&ind=0&team=0&rost=0&age=0&filter=&players=p"
+date+
"&page=1_50")

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

table = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="LeaderBoard1_dg1_ctl00") #Find table
rows = table.findAll('tr') #Get rows for table

player_links = list()
for row in rows:
    values = row.findAll('td', class_='grid_line_regular') #Iterate through fields in each row
    if values != []:
        name = values[1] #get name of pitcher
        team = values[2] #get team of pitcher
        ip = values[8] #get innings pitched to validate for sample size
        if float(ip.text) >= 18:
            print(name.text)
            player_links.append(name.find('a', href=True)['href'])

print(player_links)


        




    
