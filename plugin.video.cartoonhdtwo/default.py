import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os

import json


ADDON = xbmcaddon.Addon(id='plugin.video.cartoonhdtwo')

cartoon=os.path.join(ADDON.getAddonInfo('path'),'cartoon')


def CATEGORIES():
    addDir('Movie & Tv','Movie',2,'','','')
    addDir('Animation','Animation',2,'','','')
    addDir('Search','url',3,'','','')


def MAIN(url):
    xunity='http://gearscenter.com/cartoon_control/gapi-ios/index.php?op_select=catalog&os=ios&param_10=AIzaSyBsxsynyeeRczZJbxE8tZjnWl_3ALYmODs&param_7=1.0.0&param_8=com.appmovies.gears&type_film=%s' % url
    response=OPEN_URL(xunity)
    
    link=json.loads(response)

    data=link['categories']

    for field in data:
        name= field['catalog_name'].encode("utf-8")
        iconimage= field['catalog_icon'].encode("utf-8")
        action=field['catalog_id'].encode("utf-8")
    
            
        if  ADDON.getSetting('parental')=='true':
            if not '14+' in name:    
                addDir(name.strip(),action,1,iconimage,'',iconimage)
        else:
            addDir(name.strip(),action,1,iconimage,'',iconimage)            
    setView('movies', 'default') 
       
       
                                                                      
def GetContent(url):
   
        new_url='http://gearscenter.com/cartoon_control/gapi-ios/index.php?id_select=%s&op_select=films&os=ios&param_10=AIzaSyBsxsynyeeRczZJbxE8tZjnWl_3ALYmODs&param_7=1.0.0&param_8=com.appmovies.gears'% url
        response=OPEN_URL(new_url)
        link=json.loads(response)

        data=link['films']
        amount=re.compile('"film_link":"(.+?)"').findall(response)
        if len(amount)==1:
            for field in data:
                name= field['film_name'].encode("utf-8")
                url=field['film_link'].encode("utf-8")
                iconimage= field['film_icon'].encode("utf-8")
                test=url.split('https://')
                for p in test:
                    print p
                    try:
                        name =re.compile('#(.+?)#').findall(p)[0]+'p'
                        URL= 'https://'+p.split('#')[0]
                        addDir(name,URL,200,iconimage,'',iconimage)
                    except:pass    
            setView('movies', 'movies')
        else:
            for field in data:
                name= field['film_name'].encode("utf-8")
                iconimage= field['film_icon'].encode("utf-8")
                url=field['film_link'].encode("utf-8")
                addDir(name.strip(),url,200,iconimage,'',iconimage)
                setView('movies', 'movies') 
        xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)
    

def Search(url):
        search_entered = ''
        keyboard = xbmc.Keyboard(search_entered, 'Search Cartoon HD 2...XUNITYTALK.COM')
        keyboard.doModal()
        if keyboard.isConfirmed():
            search_entered = keyboard.getText() 
            if search_entered == None:
                return 
        xunity='http://gearscenter.com/cartoon_control/gapi-ios/index.php?op_select=catalog&os=ios&param_10=AIzaSyBsxsynyeeRczZJbxE8tZjnWl_3ALYmODs&param_7=1.0.0&param_8=com.appmovies.gears&type_film=Movie' 
        response=OPEN_URL(xunity)
        
        link=json.loads(response)

        data=link['categories']

        for field in data:
            name= field['catalog_name'].encode("utf-8").strip()
            iconimage= field['catalog_icon'].encode("utf-8")
            action=field['catalog_id'].encode("utf-8")
 
            if  search_entered.lower() in name.lower():
  
                    addDir(name.strip(),action,1,iconimage,'',iconimage)
         
 
def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link
    
    
    
def PLAY_STREAM(name,url,iconimage):
    print url
    NAME=[]
    URL=[]
    if url.endswith('#'):
        test=url.split('https://')
        for p in test:
            try:
                name =re.compile('#(.+?)#').findall(p)[0]+'p'
                _URL_= 'https://'+p.split('#')[0]
                NAME.append(name)
                URL.append(_URL_)
            except:pass   
        url= URL[xbmcgui.Dialog().select('Please Select Resolution', NAME)]    
        
    liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
    liz.setInfo(type='Video', infoLabels={'Title':name})
    liz.setProperty("IsPlayable","true")
    liz.setPath(url)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)




    
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

def addDir(name,url,mode,iconimage,description,fanart):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)+"&fanart="+urllib.quote_plus(fanart)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description })
        liz.setProperty("Fanart_Image", fanart)
        menu = []
        if mode ==200:
            liz.setProperty("IsPlayable","true")
            
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        else:

            xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        
        
 
        
def setView(content, viewType):
        if content:
                xbmcplugin.setContent(int(sys.argv[1]), content)
        if ADDON.getSetting('auto-view') == 'true':#<<<----see here if auto-view is enabled(true) 
                xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )#<<<-----then get the view type
                      
               
params=get_params()
url=None
name=None
mode=None
iconimage=None
description=None
fanart=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass    

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)
print "fanart: "+str(fanart) 
        
#these are the modes which tells the plugin where to go
if mode==None or url==None or len(url)<1:
        
        CATEGORIES()
       
elif mode==1:
       
        GetContent(url)

       
elif mode==2:
        
        MAIN(url)

elif mode==3:
        
        Search(url)        
        
elif mode==200:

        PLAY_STREAM(name,url,iconimage)

elif mode==2001:

        playall(name,url)        
       
xbmcplugin.endOfDirectory(int(sys.argv[1]))
