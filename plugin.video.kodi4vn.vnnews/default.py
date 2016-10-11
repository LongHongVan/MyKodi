#!/usr/bin/python
# -*- coding: utf-8 -*-
import xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , os , base64
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.kodi4vn.youtube.vnnews'
Oo0Ooo = xbmcaddon . Addon ( OO0o )
O0O0OO0O0O0 = int ( sys . argv [ 1 ] )
if 5 - 5: iiI / ii1I
def ooO0OO000o ( ) :
 if 4 - 4: IiII1IiiIiI1 / iIiiiI1IiI1I1
 o0OoOoOO00 = urllib2 . urlopen ( 'https://docs.google.com/spreadsheets/d/1P1ViMaKLDRZzUbHZ5aE192R-juxmMycs2R8RrludeVw/export?format=tsv&id=1P1ViMaKLDRZzUbHZ5aE192R-juxmMycs2R8RrludeVw&gid=0' )
 I11i = o0OoOoOO00 . read ( ) . decode ( 'utf-8-sig' ) . encode ( 'utf8' )
 o0OoOoOO00 . close ( )
 for O0O in I11i . split ( "\n" ) :
  Oo = O0O . split ( "\t" )
  I1ii11iIi11i ( Oo [ 0 ] , Oo [ 1 ] , 'index' , '' )
 I1IiI = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 I1IiI = xbmc . translatePath ( os . path . join ( I1IiI , "temp.jpg" ) )
 urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/vnnews.jpg' , I1IiI )
 o0OOO = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , I1IiI )
 iIiiiI = xbmcgui . WindowDialog ( )
 iIiiiI . addControl ( o0OOO )
 #iIiiiI . doModal ( )
 if 23 - 23: iii1II11ii * i11iII1iiI + iI1Ii11111iIi + ii1II11I1ii1I + oO0o0ooO0 - iiIIIII1i1iI
def o0oO0 ( url ) :
 oo00 = o00 ( url )
 Oo0oO0ooo = re . compile ( "<openSearch:totalResults>(.+?)</openSearch:totalResults><openSearch:startIndex>(.+?)</openSearch:startIndex>" , re . DOTALL ) . findall ( oo00 )
 o0oOoO00o = int ( Oo0oO0ooo [ 0 ] [ 0 ] )
 i1 = int ( Oo0oO0ooo [ 0 ] [ 1 ] )
 oOOoo00O0O = oo00 . split ( '<entry' )
 if i1 < 50 :
  i1111 = re . compile ( "users/(.+?)/" , re . DOTALL ) . findall ( url ) [ 0 ]
  I1ii11iIi11i ( "[COLOR orange][B]Hot News[/B][/COLOR]" , "https://gdata.youtube.com/feeds/api/users/%s/uploads?v=2&max-results=50" % i1111 , 'showItems' , '' )
 for i11 in range ( 1 , len ( oOOoo00O0O ) , 1 ) :
  I11 = oOOoo00O0O [ i11 ]
  Oo0oO0ooo = re . compile ( "src='(.+?)'" , re . DOTALL ) . findall ( I11 )
  Oo0o0000o0o0 = Oo0oO0ooo [ 0 ]
  Oo0oO0ooo = re . compile ( "<title>(.+?)</title>" , re . DOTALL ) . findall ( I11 )
  oOo0oooo00o = Oo0oO0ooo [ 0 ]
  if len ( Oo0oO0ooo ) > 0 :
   oOo0oooo00o = Oo0oO0ooo [ 0 ]
   oOo0oooo00o = oO0o0o0ooO0oO ( oOo0oooo00o )
  Oo0oO0ooo = re . compile ( "<media:thumbnail url='(.+?)' height='90' width='120' yt:name='default'/>" , re . DOTALL ) . findall ( I11 )
  oo0o0O00 = ""
  if ( len ( Oo0oO0ooo ) > 0 ) :
   oo0o0O00 = Oo0oO0ooo [ 0 ]
  I1ii11iIi11i ( "[B]" + oOo0oooo00o + "[/B]" , Oo0o0000o0o0 , 'showItems' , oo0o0O00 )
 if i1 + 50 <= o0oOoO00o :
  I1ii11iIi11i ( "[Next >]" , url + "&start-index=" + str ( int ( i1 ) + 50 ) , "showNextPlaylists" , "" )
  if 68 - 68: o00oo . iI1 + OoOooOOOO
def I1ii11iIi11i ( name , url , mode , iconimage ) :
 i11iiII = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 I1iiiiI1iII = True
 if iconimage == "" : iconimage = "DefaultFolder.png"
 IiIi11i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiIi11i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : "" } )
 I1iiiiI1iII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i11iiII , listitem = IiIi11i , isFolder = True )
 return I1iiiiI1iII
 if 43 - 43: o0O0 * O00O0O0O0
def ooO0O ( name , url , mode , iconimage ) :
 i11iiII = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 I1iiiiI1iII = True
 IiIi11i = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 IiIi11i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : "" } )
 IiIi11i . setProperty ( 'IsPlayable' , 'true' )
 I1iiiiI1iII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i11iiII , listitem = IiIi11i )
 return I1iiiiI1iII
 if 63 - 63: iIii1 . oOOoO0
def O0OoO000O0OO ( youtubeID ) :
 iiI1IiI = II ( youtubeID )
 ooOoOoo0O = xbmcgui . ListItem ( path = iiI1IiI )
 ooOoOoo0O . setProperty ( "IsPlayable" , "true" )
 return xbmcplugin . setResolvedUrl ( O0O0OO0O0O0 , True , ooOoOoo0O )
 if 76 - 76: i1II1I11 / i1I / OoOooOOOO / IiII1IiiIiI1 % iI1
def II ( youtubeID ) :
 iiI1IiI = "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid=" + youtubeID
 return iiI1IiI
 if 75 - 75: iIii1
def oo ( ) :
 oo00 = o00 ( iiI1IiI + "&max-results=50" )
 Oo0oO0ooo = re . compile ( "<openSearch:totalResults>(.+?)</openSearch:totalResults><openSearch:startIndex>(.+?)</openSearch:startIndex>" , re . DOTALL ) . findall ( oo00 )
 o0oOoO00o = int ( Oo0oO0ooo [ 0 ] [ 0 ] )
 i1 = int ( Oo0oO0ooo [ 0 ] [ 1 ] )
 oOOoo00O0O = oo00 . split ( '<entry' )
 for i11 in range ( 1 , len ( oOOoo00O0O ) , 1 ) :
  I11 = oOOoo00O0O [ i11 ]
  Oo0oO0ooo = re . compile ( "<yt:videoid>(.+?)</yt:videoid>" , re . DOTALL ) . findall ( I11 )
  O0o0Oo = Oo0oO0ooo [ 0 ]
  Oo0oO0ooo = re . compile ( "<title>(.+?)</title>" , re . DOTALL ) . findall ( I11 )
  oOo0oooo00o = Oo0oO0ooo [ 0 ]
  if len ( Oo0oO0ooo ) > 0 :
   oOo0oooo00o = Oo0oO0ooo [ 0 ]
   oOo0oooo00o = oO0o0o0ooO0oO ( oOo0oooo00o )
  Oo0oO0ooo = re . compile ( "<media:thumbnail url='(.+?)' height='90' width='120'" , re . DOTALL ) . findall ( I11 )
  oo0o0O00 = ""
  if len ( Oo0oO0ooo ) > 0 :
   oo0o0O00 = Oo0oO0ooo [ 0 ]
  ooO0O ( "[B]" + oOo0oooo00o + "[/B]" , O0o0Oo , 'playVideo' , oo0o0O00 )
 if i1 + 50 <= o0oOoO00o :
  I1ii11iIi11i ( "[Next >]" , iiI1IiI + "&start-index=" + str ( int ( i1 ) + 50 ) + "&max-results=50" , 'showItems' , oo0o0O00 )
  if 78 - 78: ii1I - O00O0O0O0 * ii1II11I1ii1I + iiIIIII1i1iI + iIii1 + iIii1
def oO0o0o0ooO0oO ( title ) :
 title = title . replace ( "&lt;" , "<" ) . replace ( "&gt;" , ">" ) . replace ( "&amp;" , "&" ) . replace ( "&#039;" , "\\" ) . replace ( "&quot;" , "\"" ) . replace ( "&szlig;" , "ß" ) . replace ( "&ndash;" , "-" )
 title = title . replace ( "&#038;" , "&" ) . replace ( "&#8230;" , "..." ) . replace ( "&#8211;" , "-" ) . replace ( "&#8220;" , "-" ) . replace ( "&#8221;" , "-" ) . replace ( "&#8217;" , "'" )
 title = title . replace ( "&Auml;" , "Ä" ) . replace ( "&Uuml;" , "Ü" ) . replace ( "&Ouml;" , "Ö" ) . replace ( "&auml;" , "ä" ) . replace ( "&uuml;" , "ü" ) . replace ( "&ouml;" , "ö" )
 title = title . strip ( )
 return title
 if 11 - 11: iIii1 - ii1II11I1ii1I % i1I % iIii1 / oO0o0ooO0 - ii1II11I1ii1I
def o00 ( url ) :
 o0o0oOOOo0oo = urllib2 . Request ( url )
 o0o0oOOOo0oo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:19.0) Gecko/20100101 Firefox/19.0' )
 o0oo0o0O00OO = urllib2 . urlopen ( o0o0oOOOo0oo )
 o0oO = o0oo0o0O00OO . read ( )
 o0oo0o0O00OO . close ( )
 return o0oO
 if 48 - 48: o0O0 + o0O0 / iii1II11ii / ii1I
def i1iiI11I ( parameters ) :
 iiii = { }
 if 54 - 54: o00oo * OoOooOOOO
 if parameters :
  I1IIIii = parameters [ 1 : ] . split ( "&" )
  for oOoOooOo0o0 in I1IIIii :
   OOOO = oOoOooOo0o0 . split ( '=' )
   if ( len ( OOOO ) ) == 2 :
    iiii [ OOOO [ 0 ] ] = OOOO [ 1 ]
 return iiii
 if 87 - 87: iI1 / o0O0 - iIiiiI1IiI1I1 * OoOooOOOO / IiII1IiiIiI1 . iiI
iii11I111 = xbmc . translatePath ( Oo0Ooo . getAddonInfo ( 'profile' ) )
if 63 - 63: ii1II11I1ii1I * iI1 - iIii1 * iiI
if os . path . exists ( iii11I111 ) == False :
 os . mkdir ( iii11I111 )
iIii111IIi = os . path . join ( iii11I111 , 'visitor' )
if 4 - 4: iii1II11ii / i1I . iIii1
if os . path . exists ( iIii111IIi ) == False :
 from random import randint
 O0oo0OO0oOOOo = open ( iIii111IIi , "w" )
 O0oo0OO0oOOOo . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 O0oo0OO0oOOOo . close ( )
 if 35 - 35: oOOoO0 % i11iII1iiI
def Oo ( k , e ) :
 o0OOoo0OO0OOO = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for i11 in range ( len ( e ) ) :
  iI1iI1I1i1I = k [ i11 % len ( k ) ]
  iIi11Ii1 = chr ( ( 256 + ord ( e [ i11 ] ) - ord ( iI1iI1I1i1I ) ) % 256 )
  o0OOoo0OO0OOO . append ( iIi11Ii1 )
 return "" . join ( o0OOoo0OO0OOO )
 if 50 - 50: iii1II11ii - i1I * o00oo / i1II1I11 + iiIIIII1i1iI
def O0O0O ( utm_url ) :
 oO0Oo = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  o0o0oOOOo0oo = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : oO0Oo }
 )
  o0oo0o0O00OO = urllib2 . urlopen ( o0o0oOOOo0oo ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return o0oo0o0O00OO
 if 54 - 54: iiIIIII1i1iI - i11iII1iiI + IiII1IiiIiI1
def O0o0 ( group , name ) :
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
  OO00Oo = "1.0"
  O0OOO0OOoO0O = open ( iIii111IIi ) . read ( )
  O00Oo000ooO0 = "VNNews"
  OoO0O00 = "UA-52209804-2"
  IIiII = "www.viettv24.com"
  o0 = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   ooOooo000oOO = o0 + "?" + "utmwv=" + OO00Oo + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( O00Oo000ooO0 ) + "&utmac=" + OoO0O00 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , O0OOO0OOoO0O , "1" , "1" , "2" ] )
   if 59 - 59: iii1II11ii + IiII1IiiIiI1 * oO0o0ooO0 + iIiiiI1IiI1I1
   if 58 - 58: iii1II11ii * OoOooOOOO * o00oo / OoOooOOOO
   if 75 - 75: iI1
   if 50 - 50: O00O0O0O0 / iI1Ii11111iIi - iI1 - o0O0 % iIii1 - iI1
   if 91 - 91: ii1II11I1ii1I / o0O0 - iii1II11ii . o0O0
  else :
   if group == "None" :
    ooOooo000oOO = o0 + "?" + "utmwv=" + OO00Oo + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( O00Oo000ooO0 + "/" + name ) + "&utmac=" + OoO0O00 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , O0OOO0OOoO0O , "1" , "1" , "2" ] )
    if 18 - 18: iiIIIII1i1iI
    if 98 - 98: iIii1 * iIii1 / iIii1 + o0O0
    if 34 - 34: i1I
    if 15 - 15: o0O0 * i1I * iI1Ii11111iIi % i11iIiiIii % oO0o0ooO0 - OoOooOOOO
    if 68 - 68: i1II1I11 % iIiiiI1IiI1I1 . oOOoO0 . o00oo
   else :
    ooOooo000oOO = o0 + "?" + "utmwv=" + OO00Oo + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( O00Oo000ooO0 + "/" + group + "/" + name ) + "&utmac=" + OoO0O00 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , O0OOO0OOoO0O , "1" , "1" , "2" ] )
    if 92 - 92: iIii1 . i1II1I11
    if 31 - 31: i1II1I11 . oO0o0ooO0 / iiI
    if 89 - 89: oO0o0ooO0
    if 68 - 68: ii1II11I1ii1I * IiII1IiiIiI1 % iiI + ii1II11I1ii1I + i1I
    if 4 - 4: i1I + iiI * OoOooOOOO
    if 55 - 55: iI1Ii11111iIi + ii1I / oO0o0ooO0 * iI1 - i11iIiiIii - O00O0O0O0
  print "============================ POSTING ANALYTICS ============================"
  O0O0O ( ooOooo000oOO )
  if 25 - 25: o00oo
  if not group == "None" :
   Ii1i = o0 + "?" + "utmwv=" + OO00Oo + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( IIiII ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + O00Oo000ooO0 + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( O00Oo000ooO0 ) + "&utmac=" + OoO0O00 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , O0OOO0OOoO0O , "1" , "2" ] )
   if 15 - 15: oOOoO0 . ii1I . IiII1IiiIiI1 / i11iIiiIii - O00O0O0O0 . iIiiiI1IiI1I1
   if 33 - 33: o0O0 . iiIIIII1i1iI
   if 75 - 75: iiIIIII1i1iI % iiIIIII1i1iI . i1II1I11
   if 5 - 5: iiIIIII1i1iI * i1I + oO0o0ooO0 . OoOooOOOO + oO0o0ooO0
   if 91 - 91: iiI
   if 61 - 61: iii1II11ii
   if 64 - 64: i1I / oO0o0ooO0 - iiI - o0O0
   if 86 - 86: o0O0 % oO0o0ooO0 / i11iII1iiI / oO0o0ooO0
   try :
    print "============================ POSTING TRACK EVENT ============================"
    O0O0O ( Ii1i )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 42 - 42: ii1II11I1ii1I
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 67 - 67: i1II1I11 . iIii1 . iiI
IIIIiiII111 = i1iiI11I ( sys . argv [ 2 ] )
OOoOoo = IIIIiiII111 . get ( 'mode' )
iiI1IiI = IIIIiiII111 . get ( 'url' )
oO0000OOo00 = IIIIiiII111 . get ( 'name' )
if type ( iiI1IiI ) == type ( str ( ) ) :
 iiI1IiI = urllib . unquote_plus ( iiI1IiI )
if type ( oO0000OOo00 ) == type ( str ( ) ) :
 oO0000OOo00 = urllib . unquote_plus ( oO0000OOo00 )
if OOoOoo == 'index' :
 O0o0 ( "Browse" , oO0000OOo00 )
 o0oO0 ( iiI1IiI )
elif OOoOoo == 'showItems' :
 O0o0 ( "Browse" , oO0000OOo00 )
 oo ( )
elif OOoOoo == 'showNextPlaylists' :
 O0o0 ( "Browse" , oO0000OOo00 )
 o0oO0 ( iiI1IiI )
elif OOoOoo == 'playVideo' :
 O0o0 ( "Play" , oO0000OOo00 + "/" + iiI1IiI )
 iiIi1IIiIi = xbmcgui . DialogProgress ( )
 iiIi1IIiIi . create ( 'SBTNOfficial Playlist' , 'Loading video. Please wait...' )
 O0OoO000O0OO ( iiI1IiI )
 iiIi1IIiIi . close ( )
 del iiIi1IIiIi
else :
 O0o0 ( "None" , "None" )
 ooO0OO000o ( )
xbmcplugin . endOfDirectory ( O0O0OO0O0O0 )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
