"""
Implement pre-processing and save files: <text></text> part
"""
from bs4 import BeautifulSoup

from nikl.preprocessor import *

def save_info(name, infos):
    """ Save .text info"""
    file = open("../data/info/" + name + "_info.txt", 'a', encoding="utf-8")
    #for info in range(len(infos)):

    #file.write(line) for line in range(len(text))
