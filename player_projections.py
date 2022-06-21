import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup




def get_daily_projections(player_url):
    

    site_url = "https://www.fangraphs.com/" + player_url
    player_page = requests.get(site_url)

    
    player_soup = BeautifulSoup(player_page.content, "html.parser")
    daily_projections = player_soup.findAll('div') 
    print(daily_projections)


get_daily_projections("statss.aspx?playerid=13743&position=P")