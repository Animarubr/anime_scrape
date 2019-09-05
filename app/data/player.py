from bs4 import BeautifulSoup
import requests
import re


def video(_id):
	sourses = []
	s = []
	url = _id
	sourse = requests.get(url)
	soup = BeautifulSoup(sourse.text, 'html.parser')
	a = soup.find_all('div', class_='row block page p-video')
	regex = r"\bfile: \"(.*?)\""
	for i in a:
		javaS = i.find_all('script')
		for el in javaS:
			matches = re.findall(regex, el.text)
			if matches != []:
				sourses.append(matches)


	dicionario = {}
	if sourses != []:
		for i in sourses:
			if len(i) == 3:
				dicionario['fhd'] = i[0]
				dicionario['hd'] = i[1]
				dicionario['sd'] = i[2]
			elif len(i) == 2:
				dicionario['hd'] = i[0]
				dicionario['sd'] = i[1]
			else:
				
				dicionario['sd'] = i[0]

	return dicionario

