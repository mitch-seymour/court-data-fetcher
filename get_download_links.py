from bs4 import BeautifulSoup
from openpyxl import load_workbook
import requests
import json

base_url = 'http://www.uscourts.gov'
page_content = requests.get(base_url + '/data-table-numbers/f-2?pt=All&pn=32&t=All&m%5Bvalue%5D%5Bmonth%5D=&y%5Bvalue%5D%5Byear%5D=').text
soup = BeautifulSoup(page_content, 'html.parser')

# get the links to the reports
links = []
for link in soup.find_all('a', text=True):
    href = str(link.get('href'))
	
    if 'statistics/table' in href:
		parts = href.split('/')
		l = len(parts)
		date_str = '/'.join(parts[l-3:l])
		
		try:
			# fetch the download link
			link_page_soup = BeautifulSoup(requests.get(base_url + href).text, 'html.parser')
			download_link = link_page_soup.find('div', {'class': ['file-application-vndms-excel','file-application-vndopenxmlformats-officedocumentspreadsheetmlsheet']}).find('a') 

			links.append({'url': base_url + str(download_link.get('href')), 'date': date_str})
		except AttributeError:
			print("Could not fetch download link for date: " + date_str + ". Url: " + href)

with open('links.json', 'w') as fp:
	json.dump(links, fp)
