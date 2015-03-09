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
zip_code = [10001, 10002, 10003, 10004, 10005, 10006, 10007, 10009, 10010, 10011, 10012, 10013, 10014, 10016, 10017, 10018, 10019, 10020, 10021, 10022, 10023, 10024, 10025, 10026, 10027, 10028, 10029, 10030, 10031, 10032, 10033, 10034, 10035, 10036, 10037, 10038, 10039, 10040, 10044, 10065, 10069, 10075, 10103, 10110, 10111, 10112, 10115, 10119, 10128, 10152, 10153, 10154, 10162, 10165, 10167, 10168, 10169, 10170, 10171, 10172, 10173, 10174, 10177, 10199, 10271, 10278, 10279, 10280, 10282, 10301, 10302, 10303, 10304, 10305, 10306, 10307, 10308, 10309, 10310, 10311, 10312, 10314, 10451, 10452, 10453, 10454, 10455, 10456, 10457, 10458, 10459, 10460, 10461, 10462, 10463, 10464, 10465, 10466, 10467, 10468, 10469, 10470, 10471, 10472, 10473, 10474, 10475, 11004, 11005, 11101, 11102, 11103, 11104, 11105, 11106, 11109, 11201, 11203, 11204, 11205, 11206, 11207, 11208, 11209, 11210, 11211, 11212, 11213, 11214, 11215, 11216, 11217, 11218, 11219, 11220, 11221, 11222, 11223, 11224, 11225, 11226, 11228, 11229, 11230, 11231, 11232, 11233, 11234, 11235, 11236, 11237, 11238, 11239, 11351, 11354, 11355, 11356, 11357, 11358, 11359, 11360, 11361, 11362, 11363, 11364, 11365, 11366, 11367, 11368, 11369, 11370, 11371, 11372, 11373, 11374, 11375, 11377, 11378, 11379, 11385, 11411, 11412, 11413, 11414, 11415, 11416, 11417, 11418, 11419, 11420, 11421, 11422, 11423, 11424, 11425, 11426, 11427, 11428, 11429, 11430, 11432, 11433, 11434, 11435, 11436, 11451, 11691, 11692, 11693, 11694, 11697]
d = {}
for i in columns:
	count = d.setdefault(i, {})
	for j in zip_code:
		count = d[i].setdefault(j, 0)
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
df = pd.DataFrame(data = d, index=zip_code,columns = columns)
print df.head()
df.to_csv('data.csv')