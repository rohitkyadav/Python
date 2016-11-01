import requests
from bs4 import BeautifulSoup

def get_data(max_pages):
	
	page = 1
	
	
	while page <= max_pages:
		
		url = "http://delhi-ncr.yellowpages.co.in/Coffee?trc=336&page=" + str(page)
		r = requests.get(url)
		soup = BeautifulSoup(r.content)   #soup holds all the content in the above link
		#print (soup.prettify())
		#soup.find_all('a')  #gives all the links  # a is a HTML tag
		#for link in soup.find_all("a"):
			#print(link)

		#for link in soup.find_all("a"):
			#print(link.get("href"))

		#for link in soup.find_all("a"):
			#print(link.text)

		#for link in soup.find_all("a"):    
			#print(link.text,link.get("href"))


		for link in soup.find_all("a"):
			#if "http" in link.get("href"):
			print("<a href='%s'>%s</a>" %(link.get("href"),link.text))
			

		g_data = soup.find_all("li", {"class":"clearfix"})

		for item in g_data:
			print (item.contents[1].text)
			try:
				print (item.contents[3].find_all('div',{"class":"phone"})[0].text)
			except:
				pass

		page += 1


get_data(2)
