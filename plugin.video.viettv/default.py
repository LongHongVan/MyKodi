import xbmc, xbmcgui, xbmcaddon, xbmcplugin, re
import urllib, urllib2
import re, string, json
import threading
import os
import base64
import urlparse
import xbmcplugin
import random

from BeautifulSoup import BeautifulSoup

__settings__ = xbmcaddon.Addon(id='plugin.video.viettv')
__video_quality = __settings__.getSetting('video_quality') #values="500|1000|2500"
__video_streaming = __settings__.getSetting('video_streaming') #values="f4m|m3u8"

__thumbnails = []

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

mode =None
play=False

paramstring=sys.argv[2]

print paramstring
name=''
proxy_string=None
proxy_use_chunks=True
auth_string=''
streamtype='HDS'
setResolved=False

sourceUrl='http://fptplay.net/livetv/'

if paramstring:
    paramstring="".join(paramstring[1:])
    params=urlparse.parse_qs(paramstring)
    url = params['url'][0]
    try:
        name = params['name'][0]
    except:pass

    try:
        proxy_string = params['proxy'][0]
    except:pass
    try:
        auth_string = params['auth'][0]
    except:pass
    print 'auth_string',auth_string
    try:
        streamtype = params['streamtype'][0]
    except:pass
    print 'streamtype',streamtype

    try:
        proxy_use_chunks_temp = params['proxy_for_chunks'][0]
        import json
        proxy_use_chunks=json.loads(proxy_use_chunks_temp)
    except:pass
    
    simpleDownloader=False
    try:
        simpleDownloader_temp = params['simpledownloader'][0]
        import json
        simpleDownloader=json.loads(simpleDownloader_temp)
    except:pass
	
	
    mode='play'

    try:    
        mode =  params['mode'][0]
    except: pass
    maxbitrate=0
    try:
        maxbitrate =  int(params['maxbitrate'][0])
    except: pass
    play=True

    try:
        setResolved = params['setresolved'][0]
        import json
        setResolved=json.loads(setResolved)
    except:setResolved=False
    
def playF4mLink(url,name,proxy=None,use_proxy_for_chunks=False,auth_string=None,streamtype='HDS',setResolved=False):
    from F4mProxy import f4mProxyHelper
    player=f4mProxyHelper()
    if setResolved:
        urltoplay,item=player.playF4mLink(url, name, proxy, use_proxy_for_chunks,maxbitrate,simpleDownloader,auth_string,streamtype,setResolved)
        item.setProperty("IsPlayable", "true")
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)

    else:
        xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=False)
        player.playF4mLink(url, name, proxy, use_proxy_for_chunks,maxbitrate,simpleDownloader,auth_string,streamtype,setResolved)
    
    return   
    
if mode ==None:
    
    req = urllib2.Request(sourceUrl)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.4) Gecko/2008092417 Firefox/4.0.4')
    response = urllib2.urlopen(req, timeout=90)
    link=response.read()
    response.close()
    match=re.compile("channel=\"(.*?)\" href=\".+?\" data=\"(.*?)\" adsstatus=\".+?\">\s+<img src=\"(.*?)\"").findall(link)
    for name,url,thumbnail in match:
        file_link = 'http://fptplay.net' + url
        imgurl = thumbnail
        maxbitrate = 2500
        proxy = ''
        usechunks = True
        title = name.replace('&#39;','\'')
        liz=xbmcgui.ListItem(title,iconImage=imgurl, thumbnailImage=imgurl)
        liz.setInfo( type="Video", infoLabels={ "Title": title} )
        #liz.setProperty("IsPlayable","true")
        u = sys.argv[0] + "?" + urllib.urlencode({'url': file_link,'mode':'play','name':title,'maxbitrate':maxbitrate,'proxy':proxy,'proxy_for_chunks':usechunks}) 
        
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False, )

    liz=xbmcgui.ListItem("Add-on settings",iconImage="", thumbnailImage="")
    liz.setInfo( type="Video", infoLabels={ "Title": "Add-on settings"} )
    u = sys.argv[0] + "?" + urllib.urlencode({'url':'#','mode':'settings','name':'Add-on settings','maxbitrate':0,'proxy':'','proxy_for_chunks':False}) 
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False, )

elif mode == "play":
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.4) Gecko/2008092417 Firefox/4.0.4')
    response = urllib2.urlopen(req, timeout=90)
    link=response.read()
    response.close()
    data = json.loads(link)
    
    streamUrl = data['hds_stream_' + __video_quality]
    
    if '.m3u8' in streamUrl:
        listitem = xbmcgui.ListItem( label = str(name), iconImage = "DefaultVideo.png", thumbnailImage = xbmc.getInfoImage( "ListItem.Thumb" ), path=streamUrl )
        xbmc.Player().play( streamUrl,listitem)
    else:
        if __video_streaming == 'm3u8':
            streamUrl = data['hls_stream']
            streamUrl = streamUrl.replace('_1000','_' + __video_quality)
            #kiem tra xem co bitrate nay khong?
            ok = False
            try:
                pDialog = xbmcgui.DialogProgressBG()
                pDialog.create('', 'Detecting bitrate...')
                req = urllib2.Request(streamUrl)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.4) Gecko/2008092417 Firefox/4.0.4')
                response = urllib2.urlopen(req, timeout=5)
                link=response.read()
                response.close()
                pDialog.close()
                pDialog.update(100, message='Bitrate is ' + __video_quality)
                ok = True
            except:
                pDialog.update(100, message='Bitrate is 1000')
                pDialog.close()
                pass
            if not ok:
                streamUrl = data['hls_stream']

            listitem = xbmcgui.ListItem( label = str(name), iconImage = "DefaultVideo.png", thumbnailImage = xbmc.getInfoImage( "ListItem.Thumb" ), path=streamUrl )
            xbmc.Player().play( streamUrl,listitem)
        else:
            streamUrl = streamUrl + '|Referer=http://play.fpt.vn/static/mediaplayer/FPlayer.swf'
            playF4mLink(streamUrl,name, proxy_string, proxy_use_chunks,auth_string,streamtype,setResolved)
    
elif mode == "settings":
    __settings__.openSettings()

if not play:
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=False)
    
 