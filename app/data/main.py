from bs4 import BeautifulSoup
import requests
import re


class Home:

    def __init__(self, *url):
        if url:
            r = requests.get(url[0])
            self.soup = BeautifulSoup(r.text, 'html.parser')
        else:
            url = 'https://goyabu.com/'
            r = requests.get(url)
            self.soup = BeautifulSoup(r.text, 'html.parser')
             
    def home(self):
        self.name = []
        self.epi = []
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
                        if re.findall('\w*[0-9]', tl.text):
                            self.epi.append(re.findall('\w*[0-9]', tl.text)[0])
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
                           if 'jpg' or 'wrbp' in ima['src']:
                               if 'w3' not in ima['src']:
                                  self.images.append(ima['src'])
                           else:
                               self.images.append('https://image.freepik.com/vetores-gratis/conceito-de-erro-404-para-a-pagina-de-destino_52683-10996.jpg')
                for vl in vt:
                    tm = vl.find_all('span', class_="timer")
                    for timer in tm:
                        self.timer.append(timer.text)

            newsA = {}
            c = 0
            for i in self.name:
                anime = {}
                anime['title'] = self.name[c]
                if self.images:
                    if 'http' not in self.images[c]:
                        anime['image'] = 'https://goyabu.com/' + self.images[c]
                    else:
                        anime['image'] = self.images[c]
                anime['url'] = self.link[c]
                if self.epi[c]:
                    anime['episode'] = self.epi[c]
                else:
                    anime['episode'] = 'XX'
                anime['timer'] = self.timer[c]
                c += 1
                newsA[str(c)] = anime.copy()
                anime.clear()

            return newsA

