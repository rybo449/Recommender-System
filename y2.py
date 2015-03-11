from yelpapi import YelpAPI
import pandas as pd
consumer_key = 'PnHvincoddn76xfpm3LhLg'
consumer_secret = 'PGmBEyjY0dKu1jzYkJr2Mxe2SCs'
token = 'Xo8UWIL1CdyTxn-cX-XYbxsAXQOpgfYz'
token_secret = '1J60nMB-wGTsLyNOyGkY9EZfMFM'
yelp_api = YelpAPI(consumer_key,consumer_secret,token,token_secret)
#search_results = yelp_api.search_query()
columns = ['bars','restaurants','laundry','pizza','hospitals','coffee','boutique','clothing','education','arts']
#zip_code = ['10453','10458','10451','10454','10463','10466','10461','11212','11209','11204','11234','11223','11201','11203','11207','11211','11220','11206','10026','10001','10029','10010','10012','10004','10002','10021','10023','10031','11361','11354','11365','11412','11101','11374','11691','11004','11414','11368','10301','10314']
zip_code = ["Central Bronx", "Bronx Park and Fordham", "High Bridge and Morrisania", "Hunts Point and Mott Haven", "Kingsbridge and Riverdale", "Northeast Bronx", "Southeast Bronx", "Central Brooklyn", "Southwest Brooklyn", "Borough Park", "Canarsie and Flatlands", "Southern Brooklyn", "Northwest Brooklyn", "Flatbush", "East New York and New Lots", "Greenpoint", "Sunset Park", "Bushwick and Williamsburg", "Central Harlem", "Chelsea and Clinton", "East Harlem", "Gramercy Park and Murray Hill", "Greenwich Village and Soho", "Lower Manhattan", "Lower East Side", "Upper East Side", "Upper West Side", "Inwood and Washington Heights", "Northeast Queens", "North Queens", "Central Queens", "Jamaica", "Northwest Queens", "West Central Queens", "Rockaways", "Southeast Queens", "Southwest Queens", "West Queens", "Port Richmond", "South Shore", "Stapleton and St. George", "Mid-Island"]
d = {}
for i in columns:
	count = d.setdefault(i, {})
	for j in zip_code:
		count = d[i].setdefault(j, 0)
		try:
			business_results = yelp_api.search_query(term = i,location = j, radius_filter = 1000)
			
			rating = 0
			num = 0
			for k in business_results['businesses']:
				try:
					if k['review_count']>500:
						rating += (k['rating']/float(5))*3 + 2
					else:
						rating += (k['rating']/float(5))*3 + (k['review_count']/float(500))*2
					#print k['name'],k['rating'],k['review_count'],k['location']['postal_code'],k['location']['neighborhoods']
				except:
					continue
			rating = rating/float(20)
			print i,j
			#count = d.setdefault()
			d[i][j] = rating
			#print rating
		except:
			continue
df = pd.DataFrame(data = d, index=zip_code,columns = columns)
print df.head()
df.to_csv('data1.csv')