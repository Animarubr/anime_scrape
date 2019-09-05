from bs4 import BeautifulSoup
import requests
import re

class Search:

    def __init__(self, _id):
        url = 'https://goyabu.com/?s=' + _id
        print(url)
        r = requests.get(url)
        self.soup = BeautifulSoup(r.text, 'html.parser')
    
    def home(self):
        self.name = []
        self.link = []
        self.images = []
        self.timer = []
        news = self.soup.find_all('div', class_="loop-content phpvibe-video-list miau")
        for i in news:
            card = i.find_all('div', class_="video")
            for n in card:
                data = n.find_all('div', class_="video-data")
                for t in data:
                    title = t.find_all('h4', class_="video-title")
                    for tl in title:
                        self.name.append(tl.text)
                    for tl in title:
                        a = tl.find_all('a', href=True)
                        for lin in a:
                            self.link.append(lin['href'])
            for thumb in card:
                vt = thumb.find_all('div', class_="video-thumb")
                for span in vt:
                    s = span.find_all('span', class_="clip")
                    for im in s:
                        img = im.find_all('img', src=True)
                        for ima in img:
                           if 'jpg' in ima['src']:
                               self.images.append(ima['src'])
                for vl in vt:
                    tm = vl.find_all('span', class_="timer")
                    for timer in tm:
                        self.timer.append(timer.text)

            news = {}
            c = 0
            for i in self.name:
                anime = {}
                anime['title'] = self.name[c]
                anime['image'] = 'https://goyabu.com/' + self.images[c]
                anime['url'] = self.link[c]
                anime['timer'] = self.timer[c]
                c += 1
                news[str(c)] = anime.copy()
                anime.clear()
            return news
