# -*- coding: utf-8 -*-

'''
Copyright (C) 2014                                                     

This program is free software: you can redistribute it and/or modify   
it under the terms of the GNU General Public License as published by   
the Free Software Foundation, either version 3 of the License, or      
(at your option) any later version.                                    

This program is distributed in the hope that it will be useful,        
but WITHOUT ANY WARRANTY; without even the implied warranty of         
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          
GNU General Public License for more details.                           

You should have received a copy of the GNU General Public License      
along with this program. If not, see <http://www.gnu.org/licenses/  
'''                                                                           

import urllib,urllib2,re,os
import xbmc,xbmcplugin,xbmcgui,xbmcaddon

addon      = xbmcaddon.Addon('plugin.video.vietplay')
profile    = xbmc.translatePath(addon.getAddonInfo('profile'))
mysettings = xbmcaddon.Addon(id='plugin.video.vietplay')
home       = mysettings.getAddonInfo('path')
fanart     = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
icon       = xbmc.translatePath(os.path.join(home, 'icon.png'))
logos      = xbmc.translatePath(os.path.join(home, 'logos\\'))
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
			#addDir('[COLOR yellow]' + name + '[/COLOR]',fptplay + url,3,logos + 'fptplay.png')
		else:
			addDir( name ,fptplay + url,1,icon)			
								
def plist(url):	
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.4) Gecko/2008092417 Firefox/4.0.4')
	response = urllib2.urlopen(req, timeout=90)
	link=response.read()
	response.close()
	match=re.compile("<div class=\"col\">\s*<a href=\"([^\"]+)\">\s*<img src=\"([^\"]*)\" alt=\"(.+?)\"").findall(link)
	for url,thumbnail,name in match:	
		addDir(name,fptplay + url,4,thumbnail)
	match=re.compile("<li><a href=\"(.+?)\">(\d+)<\/a><\/li>").findall(link)
	for url,name in match:	
		addDir('[COLOR lime]Trang ' + name + '[/COLOR]',fptplay + url,2,logos + 'fptplay.png')

def dirs(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.4) Gecko/2008092417 Firefox/4.0.4')
	response = urllib2.urlopen(req, timeout=90)
	link=response.read()
	response.close()
	match=re.compile("<h3><a href=\"(.+?)\">(.+?)<\/a><\/h3>").findall(link)
	for url,name in match:	
		addDir(name,fptplay + url,2,icon)

def episodes(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.4) Gecko/2008092417 Firefox/4.0.4')
	response = urllib2.urlopen(req, timeout=90)
	link=response.read()
	response.close()
	title=re.compile('<title>([^\']+)</title>').findall(link)		
	match=re.compile("<li class=\"(.*?)\" data=\"(.*?)\" href=\"\/Video([^\"]*)\" onclick=\".*?\"><a>(.*?)<\/a><\/li>", re.MULTILINE).findall(link)
	for cls,data,url,name in match:
		addDir(('%s   -   %s' % ('Tập ' + name,title[-1])),('%s%s' % (fptplay, data)),5,logos + 'fptplay.png')
						
def index(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.4) Gecko/2008092417 Firefox/4.0.4')
	response = urllib2.urlopen(req, timeout=90)
	link=response.read()
	response.close()
	match=re.compile("channel=\"(.*?)\" href=\"(.+?)\" data=\".+?\">\s+<img src=\"(.*?)\"").findall(link)
	for name,url,thumbnail in match:
		addDir('[COLOR lime]' + name + '[/COLOR]',fptplay + url,5,thumbnail)						

def addLink(name,url,iconimage):
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
    return ok
			
def vlinks(url,name):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.4) Gecko/2008092417 Firefox/4.0.4')
	req.add_header('Referer', fptplay)
	response = urllib2.urlopen(req, timeout=90)
	link=response.read()
	response.close()

	if 'livetv' in url:
		match=re.compile('var video_str = "<video id=\'main-video\' src=\'" \+ "(.+?)"').findall(link)
		for url in match:
			addLink(name,url.replace('1000.stream','2500.stream'),logos + 'fptplay.png')						
	else:
		listitem = xbmcgui.ListItem(path=link)
      	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)

def get_params():
    param=[]
    paramstring=sys.argv[2]
    if len(paramstring)>=2:
        params=sys.argv[2]
        cleanedparams=params.replace('?','')
        if (params[len(params)-1]=='/'):
            params=params[0:len(params)-2]
        pairsofparams=cleanedparams.split('&')
        param={}
        for i in range(len(pairsofparams)):
            splitparams={}
            splitparams=pairsofparams[i].split('=')
            if (len(splitparams))==2:
                param[splitparams[0]]=splitparams[1]
                        
    return param

def addDir(name,url,mode,iconimage):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    isFolder = True
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    if mode == 5:
    	liz.setProperty('IsPlayable', 'true')
    	isFolder = False
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isFolder)
    return ok
                      
params=get_params()
url=None
name=None
mode=None

try:
    url=urllib.unquote_plus(params["url"])
except:
    pass
try:
    name=urllib.unquote_plus(params["name"])
except:
    pass
try:
    mode=int(params["mode"])
except:
    pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
    print ""
    home()
		
elif mode==1:
    print ""+url
    dirs(url)
		
elif mode==2:
    print ""+url
    plist(url)
		
elif mode==3:
    print ""+url
    index(url)
		
elif mode==4:
    print ""+url
    episodes(url)
		
elif mode==5:
   	vlinks(url,name)
			
xbmcplugin.endOfDirectory(int(sys.argv[1]))