from lxml import html
import requests
import csv
import json

businesses, numbers, websites = [], [], []

apikey = '&key=noapikeyforyou'

for x in range(1,27):
	page = requests.get('http://us-business.info/directory/cumming-ga/part' + str(x))
	tree = html.fromstring(page.content)
	businesses += tree.xpath('//div[@class="fn org"]/text()')
	numbers += tree.xpath('//div[@class="tel"]/text()')

for businessname in businesses:

	print('iteration')

	response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=34.2073,-84.1402&radius=48280.3&keyword=' + businessname + apikey)
	data = response.json()
	results = (data['results'])
	try:
		placeID = results[0]['place_id']

		details = requests.get('https://maps.googleapis.com/maps/api/place/details/json?placeid=' + placeID + apikey)
		detailsJSON = details.json()

		try:
			website =  detailsJSON['result']['website']
			print(website)
			websites.append(website)
		except:
			websites.append('N/A Error 02')
			pass
	except:
		websites.append('N/A Error 01')
		pass

rows = zip(businesses,numbers,websites)

with open('directory.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in rows:
    	writer.writerow(row)

f.close()