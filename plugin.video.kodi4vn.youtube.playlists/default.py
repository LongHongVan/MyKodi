#!/usr/bin/python
# -*- coding: utf-8 -*-
import xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , os , base64
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.kodi4vn.youtube.playlists'
Oo0Ooo = xbmcaddon . Addon ( OO0o )
O0O0OO0O0O0 = int ( sys . argv [ 1 ] )
if 5 - 5: iiI / ii1I
def ooO0OO000o ( url ) :
 ii11i = oOooOoO0Oo0O ( url )
 iI1 = re . compile ( "<openSearch:totalResults>(.+?)</openSearch:totalResults><openSearch:startIndex>(.+?)</openSearch:startIndex>" , re . DOTALL ) . findall ( ii11i )
 i1I11i = int ( iI1 [ 0 ] [ 0 ] )
 OoOoOO00 = int ( iI1 [ 0 ] [ 1 ] )
 I11i = ii11i . split ( '<entry' )
 for O0O in range ( 1 , len ( I11i ) , 1 ) :
  Oo = I11i [ O0O ]
  iI1 = re . compile ( "src='(.+?)'" , re . DOTALL ) . findall ( Oo )
  I1ii11iIi11i = iI1 [ 0 ]
  iI1 = re . compile ( "<title>(.+?)</title>" , re . DOTALL ) . findall ( Oo )
  I1IiI = iI1 [ 0 ]
  if len ( iI1 ) > 0 :
   I1IiI = iI1 [ 0 ]
   I1IiI = o0OOO ( I1IiI )
  iI1 = re . compile ( "<media:thumbnail url='(.+?)' height='90' width='120' yt:name='default'/>" , re . DOTALL ) . findall ( Oo )
  iIiiiI = ""
  if ( len ( iI1 ) > 0 ) :
   iIiiiI = iI1 [ 0 ]
  Iii1ii1II11i ( "[B]" + I1IiI + "[/B]" , I1ii11iIi11i , 'showItems' , iIiiiI )
 if OoOoOO00 + 50 <= i1I11i :
  Iii1ii1II11i ( "[Next >]" , url + "&start-index=" + str ( int ( OoOoOO00 ) + 50 ) , "showNextPlaylists" , "" )
 xbmcplugin . endOfDirectory ( O0O0OO0O0O0 )
 if 10 - 10: I1iII1iiII + I1Ii111 / OOo
def Iii1ii1II11i ( name , url , mode , iconimage ) :
 i1i1II = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 O0oo0OO0 = True
 if iconimage == "" : iconimage = "DefaultFolder.png"
 I1i1iiI1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1i1iiI1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : "" } )
 O0oo0OO0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1i1II , listitem = I1i1iiI1 , isFolder = True )
 return O0oo0OO0
 if 24 - 24: oOOOO0o0o
def Ii1iI ( name , url , mode , iconimage , playlistid ) :
 i1i1II = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 O0oo0OO0 = True
 I1i1iiI1 = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 I1i1iiI1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : "" } )
 I1i1iiI1 . setProperty ( 'IsPlayable' , 'true' )
 I1i1iiI1 . addContextMenuItems ( [ ( "Play from here" , "XBMC.RunPlugin(plugin://plugin.video.youtube/?path=/root/playlists&action=play_all&playlist=%s&videoid=%s&)" % ( playlistid , url ) ) ] )
 O0oo0OO0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1i1II , listitem = I1i1iiI1 )
 return O0oo0OO0
 if 100 - 100: i11Ii11I1Ii1i . ooO - OOoO / ooo0Oo0 * i1 - OOooo0000ooo
def OOo000 ( youtubeID ) :
 O0 = I11i1i11i1I ( youtubeID )
 Iiii = xbmcgui . ListItem ( path = O0 )
 return xbmcplugin . setResolvedUrl ( O0O0OO0O0O0 , True , Iiii )
 if 87 - 87: oO0o0o0ooO0oO / I1i1I - OoOoo0 % iIiiI1 % OOooO % OOoO00o
def I11i1i11i1I ( youtubeID ) :
 O0 = "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid=" + youtubeID
 return O0
 if 9 - 9: I1iiiiI1iII - oO0o0o0ooO0oO / I1Ii111 + oO0o0o0ooO0oO
def IiIi1Iii1I1 ( ) :
 ii11i = oOooOoO0Oo0O ( O0 + "&max-results=50" )
 iI1 = re . compile ( "<openSearch:totalResults>(.+?)</openSearch:totalResults><openSearch:startIndex>(.+?)</openSearch:startIndex>" , re . DOTALL ) . findall ( ii11i )
 i1I11i = int ( iI1 [ 0 ] [ 0 ] )
 OoOoOO00 = int ( iI1 [ 0 ] [ 1 ] )
 iI1 = re . compile ( "<yt:playlistId>(.+?)</yt:playlistId>" , re . DOTALL ) . findall ( ii11i )
 O00O0O0O0 = iI1 [ 0 ]
 I11i = ii11i . split ( '<entry' )
 for O0O in range ( 1 , len ( I11i ) , 1 ) :
  Oo = I11i [ O0O ]
  iI1 = re . compile ( "<yt:videoid>(.+?)</yt:videoid>" , re . DOTALL ) . findall ( Oo )
  ooO0O = iI1 [ 0 ]
  iI1 = re . compile ( "<title>(.+?)</title>" , re . DOTALL ) . findall ( Oo )
  I1IiI = iI1 [ 0 ]
  if len ( iI1 ) > 0 :
   I1IiI = iI1 [ 0 ]
   I1IiI = o0OOO ( I1IiI )
  iI1 = re . compile ( "<media:thumbnail url='(.+?)' height='90' width='120'" , re . DOTALL ) . findall ( Oo )
  iIiiiI = ""
  if len ( iI1 ) > 0 :
   iIiiiI = iI1 [ 0 ]
  Ii1iI ( "[B]" + I1IiI + "[/B]" , ooO0O , 'playVideo' , iIiiiI , O00O0O0O0 )
 if OoOoOO00 + 50 <= i1I11i :
  Iii1ii1II11i ( "[Next >]" , O0 + "&start-index=" + str ( int ( OoOoOO00 ) + 50 ) + "&max-results=50" , 'showItems' , iIiiiI )
 xbmcplugin . endOfDirectory ( O0O0OO0O0O0 )
 if 63 - 63: OOo . OOo
def o0OOO ( title ) :
 title = title . replace ( "&lt;" , "<" ) . replace ( "&gt;" , ">" ) . replace ( "&amp;" , "&" ) . replace ( "&#039;" , "\\" ) . replace ( "&quot;" , "\"" ) . replace ( "&szlig;" , "ß" ) . replace ( "&ndash;" , "-" )
 title = title . replace ( "&#038;" , "&" ) . replace ( "&#8230;" , "..." ) . replace ( "&#8211;" , "-" ) . replace ( "&#8220;" , "-" ) . replace ( "&#8221;" , "-" ) . replace ( "&#8217;" , "'" )
 title = title . replace ( "&Auml;" , "Ä" ) . replace ( "&Uuml;" , "Ü" ) . replace ( "&Ouml;" , "Ö" ) . replace ( "&auml;" , "ä" ) . replace ( "&uuml;" , "ü" ) . replace ( "&ouml;" , "ö" )
 title = title . strip ( )
 return title
 if 32 - 32: I1Ii111 . I1i1I % ooO . ooo0Oo0
def oOooOoO0Oo0O ( url ) :
 i1I111I = urllib2 . Request ( url )
 i1I111I . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:19.0) Gecko/20100101 Firefox/19.0' )
 i11I1IIiiIi = urllib2 . urlopen ( i1I111I )
 IiIiIi = i11I1IIiiIi . read ( )
 i11I1IIiiIi . close ( )
 return IiIiIi
 if 40 - 40: OOooo0000ooo . OOoO . i11Ii11I1Ii1i . I1Ii111
def I11iii ( parameters ) :
 OO0O00 = { }
 if 20 - 20: I1iII1iiII
 if parameters :
  Ii11iI1i = parameters [ 1 : ] . split ( "&" )
  for Ooo in Ii11iI1i :
   O0o0Oo = Ooo . split ( '=' )
   if ( len ( O0o0Oo ) ) == 2 :
    OO0O00 [ O0o0Oo [ 0 ] ] = O0o0Oo [ 1 ]
 return OO0O00
 if 78 - 78: ii1I - OoOoo0 * ooO + ooo0Oo0 + iIiiI1 + iIiiI1
I11I11i1I = xbmc . translatePath ( Oo0Ooo . getAddonInfo ( 'profile' ) )
if 49 - 49: OOo % iIiiI1 * iiI
if os . path . exists ( I11I11i1I ) == False :
 os . mkdir ( I11I11i1I )
oOOo0oo = os . path . join ( I11I11i1I , 'visitor' )
if 80 - 80: I1i1I * i11iIiiIii / OOoO00o
if os . path . exists ( oOOo0oo ) == False :
 from random import randint
 I11II1i = open ( oOOo0oo , "w" )
 I11II1i . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 I11II1i . close ( )
 if 23 - 23: i1 / ooo0Oo0 + I1i1I + I1i1I / OOo
def iiI1 ( k , e ) :
 i11Iiii = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for O0O in range ( len ( e ) ) :
  iI = k [ O0O % len ( k ) ]
  I1i1I1II = chr ( ( 256 + ord ( e [ O0O ] ) - ord ( iI ) ) % 256 )
  i11Iiii . append ( I1i1I1II )
 return "" . join ( i11Iiii )
 if 45 - 45: OOoO00o . OOoO
def oO ( utm_url ) :
 ii1i1I1i = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  i1I111I = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : ii1i1I1i }
 )
  i11I1IIiiIi = urllib2 . urlopen ( i1I111I ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return i11I1IIiiIi
 if 53 - 53: OOooO + oOOOO0o0o * OOooo0000ooo
def OooOooooOOoo0 ( group , name ) :
 try :
  try :
   from hashlib import md5
  except :
   from md5 import md5
  from random import randint
  import time
  from urllib import unquote , quote
  from os import environ
  from hashlib import sha1
  o00OO0OOO0 = "1.0"
  oo0 = open ( oOOo0oo ) . read ( )
  o00 = "VIPPlaylists"
  OooOooo = "UA-52209804-2"
  O000oo0O = "www.viettv24.com"
  OOOO = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   i11i1 = OOOO + "?" + "utmwv=" + o00OO0OOO0 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( o00 ) + "&utmac=" + OooOooo + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , oo0 , "1" , "1" , "2" ] )
   if 29 - 29: i1 % oOOOO0o0o + I1iiiiI1iII / ooo0Oo0 + oO0o0o0ooO0oO * ooo0Oo0
   if 42 - 42: OoOoo0 + OOooo0000ooo
   if 76 - 76: OOoO00o - ooO
   if 70 - 70: I1iiiiI1iII
   if 61 - 61: i1 . i1
  else :
   if group == "None" :
    i11i1 = OOOO + "?" + "utmwv=" + o00OO0OOO0 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( o00 + "/" + name ) + "&utmac=" + OooOooo + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , oo0 , "1" , "1" , "2" ] )
    if 10 - 10: OOoO * iIiiI1 . I1i1I + OOo - I1iiiiI1iII * I1Ii111
    if 56 - 56: ooo0Oo0 * OOooO * OOo
    if 80 - 80: ooo0Oo0 * OOo % OOo
    if 59 - 59: ii1I + oOOOO0o0o - ooo0Oo0 - oOOOO0o0o + oO0o0o0ooO0oO / i1
    if 24 - 24: I1i1I . iIiiI1 % oO0o0o0ooO0oO + I1iiiiI1iII % OOoO
   else :
    i11i1 = OOOO + "?" + "utmwv=" + o00OO0OOO0 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( o00 + "/" + group + "/" + name ) + "&utmac=" + OooOooo + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , oo0 , "1" , "1" , "2" ] )
    if 4 - 4: OOooO - ooO * OOoO - I1i1I
    if 41 - 41: OOoO . oOOOO0o0o * OOooo0000ooo % OOooO
    if 86 - 86: oOOOO0o0o + OoOoo0 % i11iIiiIii * OOooo0000ooo . I1iiiiI1iII * I1i1I
    if 44 - 44: OOooo0000ooo
    if 88 - 88: OOoO00o % OoOoo0 . OOo
    if 38 - 38: ooo0Oo0
  print "============================ POSTING ANALYTICS ============================"
  oO ( i11i1 )
  if 57 - 57: iiI / OOooo0000ooo * OOoO00o / OOoO . OOo
  if not group == "None" :
   i11iIIIIIi1 = OOOO + "?" + "utmwv=" + o00OO0OOO0 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( O000oo0O ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + o00 + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( o00 ) + "&utmac=" + OooOooo + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , oo0 , "1" , "2" ] )
   if 20 - 20: I1Ii111 + i1 - I1iiiiI1iII
   if 30 - 30: OOo - oO0o0o0ooO0oO - i11iIiiIii % OOoO - OOo * OoOoo0
   if 61 - 61: OOooo0000ooo - I1i1I % oO0o0o0ooO0oO
   if 84 - 84: OOooo0000ooo * ooO / I1i1I - iiI
   if 30 - 30: ii1I / I1iiiiI1iII - OOoO00o - OOo % iIiiI1
   if 49 - 49: oOOOO0o0o % I1iiiiI1iII . I1iiiiI1iII . I1i1I * I1iiiiI1iII
   if 97 - 97: OoOoo0 + ooo0Oo0 . oO0o0o0ooO0oO + i1 % iIiiI1
   if 95 - 95: I1Ii111
   try :
    print "============================ POSTING TRACK EVENT ============================"
    oO ( i11iIIIIIi1 )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 3 - 3: OOoO00o - iiI / OOoO00o % ooO / OOoO00o . oOOOO0o0o
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 50 - 50: OOooO
i11I1iIiII = I11iii ( sys . argv [ 2 ] )
oO00o0 = i11I1iIiII . get ( 'mode' )
O0 = i11I1iIiII . get ( 'url' )
OOoo0O = i11I1iIiII . get ( 'name' )
if type ( O0 ) == type ( str ( ) ) :
 O0 = urllib . unquote_plus ( O0 )
if type ( OOoo0O ) == type ( str ( ) ) :
 OOoo0O = urllib . unquote_plus ( OOoo0O )
if oO00o0 == 'showItems' :
 OooOooooOOoo0 ( "Browse" , OOoo0O )
 IiIi1Iii1I1 ( )
elif oO00o0 == 'showNextPlaylists' :
 OooOooooOOoo0 ( "Browse" , OOoo0O )
 ooO0OO000o ( O0 )
elif oO00o0 == 'playVideo' :
 OooOooooOOoo0 ( "Play" , OOoo0O + "/" + O0 )
 Oo0ooOo0o = xbmcgui . DialogProgress ( )
 Oo0ooOo0o . create ( 'VIP Playlist' , 'Loading video. Please wait...' )
 OOo000 ( O0 )
 Oo0ooOo0o . close ( )
 del Oo0ooOo0o
else :
 Ii1i1 = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 Ii1i1 = xbmc . translatePath ( os . path . join ( Ii1i1 , "temp.jpg" ) )
 urllib . urlretrieve ( 'http://echipstore.net/images/vip.jpg' , Ii1i1 )
 iiIii = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , Ii1i1 )
 ooo0O = xbmcgui . WindowDialog ( )
 ooo0O . addControl ( iiIii )
 #ooo0O . doModal ( )
 OooOooooOOoo0 ( "None" , "None" )
 ooO0OO000o ( "https://gdata.youtube.com/feeds/api/users/xempihim3/playlists?v=2&max-results=30" ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
