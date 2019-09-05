from bs4 import BeautifulSoup
import requests
import re

class Head:

    def __init__(self, url):
        self.url = url
        r = requests.get(self.url)
        self.soup = BeautifulSoup(r.text, 'html.parser')


    def row(self):
        self.name = []
        self.images = []
        
        news = self.soup.find_all('div', class_="main-holder pad-holder col-md-12 top10 nomargin")
        for i in news:
            r = i.find_all('div', class_="left20 right20")
            for e in r:
                romanji = e.find_all('h1')
                for t in romanji:
                    self.name.append(t.text)
            img = i.find_all('div', class_="mleft20 mright20 text-center")
            for im in img:
                aba = im.find_all('img', src=True)
                for src in aba:
                    if 'jpg' in src['src']:
                        self.images.append(src['src'])
        newsA = {}
        c = 0
        for i in self.name:
            anime = {}
            anime['title'] = self.name[c]
            anime['image'] = self.images[c]
            c += 1
            newsA[str(c)] = anime.copy()
            anime.clear()

        return newsA

    def episodios(self):
       from .main import Home
       a = Home(self.url)
       return a.home()
