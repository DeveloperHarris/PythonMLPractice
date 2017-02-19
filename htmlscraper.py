from lxml import html
import requests
import csv

businesses, numbers = [], []

for x in range(1,27):
	page = requests.get('http://us-business.info/directory/cumming-ga/part' + str(x))
	tree = html.fromstring(page.content)
	businesses += tree.xpath('//div[@class="fn org"]/text()')
	numbers += tree.xpath('//div[@class="tel"]/text()')

rows = zip(businesses,numbers)

with open('directory.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in rows:
    	writer.writerow(row)

