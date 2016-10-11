# -*- coding: utf-8 -*-
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

from BeautifulSoup import BeautifulSoup

__settings__ = xbmcaddon.Addon(id='plugin.audio.vietmusic')
__language__ = __settings__.getLocalizedString
home = __settings__.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
thumbnails = xbmc.translatePath( os.path.join( home, 'thumbnails\\' ) )


__video_quality = __settings__.getSetting('video_quality') #values="240p|360p|480p|720p|1080p"
__mp3_quality = __settings__.getSetting('mp3_quality') #values="32K|128K|320K|500K|Lossless"

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

def make_request(url, headers=None):
        if headers is None:
            headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
                       'Referer' : 'http://www.google.com'}
        try:
            req = urllib2.Request(url,headers=headers)
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

def get_chiasenhac(url = None, page = 0):
  if url == '':
    content = make_request('http://chiasenhac.com')
    soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)
    items = soup.find('div',{'id' : 'myslidemenu'}).find('ul').findAll('li')
    for item in items:
      if item.a is not None:
        href = item.a.get('href')
        if href is not None:
          try:
            add_dir(item.a.text, 'http://chiasenhac.com/' + href, 100, get_thumbnail_url(), query, type, 0)
          except:
            pass
    return
  
  if '/mp3/hot/' in url:  
    content = make_request(url)
    soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)
    tables = soup.findAll('tr',{'class' : '2'})
    for table in tables:
      item = table.find('a', {'class':'musictitle'})
      if item is not None:
        href = item.get('href')
        text = item.get('title')
        if text is not None:
          if 'chiasenhac.com' not in href:
            href = 'http://chiasenhac.com/' + href
          quality = table.find('span', {'style':['color: red','color: orange','color: darkblue','color: darkgreen']})
          if quality is not None:
            quality = '[' + quality.text + '] '
          else:
            quality = '';
          try:
            t1 = table.find('div', {'class':'gensmall'}).text
            t2 = t1 + item.text
            t3 = table.find('div', {'class':'musicinfo'}).text
          except:
            t3 = ''
            t2 = ''
            pass

          text = text + ' - [COLOR FF0084EA]' + t3.replace(t2,'') + '[/COLOR]'
          
          add_link('', quality + text, 0, href, get_thumbnail_url(), '')
    return   

  if '/hd/video/' in url:
    content = make_request(url)
    soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)
    tables = soup.findAll('div',{'class' : 'list-l list-1'})
    for table in tables:
      item = table.find('div', {'class':'info'}).find('a')
      href = item.get('href')
      text = item.text
      text_casi = table.find('div', {'class':'info'}).find('p').text

      text = text + ' - [COLOR FF0084EA]' + text_casi + '[/COLOR]'

      if 'playlist.chiasenhac.com' not in href:
        href = 'http://playlist.chiasenhac.com/' + href
      img = table.find('div', {'class':'gensmall'}).find('a').find('img')
      quality = table.find('span', {'style':['color: red','color: orange','color: darkblue','color: darkgreen']})
      if quality is not None:
        quality = '[' + quality.text + '] '
      else:
        quality = '';
      add_link('', quality + text, 0, href, img.get('src'), '')

    url_parts = url.split('/')
    if page == 0:
      page = 2
    url_parts[len(url_parts) -1] = 'new' + str(page) + '.html'
    add_dir(u'Trang tiếp >>', '/'.join(url_parts) , 100, get_thumbnail_url(), query, type, page + 1)

    return  

  if '/mp3/beat-playback/' in url or '/mp3/vietnam/' in url or '/mp3/thuy-nga/' in url or '/mp3/us-uk/' in url or '/mp3/chinese/' in url or '/mp3/korea/' in url or '/mp3/other/' in url:
    content = make_request(url)
    soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)
    if page == 0:
      tables = soup.findAll('div',{'class' : 'list-r list-1'})
      for table in tables:
        item = table.find('div', {'class':'text2'}).find('a')
        href = item.get('href')
        text = item.text
        text_casi = table.find('div', {'class':'text2'}).find('p').text

        text = text + ' - [COLOR FF0084EA]' + text_casi + '[/COLOR]'

        if 'playlist.chiasenhac.com' not in href:
          href = 'http://playlist.chiasenhac.com/' + href
        quality = table.find('div',{'class':'texte2'}).find('span', {'style':['color: red','color: orange','color: darkblue','color: darkgreen']})
        if quality is not None:
          quality = '[' + quality.text + '] '
        else:
          quality = '';
        add_link('', quality + text, 0, href, get_thumbnail_url(), '')
    else:
      tables = soup.findAll('tr',{'class' : '2'})
      for table in tables:
        item = table.find('a', {'class':'musictitle'})
        if item is not None:
          href = item.get('href')
          text = item.parent.text.replace(item.text, item.text + ' - ')
          if 'chiasenhac.com' not in href:
            href = 'http://chiasenhac.com/' + href
          quality = table.find('span', {'style':['color: red','color: orange','color: darkblue','color: darkgreen']})
          if quality is not None:
            quality = '[' + quality.text + '] '
          else:
            quality = '';
          tt =text.split('-')
          if len(tt) == 2:
            text = tt[0] + ' - [COLOR FF0084EA]' + tt[1] + '[/COLOR]'
          add_link('', quality + text, 0, href, get_thumbnail_url(), '')
    
    url_parts = url.split('/')
    if page == 0:
      page = 1
    url_parts[len(url_parts) -1] = 'new' + str(page) + '.html'
    add_dir(u'Trang tiếp >>', '/'.join(url_parts) , 100, get_thumbnail_url(), query, type, page + 1)
    
    return
  return

def get_chiasenhac_album(url = None, page = 0):
  
  #content = make_request(url)
  #soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES) 
  #album_url = 'http://chiasenhac.com/' + soup.find('th',{'class' : 'catLeft'}).find('a').get('href')
  album_url = url

  content = make_request(album_url)
  soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)

  albums_thumbs = {}
  albums = soup.findAll('span',{'class' : 'genmed'})
  for album in albums:
    a = album.find('a').get('href')
    b = album.find('img').get('src')
    albums_thumbs[a] = b

  albums = soup.findAll('span',{'class' : 'gen'})
  for album in albums:
    href = album.find('a', {'class' : 'musictitle'})
    title = href.get('title')
    link = href.get('href')
    thumb = None
    if link in albums_thumbs:
      thumb = albums_thumbs[link]
    
    quality = href.parent.find('span', {'style':['color: red','color: orange','color: darkblue','color: darkgreen']})
    if quality is not None:
      quality = '[' + quality.text + '] '
    else:
      quality = '';
    add_dir(quality + title, link, 102, thumb, query, type, 0)
  
  url_parts = url.split('/')
  if page == 0:
    page = 2
  if page < 3:
    url_parts[len(url_parts) -1] = 'album' + str(page) + '.html'
    add_dir(u'Trang tiếp >>', '/'.join(url_parts) , 101, get_thumbnail_url(), query, type, page + 1)

  return   

def get_chiasenhac_album_songs(url = None):
  content = make_request(url)
  soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)

  albums = soup.find('div',{'id':'playlist'}).findAll('span',{'class' : 'gen'})
  for album in albums:
    a = album.findAll('a')
    if (len(a) == 3):
      href = 'http://chiasenhac.com/' + a[1].get('href')
      text = album.text
      tt =text.split('-')
      if len(tt) == 2:
        text = tt[0] + ' - [COLOR FF0084EA]' + tt[1] + '[/COLOR]'

      add_link('', text, 0, href, get_thumbnail_url(), '')
      
  return 

def get_categories():
  add_dir('Xếp hạng', 'mp3/hot/', 1,  get_thumbnail_url(), '', type, 0)
  add_dir('Video Clip','hd/video/', 1,  get_thumbnail_url(), '', type, 0)
  add_dir('Playback','mp3/beat-playback/', 1,  get_thumbnail_url(), '', type, 0)
  add_dir('Việt Nam','mp3/vietnam/', 1,  get_thumbnail_url(), '', type, 0)
  add_dir('Thuý Nga','mp3/thuy-nga/', 1,  get_thumbnail_url(), '', type, 0)
  add_dir('Âu, Mỹ','mp3/us-uk/', 1,  get_thumbnail_url(), '', type, 0)
  add_dir('Nhạc Hoa','mp3/chinese/', 1,  get_thumbnail_url(), '', type, 0)
  add_dir('Nhạc Hàn','mp3/korea/', 1,  get_thumbnail_url(), '', type, 0)
  add_dir('Nước Khác','mp3/other/', 1,  get_thumbnail_url(), '', type, 0)
  add_dir('Tìm kiếm theo tên bài hát','', 210, get_thumbnail_url(), '', type, 0)
  add_dir('Tìm kiếm theo tên ca sỹ/ban nhạc','', 213, get_thumbnail_url(), '', type, 0)
  add_dir('Tìm kiếm Video','', 212, get_thumbnail_url(), '', type, 0)
  add_dir('Tìm kiếm theo tên album','', 211, get_thumbnail_url(), '', type, 0)
  add_dir('Add-on settings', '', 99, get_thumbnail_url(), '', type, 0)
    

def get_sub_categories(url, mode):
  content = make_request('http://chiasenhac.com')
  soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)
  items = soup.find('div',{'id' : 'myslidemenu'}).find('ul').findAll('li')
  for item in items:
    href = item.a.get('href')
    if href is not None:
      try:
        if href.startswith(url) and len(href) > len(url):
          prefix = ''
          if url != 'mp3/hot/' and url !='hd/video/':
            prefix = 'Songs: '
          add_dir(prefix + item.a.text, 'http://chiasenhac.com/' + href, 100, get_thumbnail_url(), query, type, 0)
      except:
        pass
  for item in items:
    href = item.a.get('href')
    if href is not None:
      try:
        if url != 'mp3/hot/' and url !='hd/video/' and href.startswith(url) and len(href) > len(url):
          add_dir('Albums: ' + item.a.text, 'http://chiasenhac.com/' + href + 'album.html', 101, get_thumbnail_url(), query, type, 0)
      except:
        pass
  add_dir('Tìm kiếm theo tên bài hát','', 210, get_thumbnail_url(), '', type, 0)
  add_dir('Tìm kiếm theo tên ca sỹ/ban nhạc','', 213, get_thumbnail_url(), '', type, 0)
  add_dir('Tìm kiếm Video','', 212, get_thumbnail_url(), '', type, 0)
  add_dir('Tìm kiếm theo tên album','', 211, get_thumbnail_url(), '', type, 0)
  return
 
def show_search_recent(mode):
  add_dir('Tìm kiếm','', mode - 200, get_thumbnail_url(), '', type, 0)
  saved_search = __settings__.getSetting('saved_search_' + str(mode - 200))
  if saved_search is not None:
    items=saved_search.split('~')
    for i in range(len(items)):
      if len(items[i]) > 0:
        add_dir(items[i],'', mode - 200, get_thumbnail_url(), items[i], type, 0)


def search(query = '', page = 0, mode = 10, cat = 'music'):
  if len(query)==0:
    query = common.getUserInput('Search', '')
    if query is None:
      return
    saved = __settings__.getSetting('saved_search_' + str(mode))
    if saved is None:
      saved = query + '~'
      __settings__.setSetting('saved_search_' + str(mode),saved)
    else:
      if query + '~' in saved:
        saved = saved.replace(query + '~','')
      saved = query + '~' + saved
      __settings__.setSetting('saved_search_' + str(mode),saved)

  if page == 0:
    page = 1

  url = 'http://search.chiasenhac.com/search.php?s=' + urllib.quote(query) + '&page=' + str(page) + '&cat=' + cat
  if 'artist' in cat:
    url = 'http://search.chiasenhac.com/search.php?s=' + urllib.quote(query) + '&page=' + str(page) + '&cat=music&mode=' + cat
  
  content = make_request(url)
  soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)
  items = soup.find('table',{'class':'tbtable'}).findAll('tr')
  for ii in items:
    item = ii.find('div',{'class':'tenbh'})
    if item is not None:
      a = item.find('a')
      p = item.findAll('p')[1]
      if a is not None:
        href = a.get('href')
        if 'chiasenhac.com' not in href:
          href = 'http://chiasenhac.com/' + href   
        quality = ii.find('span',{'class':'gen'}).find('span', {'style':['color: red','color: orange','color: darkblue','color: darkgreen']})
        if quality is not None:
          quality = '[' + quality.text + '] '
        else:
          quality = '';
        add_link('', quality + a.text + ' - [COLOR FF0084EA]' + p.text + '[/COLOR]', 0, href, get_thumbnail_url(), '')

  add_dir(u'Trang tiếp >>', '', mode, get_thumbnail_url(), query, type, page + 1)
  return

def search_albums(start, query, page):
  #http://search.chiasenhac.com/search.php?s=bai+hat&mode=album&page=2&start=221
  mode = 11
  if len(query) == 0:
    query = common.getUserInput('Search', '')
    if query is None:
      return
    saved = __settings__.getSetting('saved_search_' + str(mode))
    if saved is None:
      saved = query + '~'
      __settings__.setSetting('saved_search_' + str(mode),saved)
    else:
      if query + '~' in saved:
        saved = saved.replace(query + '~','')
      saved = query + '~' + saved
      __settings__.setSetting('saved_search_' + str(mode),saved)
  if page == 0:
    page = 1
  url = 'http://search.chiasenhac.com/search.php?mode=album&s=' + urllib.quote_plus(query) + '&page=' + str(page) + '&start=' + start
  content = make_request(url)
  soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)
  thumbs = soup.find('table',{'class' : 'tbtable'}).findAll('span',{'class' : 'genmed'})
  albums_thumbs = {}
  for thumb in thumbs:
    img = thumb.find('img')
    href = thumb.find('a')
    if (img is not None) and (href is not None):
      a = img.get('src');
      b = href.get('href')
      albums_thumbs[b] = a

  albums = soup.find('table',{'class' : 'tbtable'}).findAll('span',{'class' : 'gen'})
  for album in albums:
    href = album.find('a')
    if href is not None:
      link = href.get('href')
      title = album.text.replace(u'(Xem chi tiết...)','').replace('Lossless',' - Lossless').replace('320kbps',' - 320kbps').replace('192kbps',' - 192kbps').replace('128kbps',' - 128kbps')
      thumb = None
      if link in albums_thumbs:
        thumb = albums_thumbs[link]
      
      add_dir(title, link, 102, thumb, query, type, 0)
  xt = soup.find('a',{'class' : 'xt'})
  if xt is not None:
    href = xt.get('href')
    parts = href.split('=')
    start = parts[len(parts) - 1]
    add_dir(u'Trang tiếp >>', start, mode, get_thumbnail_url(), query, type, page + 1)
  return

def resolve_url(url):
  try:
    mediaUrl=extract_link_with_quality(__video_quality, __mp3_quality, url)
    listitem = xbmcgui.ListItem(path=mediaUrl)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)
  except:
    pass
  return


def extract_link_with_quality(video_quality, mp3_quality, url):
  #video="240p|360p|480p|720p|1080p"
  #mp3="32k|128k|320k|500k|Lossless"
  if mp3_quality == '500k':
      mp3_quality = 'm4a'
  if mp3_quality == 'Lossless':
      mp3_quality = 'flac'

  mp3_q = '128'
  if mp3_quality == 'flac':
      mp3_q = 'flac'
  if mp3_quality == 'm4a':
      mp3_q = 'm4a'
  if mp3_quality == '320k':
      mp3_q = '320'   

  video_q = '128'
  if video_quality == '1080p':
      video_q = 'flac'
  if video_quality == '720p':
      video_q = 'm4a'
  if video_quality == '480p':
      video_q = '320'

  media_link = ''
  content = make_request(url)
  
  soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)
  items = soup.find('noscript').find('object').findAll('param')
  for item in items:
      name = item.get('name')
      if name is not None and name == 'FlashVars':
          value = urllib.unquote(item.get('value'))
          pairsofparams=value.split('&')
          for i in range(len(pairsofparams)):
              splitparams=pairsofparams[i].split('=')
              if splitparams[0] == 'audioUrl' or splitparams[0] == 'file':
                  media_link = splitparams[1]
  
  #images/32k.png -> 128
  #images/128k_l.png -> 128
  #images/320k.png -> 320
  #images/m4a.png -> m4a

  #images/240p.png -> 32
  #images/360p_l.png -> 128
  #images/480p.png -> 320
  #images/720p.png -> m4a
  #images/1080p.png -> flac

  items = soup.find('div',{'class' : 'gen'}).findAll('img')
  quality_availables  = ''
  for item in items:
    quality_availables += item.get('src') + ','

  if video_quality not in quality_availables:
    video_quality = '720p'
    video_q = 'm4a'
    if video_quality not in quality_availables:
      video_quality = '480p'
      video_q = '320'
      if video_quality not in quality_availables:
        video_q = '128'

  mp3_quality_save = mp3_quality

  if mp3_quality not in quality_availables:
    mp3_quality = 'm4a'
    mp3_q = 'm4a'
    if mp3_quality not in quality_availables:
      mp3_quality = '320k'
      mp3_q = '320'
      if mp3_quality not in quality_availables:
        mp3_q = '128'

  if (mp3_quality_save == 'flac') and ('m4a' in quality_availables):
    mp3_q = 'flac'

  parts = media_link.split('/')

  if media_link.endswith('mp4.csn'):
      parts[len(parts) - 2] = video_q
  if media_link.endswith('mp3.csn'):
      parts[len(parts) - 2] = mp3_q
      if mp3_q == 'flac':
          parts[len(parts) - 1] = parts[len(parts) - 1].replace('.mp3.csn','.flac.csn')
      if mp3_q == 'm4a':
          parts[len(parts) - 1] = parts[len(parts) - 1].replace('.mp3.csn','.m4a.csn')

  
  return '/'.join(parts)

def add_link(date, name, duration, href, thumb, desc):

    description = date+'\n\n'+desc
    
    #u=extract_link_with_quality(__video_quality, __mp3_quality, href)
    u=sys.argv[0]+"?url="+urllib.quote_plus(href)+"&mode=4"

    liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=thumb)
    liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description, "Duration": duration})
    
    liz.setProperty('IsPlayable', 'true')

    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)


def add_dir(name,url,mode,iconimage,query='',type='f',page=0):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&query="+str(query)+"&type="+str(type)+"&page="+str(page)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
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
query=''
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


if mode==None:
  try: 
    get_categories()
  except:
    pass
elif mode==1:
  try:
    get_sub_categories(url,mode)
  except:
    pass
elif mode==4:
  try:
    resolve_url(url)
  except:
    pass
elif mode==210:
  try:
    show_search_recent(mode)
  except:
    pass
elif mode==10:
  try:
    search(query,page,mode,'music')
  except:
    pass
elif mode==213:
  try:
    show_search_recent(mode)
  except:
    pass
elif mode==13:
  try:
    search(query,page,mode,'artist')
  except:
    pass
elif mode==212:
  try:
    show_search_recent(mode)
  except:
    pass
elif mode==12:
  try:
    search(query,page,mode,'video')
  except:
    pass
elif mode==211:
  try:
    show_search_recent(mode)
  except:
    pass
elif mode==11:
  try:
    search_albums(url,query,page)
  except:
    pass
elif mode==100:
  try:
    get_chiasenhac(url,page)
  except:
    pass
elif mode==101:
  try:
    get_chiasenhac_album(url, page)
  except:
    pass
elif mode==102:
  try:
    get_chiasenhac_album_songs(url)
  except:
    pass
elif mode==99:
   __settings__.openSettings()
   
xbmcplugin.endOfDirectory(int(sys.argv[1]))