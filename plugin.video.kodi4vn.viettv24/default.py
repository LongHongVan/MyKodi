#!/usr/bin/python
#coding=utf-8
import xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , os , base64 , json , shutil , zipfile
from math import radians , sqrt , sin , cos , atan2
from operator import itemgetter
import xmltodict
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.kodi4vn.viettv24'
Oo0Ooo = xbmcaddon . Addon ( OO0o )
O0O0OO0O0O0 = xbmc . translatePath ( Oo0Ooo . getAddonInfo ( 'profile' ) )
iiiii = int ( sys . argv [ 1 ] )
if 64 - 64: iIIi1iI1II111 + ii11i / oOooOoO0Oo0O
def iI1 ( ) :
 i1I11i = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 i1I11i = xbmc . translatePath ( os . path . join ( i1I11i , "temp.jpg" ) )
 urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/viettv24.jpg' , i1I11i )
 OoOoOO00 = xbmcgui . WindowDialog ( )
 I11i = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , i1I11i )
 OoOoOO00 . addControl ( I11i )
 #OoOoOO00 . doModal ( )
 if 64 - 64: OOooo000oo0 . i1 * ii1IiI1i % IIIiiIIii
 I11iIi1I = IiiIII111iI ( IiII ( "ghjl" , "z9ze3KGXmeDP19jTld7T0dvc4J6bls3b1Jfd29zazdHGztPYzA==" ) )
 if 28 - 28: Ii11111i * iiI1i1
 for i1I1ii1II1iII , oooO0oo0oOOOO in eval ( I11iIi1I ) :
  O0oO ( i1I1ii1II1iII , oooO0oo0oOOOO , 'indexgroup' , i1I11i . replace ( "temp.jpg" , "icon.png" ) )
 o0oO0 = xbmc . getSkinDir ( )
 if o0oO0 == 'skin.xeebo' :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
  if 100 - 100: i11Ii11I1Ii1i
def Ooo ( url ) :
 o0oOoO00o = IiiIII111iI ( url )
 i1oOOoo00O0O = re . compile ( '<name>(.+?)</name>' ) . findall ( o0oOoO00o )
 if len ( i1oOOoo00O0O ) == 1 :
  i1111 = re . compile ( '<item>(.+?)</item>' ) . findall ( o0oOoO00o )
  for i11 in i1111 :
   I11 = ""
   Oo0o0000o0o0 = ""
   oOo0oooo00o = ""
   if "/title" in i11 :
    Oo0o0000o0o0 = re . compile ( '<title>(.+?)</title>' ) . findall ( i11 ) [ 0 ]
   if "/link" in i11 :
    oOo0oooo00o = re . compile ( '<link>(.+?)</link>' ) . findall ( i11 ) [ 0 ]
   if "/thumbnail" in i11 :
    I11 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i11 ) [ 0 ]
   oO0o0o0ooO0oO ( i1oOOoo00O0O [ 0 ] + "/" + Oo0o0000o0o0 , oOo0oooo00o , 'play' , I11 )
  o0oO0 = xbmc . getSkinDir ( )
  if o0oO0 == 'skin.xeebo' :
   xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 else :
  for oo0o0O00 in i1oOOoo00O0O :
   O0oO ( oo0o0O00 , url + "&n=" + oo0o0O00 , 'index' , '' )
   if 68 - 68: o00oo . iI1OoOooOOOO + i11iiII
def I1iiiiI1iII ( url ) :
 IiIi11i = url . split ( "&n=" ) [ 1 ]
 o0oOoO00o = IiiIII111iI ( url )
 iIii1I111I11I = re . compile ( '<channel>(.+?)</channel>' ) . findall ( o0oOoO00o )
 for OO00OooO0OO in iIii1I111I11I :
  if IiIi11i in OO00OooO0OO :
   i1111 = re . compile ( '<item>(.+?)</item>' ) . findall ( OO00OooO0OO )
   for i11 in i1111 :
    I11 = ""
    Oo0o0000o0o0 = ""
    oOo0oooo00o = ""
    if "/title" in i11 :
     Oo0o0000o0o0 = re . compile ( '<title>(.+?)</title>' ) . findall ( i11 ) [ 0 ]
    if "/link" in i11 :
     oOo0oooo00o = re . compile ( '<link>(.+?)</link>' ) . findall ( i11 ) [ 0 ]
    if "/thumbnail" in i11 :
     I11 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i11 ) [ 0 ]
    oO0o0o0ooO0oO ( IiIi11i + "/" + Oo0o0000o0o0 , oOo0oooo00o , 'play' , I11 )
 o0oO0 = xbmc . getSkinDir ( )
 if o0oO0 == 'skin.xeebo' :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
  if 28 - 28: iIii1
def IiII ( k , e ) :
 oOOoO0 = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for O0OoO000O0OO in range ( len ( e ) ) :
  iiI1IiI = k [ O0OoO000O0OO % len ( k ) ]
  II = chr ( ( 256 + ord ( e [ O0OoO000O0OO ] ) - ord ( iiI1IiI ) ) % 256 )
  oOOoO0 . append ( II )
 return "" . join ( oOOoO0 )
 if 57 - 57: ooOoo0O
def OooO0 ( source , dest_dir ) :
 with zipfile . ZipFile ( source ) as II11iiii1Ii :
  for OO0oOoo in II11iiii1Ii . infolist ( ) :
   O0o0Oo = OO0oOoo . filename . split ( '/' )
   i1I11i = dest_dir
   for Oo00OOOOO in O0o0Oo [ : - 1 ] :
    O0O , Oo00OOOOO = os . path . splitdrive ( Oo00OOOOO )
    O00o0OO , Oo00OOOOO = os . path . split ( Oo00OOOOO )
    if Oo00OOOOO in ( os . curdir , os . pardir , '' ) : continue
    i1I11i = os . path . join ( i1I11i , Oo00OOOOO )
   II11iiii1Ii . extract ( OO0oOoo , i1I11i )
   if 44 - 44: O0o / o0 + I11ii1 / o0OO0oo0oOO . i11Ii11I1Ii1i
def I1iii ( url ) :
 i1I11i = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 i1iiI11I = xbmc . translatePath ( os . path . join ( i1I11i , "tmp" ) )
 if os . path . exists ( i1iiI11I ) :
  shutil . rmtree ( i1iiI11I )
 os . makedirs ( i1iiI11I )
 if ".zip" in url :
  iiii = xbmc . translatePath ( os . path . join ( i1iiI11I , "temp.zip" ) )
  urllib . urlretrieve ( url , iiii )
  OooO0 ( iiii , i1iiI11I )
 else :
  oO0o0O0OOOoo0 = xbmc . translatePath ( os . path . join ( i1iiI11I , "temp.jpg" ) )
  urllib . urlretrieve ( url , oO0o0O0OOOoo0 )
 xbmc . executebuiltin ( "SlideShow(%s,recursive)" % i1iiI11I )
 if 48 - 48: iIIi1iI1II111 + iIIi1iI1II111 - o00oo . o0OO0oo0oOO / ii11i
def OoOOO00oOO0 ( url , title ) :
 if ( "youtube" in url ) :
  oOoo = re . compile ( '(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)' ) . findall ( url )
  iIii11I = oOoo [ 0 ] [ len ( oOoo [ 0 ] ) - 1 ] . replace ( 'v/' , '' )
  url = 'plugin://plugin.video.youtube?path=/root/video&action=play_video&videoid=' + iIii11I . replace ( '?' , '' )
  xbmc . executebuiltin ( "xbmc.PlayMedia(" + url + ")" )
 else :
  if ( "50.7.104.132" in url ) :
   OOO0OOO00oo = "http://www.viettv24.com/api/?ip=%s"
   Iii111II = json . loads ( urllib2 . urlopen ( OOO0OOO00oo % "" ) . read ( ) )
   iiii11I = "http://50.7.30.60:1935/loadbalancer?serverInfoXML"
   Ooo0OO0oOO = xmltodict . parse ( urllib2 . urlopen ( iiii11I ) . read ( ) )
   ii11i1 = [ ]
   for IIIii1II1II in Ooo0OO0oOO [ "LoadBalancerServerInfo" ] [ "LoadBalancerServer" ] :
    if ( int ( IIIii1II1II [ "connectCount" ] ) < 375 ) and ( IIIii1II1II [ "status" ] . lower ( ) == "running" ) :
     print IIIii1II1II [ "status" ] . lower ( )
     i1I1iI = json . loads ( urllib2 . urlopen ( OOO0OOO00oo % IIIii1II1II [ "redirect" ] ) . read ( ) )
     oo0OooOOo0 = o0O ( float ( Iii111II [ "latitude" ] ) , float ( Iii111II [ "longitude" ] ) , float ( i1I1iI [ "latitude" ] ) , float ( i1I1iI [ "longitude" ] ) )
     ii11i1 . append ( [ IIIii1II1II [ "redirect" ] , float ( oo0OooOOo0 ) + float ( IIIii1II1II [ "connectCount" ] ) ] )
   O00oO = sorted ( ii11i1 , key = itemgetter ( 1 ) ) [ 0 ] [ 0 ]
   url = url . replace ( "50.7.104.132" , O00oO )
  title = urllib . unquote_plus ( title )
  I11i1I1I = xbmc . PlayList ( 1 )
  I11i1I1I . clear ( )
  oO0Oo = xbmcgui . ListItem ( title )
  oO0Oo . setInfo ( 'video' , { 'Title' : title } )
  oOOoo0Oo = xbmc . Player ( )
  I11i1I1I . add ( url , oO0Oo )
  oOOoo0Oo . play ( I11i1I1I )
  if 78 - 78: iIii1
def o0O ( lat1 , lon1 , lat2 , lon2 ) :
 lat1 = radians ( lat1 )
 lon1 = radians ( lon1 )
 lat2 = radians ( lat2 )
 lon2 = radians ( lon2 )
 if 71 - 71: i11iiII + o0OO0oo0oOO % i11iIiiIii + o00oo - o0
 oO0OOoO0 = lon1 - lon2
 if 34 - 34: o0 - o0 * ii1IiI1i + ooOoo0O % o0
 i111IiI1I = 6372.8
 if 70 - 70: ooOoo0O . IIIiiIIii / i11Ii11I1Ii1i . ooOoo0O - iIIi1iI1II111 / o0
 ooOooo000oOO = sqrt (
 ( cos ( lat2 ) * sin ( oO0OOoO0 ) ) ** 2
 + ( cos ( lat1 ) * sin ( lat2 ) - sin ( lat1 ) * cos ( lat2 ) * cos ( oO0OOoO0 ) ) ** 2
 )
 Oo0oOOo = sin ( lat1 ) * sin ( lat2 ) + cos ( lat1 ) * cos ( lat2 ) * cos ( oO0OOoO0 )
 Oo0OoO00oOO0o = atan2 ( ooOooo000oOO , Oo0oOOo )
 return i111IiI1I * Oo0OoO00oOO0o
 if 80 - 80: iI1OoOooOOOO + i11iiII - i11iiII % O0o
def IiiIII111iI ( url ) :
 oOo0oooo00o = ""
 if os . path . exists ( url ) == True :
  oOo0oooo00o = open ( url ) . read ( )
 else :
  OoOO0oo0o = urllib2 . Request ( url )
  OoOO0oo0o . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
  II11i1I11Ii1i = urllib2 . urlopen ( OoOO0oo0o )
  oOo0oooo00o = II11i1I11Ii1i . read ( )
  II11i1I11Ii1i . close ( )
  if 97 - 97: o0OO0oo0oOO % O0o * ooOoo0O + i11Ii11I1Ii1i . i11iiII + i11iiII
 if ( "xml" in url ) :
  oOo0oooo00o = IiII ( "umbala" , oOo0oooo00o )
 oOo0oooo00o = '' . join ( oOo0oooo00o . splitlines ( ) ) . replace ( '\'' , '"' )
 oOo0oooo00o = oOo0oooo00o . replace ( '\n' , '' )
 oOo0oooo00o = oOo0oooo00o . replace ( '\t' , '' )
 oOo0oooo00o = re . sub ( '  +' , ' ' , oOo0oooo00o )
 oOo0oooo00o = oOo0oooo00o . replace ( '> <' , '><' )
 return oOo0oooo00o
 if 59 - 59: ii11i * i11iIiiIii / o00oo * OOooo000oo0 * iIIi1iI1II111
def oO0o0o0ooO0oO ( name , url , mode , iconimage ) :
 OOo0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 iiI111I1iIiI = True
 IIIi1I1IIii1II = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 IIIi1I1IIii1II . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 iiI111I1iIiI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOo0o , listitem = IIIi1I1IIii1II )
 return iiI111I1iIiI
 if 65 - 65: ooOoo0O . ii11i / iIIi1iI1II111 - ooOoo0O
def O0oO ( name , url , mode , iconimage ) :
 OOo0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 iiI111I1iIiI = True
 IIIi1I1IIii1II = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IIIi1I1IIii1II . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 iiI111I1iIiI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOo0o , listitem = IIIi1I1IIii1II , isFolder = True )
 return iiI111I1iIiI
 if 21 - 21: ii1IiI1i * ii11i
def oooooOoo0ooo ( parameters ) :
 I1I1IiI1 = { }
 if 5 - 5: i11Ii11I1Ii1i * o0OO0oo0oOO + iiI1i1 . i11iiII + iiI1i1
 if parameters :
  oO = parameters [ 1 : ] . split ( "&" )
  for iIi1IIIi1 in oO :
   O0oOoOOOoOO = iIi1IIIi1 . split ( '=' )
   if ( len ( O0oOoOOOoOO ) ) == 2 :
    I1I1IiI1 [ O0oOoOOOoOO [ 0 ] ] = O0oOoOOOoOO [ 1 ]
 return I1I1IiI1
 if 38 - 38: I11ii1
if os . path . exists ( O0O0OO0O0O0 ) == False :
 os . mkdir ( O0O0OO0O0O0 )
Ii1 = os . path . join ( O0O0OO0O0O0 , 'visitor' )
if 82 - 82: o00oo - ii11i / i11iiII + ooOoo0O
if os . path . exists ( Ii1 ) == False :
 from random import randint
 OOOOoOoo0O0O0 = open ( Ii1 , "w" )
 OOOOoOoo0O0O0 . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 OOOOoOoo0O0O0 . close ( )
 if 85 - 85: iI1OoOooOOOO % i11iIiiIii - O0o * oOooOoO0Oo0O / ii1IiI1i % ii1IiI1i
def IIiIi1iI ( utm_url ) :
 i1IiiiI1iI = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  OoOO0oo0o = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : i1IiiiI1iI }
 )
  II11i1I11Ii1i = urllib2 . urlopen ( OoOO0oo0o ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return II11i1I11Ii1i
 if 49 - 49: ooOoo0O / Ii11111i . i1
def ooOOoooooo ( group , name ) :
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
  II1I = "4.2.8"
  O0 = open ( Ii1 ) . read ( )
  i1II1Iiii1I11 = "VietTV24"
  IIII = "UA-52209804-2"
  iiIiI = "www.viettv24.com"
  o00oooO0Oo = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   o0O0OOO0Ooo = o00oooO0Oo + "?" + "utmwv=" + II1I + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( i1II1Iiii1I11 ) + "&utmac=" + IIII + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , O0 , "1" , "1" , "2" ] )
   if 45 - 45: iIIi1iI1II111 / i11Ii11I1Ii1i
   if 32 - 32: O0o . o0 . o0
   if 62 - 62: o00oo + o0 % O0o + i11iiII
   if 33 - 33: iIIi1iI1II111 . o0 . ii1IiI1i
   if 72 - 72: OOooo000oo0 / Ii11111i + oOooOoO0Oo0O - IIIiiIIii
  else :
   if group == "None" :
    o0O0OOO0Ooo = o00oooO0Oo + "?" + "utmwv=" + II1I + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( i1II1Iiii1I11 + "/" + name ) + "&utmac=" + IIII + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , O0 , "1" , "1" , "2" ] )
    if 29 - 29: o00oo + iI1OoOooOOOO % iIIi1iI1II111
    if 10 - 10: iIii1 / I11ii1 - ii1IiI1i * ii11i - ii1IiI1i
    if 97 - 97: o00oo + ii1IiI1i * ooOoo0O + i11iiII % O0o
    if 74 - 74: iI1OoOooOOOO - IIIiiIIii + oOooOoO0Oo0O + I11ii1 / iiI1i1
    if 23 - 23: iIIi1iI1II111
   else :
    o0O0OOO0Ooo = o00oooO0Oo + "?" + "utmwv=" + II1I + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( i1II1Iiii1I11 + "/" + group + "/" + name ) + "&utmac=" + IIII + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , O0 , "1" , "1" , "2" ] )
    if 85 - 85: ooOoo0O
    if 84 - 84: ii1IiI1i . ii11i % oOooOoO0Oo0O + ooOoo0O % oOooOoO0Oo0O % Ii11111i
    if 42 - 42: Ii11111i / iIii1 / i11Ii11I1Ii1i + O0o / iiI1i1
    if 84 - 84: o0OO0oo0oOO * i1 + IIIiiIIii
    if 53 - 53: O0o % i1 . o0 - ii11i - o0 * i1
    if 77 - 77: ii11i * Ii11111i
  print "============================ POSTING ANALYTICS ============================"
  IIiIi1iI ( o0O0OOO0Ooo )
  if 95 - 95: ii1IiI1i + i11iIiiIii
  if not group == "None" :
   I1Ii = o00oooO0Oo + "?" + "utmwv=" + II1I + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( iiIiI ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + i1II1Iiii1I11 + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( i1II1Iiii1I11 ) + "&utmac=" + IIII + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , O0 , "1" , "2" ] )
   if 94 - 94: ooOoo0O - i1 . i11iiII % iIii1 . i11iIiiIii + iIIi1iI1II111
   if 26 - 26: iIii1 - ii11i - ii1IiI1i / Ii11111i . iiI1i1 % ii11i
   if 91 - 91: i11Ii11I1Ii1i . ii11i / iI1OoOooOOOO + OOooo000oo0
   if 42 - 42: o0OO0oo0oOO . i11Ii11I1Ii1i . o0OO0oo0oOO - o00oo
   if 40 - 40: o0OO0oo0oOO - i11iIiiIii / ooOoo0O
   if 35 - 35: ooOoo0O - ii1IiI1i % i11Ii11I1Ii1i . oOooOoO0Oo0O % ooOoo0O
   if 47 - 47: O0o - ooOoo0O . i1 + oOooOoO0Oo0O . i11iIiiIii
   if 94 - 94: i11Ii11I1Ii1i * ooOoo0O / IIIiiIIii / ooOoo0O
   try :
    print "============================ POSTING TRACK EVENT ============================"
    IIiIi1iI ( I1Ii )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 87 - 87: IIIiiIIii . o0
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 75 - 75: o0OO0oo0oOO + iiI1i1 + i11Ii11I1Ii1i * iIii1 % iI1OoOooOOOO . O0o
oOI1Ii1I1 = oooooOoo0ooo ( sys . argv [ 2 ] )
IiII111iI1ii1 = oOI1Ii1I1 . get ( 'mode' )
iI11I1II = oOI1Ii1I1 . get ( 'url' )
oo0o0O00 = oOI1Ii1I1 . get ( 'name' )
if type ( iI11I1II ) == type ( str ( ) ) :
 iI11I1II = urllib . unquote_plus ( iI11I1II )
if type ( oo0o0O00 ) == type ( str ( ) ) :
 oo0o0O00 = urllib . unquote_plus ( oo0o0O00 )
 if 40 - 40: ii11i / iiI1i1 % o00oo + i1
ii1Ii1I1Ii11i = str ( sys . argv [ 1 ] )
if IiII111iI1ii1 == 'index' :
 ooOOoooooo ( "Browse" , oo0o0O00 )
 I1iiiiI1iII ( iI11I1II )
elif IiII111iI1ii1 == 'indexgroup' :
 ooOOoooooo ( "Browse" , oo0o0O00 )
 Ooo ( iI11I1II )
elif IiII111iI1ii1 == 'play' :
 ooOOoooooo ( "Play" , oo0o0O00 + "/" + iI11I1II )
 if any ( x in iI11I1II for x in [ ".jpg" , ".zip" ] ) :
  I1iii ( iI11I1II )
 else :
  i1111I1I = xbmcgui . DialogProgress ( )
  i1111I1I . create ( 'Brought to you by VietTV24.com' , 'Loading video. Please wait...' )
  OoOOO00oOO0 ( iI11I1II , oo0o0O00 )
  i1111I1I . close ( )
  del i1111I1I
else :
 ooOOoooooo ( "None" , "None" )
 iI1 ( )
xbmcplugin . endOfDirectory ( int ( ii1Ii1I1Ii11i ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
