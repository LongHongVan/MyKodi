# -*- coding: utf-8 -*-
import urllib,urllib2,re,os,json

fptplay    = 'http://fptplay.net/'

def home():
	req = urllib2.Request(fptplay)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.4) Gecko/2008092417 Firefox/4.0.4')
	response = urllib2.urlopen(req, timeout=90)
	link=response.read()
	response.close()
	match=re.compile("<li ><a href=\"(.+?)\" class=\".+?\">(.+?)<\/a><\/li>").findall(link)
	for url,name in match:
		if 'livetv' in url:
			print url
		else:
			print url

def index(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.4) Gecko/2008092417 Firefox/4.0.4')
	response = urllib2.urlopen(req, timeout=90)
	link=response.read()
	response.close()
	match=re.compile("channel=\"(.*?)\" href=\".+?\" data=\"(.*?)\" adsstatus=\".+?\">\s+<img src=\"(.*?)\"").findall(link)
	for name,url,thumbnail in match:
		print name
		print url
		print thumbnail
			

def livetv_link(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.4) Gecko/2008092417 Firefox/4.0.4')
	response = urllib2.urlopen(req, timeout=90)
	link=response.read()
	response.close()
	data = json.loads(link)
	print data['hds_stream_1000']


#index('http://fptplay.net/livetv/')

livetv_link('http://fptplay.net/livetv/api/v0.1/vtc-hd3')