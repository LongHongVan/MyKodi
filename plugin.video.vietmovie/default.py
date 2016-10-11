import CommonFunctions as common
import urllib
import urllib2
import os
import xbmcplugin
import xbmcgui
import xbmcaddon
import urlfetch
import re
import random
import time

from BeautifulSoup import BeautifulSoup

__settings__ = xbmcaddon.Addon(id='plugin.audio.vietmusic')
__language__ = __settings__.getLocalizedString
home = __settings__.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
thumbnails = xbmc.translatePath( os.path.join( home, 'thumbnails\\' ) )

__thumbnails = []

def get_thumbnail_url():
  global __thumbnails
  url = ''
  try:
    if len(__thumbnails) == 0:
      content = make_request('https://raw.github.com/onepas/xbmc-addons/master/thumbnails/thumbnails.xml')
      soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)
      __thumbnails = soup.findAll('thumbnail')

    url = random.choice(__thumbnails).text 
  except:
    pass
  
  return url

def _makeCookieHeader(cookie):
  cookieHeader = ""
  for value in cookie.values():
      cookieHeader += "%s=%s; " % (value.key, value.value)
  return cookieHeader

def make_request(url, params = None,  headers=None):
  if headers is None:
    headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
               'Referer' : 'http://www.google.com'}
  try:
    data = None
    if params is not None:
      data = urllib.urlencode(params)
    req = urllib2.Request(url,data,headers)
    f = urllib2.urlopen(req)
    body=f.read()
    return body
  except urllib2.URLError, e:
    print 'We failed to open "%s".' % url
    if hasattr(e, 'reason'):
        print 'We failed to reach a server.'
        print 'Reason: ', e.reason
    if hasattr(e, 'code'):
        print 'We failed with error code - %s.' % e.code


def build_menu():
  content = make_request('http://megabox.vn/')
  soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)
  items = soup.find('div',{'class' : 'navTop'}).findAll('div')

  for item in items:
    if item.parent.a.text != u'Thiết Bị' and item.parent.a.text != u'Videos':
      prefix = item.parent.a.text
      subItems = item.findAll('li')
      for subItem in subItems:
        if subItem.get('style') is None and subItem.a.get('style') is None:
          title = '(' + prefix + ') ' + subItem.a.text
          url = 'http://megabox.vn/' + subItem.a.get('href')
          if 'the-loai' in url:
            add_dir(title, url, 3, get_thumbnail_url())
          else:
            add_dir(title, url, 1, get_thumbnail_url())
  add_dir('Tìm kiếm','', 100, get_thumbnail_url())

def search():
  query = common.getUserInput('Tìm kiếm Phim', '')
  if query is None:
    return
  content = make_request('http://megabox.vn/home/search/index',{'key':query})
  soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)
  items = soup.findAll('div',{'class' : 'picAll'})
  for item in items:
    #espt = item.find('div',{'class':['espT', 'espT MHD']})
    espt = item.find('div',{'class':'espT'})
    mode = 2 #Phim bo
    if espt is None:
      mode = 10 #Phim le
      espt = item.find('div',{'class':'espT MHD'})
    if espt is not None:
      espt = '['+ espt.text.replace(' ','') + ']-'
    else:
      espt = ''
    if len(espt) > 0:
      title = item.h4.text
      href = item.a.get('href')
      itemStr = str(item)
      thumbIndex1 = itemStr.find('data-original')
      lenPrefix = len('data-original="')
      thumbIndex2 = itemStr.find('"',thumbIndex1+lenPrefix)
      thumb = itemStr[thumbIndex1+lenPrefix:thumbIndex2]
      d1 = itemStr.find('<p>')
      d2 = itemStr.find('</p>',d1)
      plot = itemStr[d1+3:d2]
      add_dir(espt + title, href, mode, thumb + '?f.png',plot=plot)

def list_movies(url):
  content = make_request(url)
  soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)
  items = soup.findAll('div',{'class' : 'picAll'})
  for item in items:
    espt = item.find('div',{'class':'espT'})
    mode = 2 #Phim bo
    if espt is None:
      mode = 10 #Phim le
      espt = item.find('div',{'class':'espT MHD'})
    if espt is not None:
      espt = '['+ espt.b.text.replace(' ','') + ']-'
    else:
      mode = 1
      espt = ''
    title = item.find('div',{'class':'infoC'})
    if title is not None:
      title = title.h4.text
    else:
      title = item.find('div',{'class':'loadtxtP'}).a.get('title')
    href = item.a.get('href')
    thumb = item.find('img').get('src')
    itemStr = str(item)
    d1 = itemStr.find('<p>')
    d2 = itemStr.find('</p>',d1)
    plot = itemStr[d1+3:d2]
    if '(0)' not in title:
      add_dir(espt + title, href, mode, thumb + '?f.png',plot=plot)
    
#dung cho link the-loai.html
def list_movies_category(url):
  content = make_request(url)
  soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)
  items = soup.find('div',{'class' : 'contentSHL showsBoxEps categoriesBBox'}).findAll('div',{'class' : 'picAll'})
  for item in items:
    thumb = 'http://megabox.vn/' +  item.img.get('data-original')
    infoC = item.find('div',{'class' : 'infoC'})
    href = infoC.a.get('href')
    title = infoC.find('h4').text
    if '(0)' not in title:
      add_dir(title, href, 1, thumb + '?f.png')
    

def play_movie(url,p=True):
  content = make_request(url)
  soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)
  eps = soup.find('div',{'class' : 'contentBox showsBoxEps'})
  #phim bo
  if not p and eps is not None:
    items = eps.findAll('div',{'class' : 'picAll'})
    for item in items:
      thumb = item.find('img').get('data-original')
      infoC = item.find('div',{'class' : 'infoC'})
      href = 'http://megabox.vn/' + item.a.get('href')
      title = '[' + infoC.find('h4').text + '] ' + item.find('img').get('title')
      add_dir(title, href, 10, thumb + '?f.png')
      
  else:
    m = re.findall('file:\W+http://(.*?)index.m3u8',content,re.DOTALL)
    if (len(m) > 0):
      url = 'http://' + m[0] + 'index.m3u8'
      listitem = xbmcgui.ListItem(path=url)
      xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)
    else:
      bannerSlide = soup.find('div',{'class' : 'bannerSlide'})
      if bannerSlide is not None:
        url = bannerSlide.find('a').get('href')
        content = make_request(url)
        m = re.findall('file:\W+http://(.*?)index.m3u8',content,re.DOTALL)
        if (len(m) > 0):
          url = 'http://' + m[0] + 'index.m3u8'
          listitem = xbmcgui.ListItem(path=url)
          xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)
        else:
          xbmcgui.Dialog().ok("Oops!","Không tìm thấy phim.","Link giả?")
      else:
        xbmcgui.Dialog().ok("Oops!","Không tìm thấy phim.","Link giả?")

      
def add_link(date, name, duration, href, thumb, desc):

    u=sys.argv[0]+"?url="+urllib.quote_plus(href)+"&mode=10"

    liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=thumb)
    liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description, "Duration": duration})
    
    liz.setProperty('IsPlayable', 'true')

    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)


def add_dir(name,url,mode,iconimage,query='',type='f',page=0,plot=''):
  u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&query="+str(query)+"&type="+str(type)+"&page="+str(page)
  ok=True
  liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
  liz.setInfo( type="Video", infoLabels={ "Title": name, "plot":plot } )
  isFolder = True;
  if mode == 10:
    liz.setProperty('IsPlayable', 'true')
    isFolder = False
  
  ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isFolder)
  return ok


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

xbmcplugin.setContent(int(sys.argv[1]), 'movies')

params=get_params()

url=''
name=None
mode=None
query=None
type='f'
page=0

try:
    type=urllib.unquote_plus(params["type"])
except:
    pass
try:
    page=int(urllib.unquote_plus(params["page"]))
except:
    pass
try:
    query=urllib.unquote_plus(params["query"])
except:
    pass
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
print "type: "+str(type)
print "page: "+str(page)
print "query: "+str(query)

if mode==None:
  build_menu()
elif mode == 1:
  list_movies(url)
elif mode == 2:
  play_movie(url,False)
elif mode == 3:
  list_movies_category(url)
elif mode == 10:
  play_movie(url)
elif mode == 100:
  search()

xbmcplugin.endOfDirectory(int(sys.argv[1]))