# -*- coding: utf-8 -*- 

import urllib2,sys,json

reload(sys)
sys.setdefaultencoding('utf-8')


def get_city(city = None):
	if city == None:
		id_url = 'http://61.4.185.48:81/g/'
		id_data = urllib2.urlopen(id_url)
		city_id = id_data.readline().split(';')[1].split('=')[1]
	else:
		id_file = open('city_files.txt','r')
		for line in id_file:
			#line = line.decode('gbk').encode('utf-8')
			if city in line:
				city_id = line.split('=')[1]
	return city_id

def get_weather(city_id):
	str_id = str(city_id)
	city_url = "http://m.weather.com.cn/data/"+str_id+".html"
	result = urllib2.urlopen(city_url)
	weather_data = [i for i in result]
	data = json.loads(weather_data[0])
	v = Weather(data)
	return v

class Weather(object):
	"""docstring for Weather"""
	def __init__(self, data):
		data = data['weatherinfo']
		self.city = data['city']
		self.id = data['cityid']
		self.date = ' '.join([data['date_y'],data['week']])
		t1 = ' '.join([data['temp1'],data['weather1']])
		t2 = ' '.join([data['temp2'],data['weather2']])
		t3 = ' '.join([data['temp3'],data['weather3']])
		t4 = ' '.join([data['temp4'],data['weather4']])
		t5 = ' '.join([data['temp5'],data['weather5']])
		t6 = ' '.join([data['temp6'],data['weather6']])
		self.weather = [t1,t2,t3,t4,t5,t6]
		self.suggest = data['index_d']
		self.original = data
	def report(self):
		days = [u'今天',u'明天',u'后天']
		print self.city,self.date
		print '-'*26
		for i in range(3):
			print days[i] + u':' + self.weather[i]
		print '-'*26
		print self.suggest

city_id = get_city(sys.argv[1].decode('gbk'))
weather_data = get_weather(city_id)
weather_data.report()