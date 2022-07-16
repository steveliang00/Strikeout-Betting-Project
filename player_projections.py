import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from bs4 import Comment




def get_daily_projections(player_url):
    

    site_url = "https://www.fangraphs.com/" + player_url
    player_page = requests.get(site_url)

    
    player_soup = BeautifulSoup(player_page.content, "html.parser")

    
    comments = player_soup.find_all(string=lambda text: isinstance(text, Comment))
    player_info = player_soup.find("div", {"id": "root-player-pages"})
    print(player_info)


get_daily_projections("statss.aspx?playerid=14107&position=P")