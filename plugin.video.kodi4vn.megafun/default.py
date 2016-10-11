#!/usr/bin/python
# coding=utf-8
import os , xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , random , base64 , json , time , datetime
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.kodi4vn.megafun'
Oo0Ooo = xbmcaddon . Addon ( OO0o )
O0O0OO0O0O0 = int ( sys . argv [ 1 ] )
if 5 - 5: iiI / ii1I
def ooO0OO000o ( ) :
 ii11i = oOooOoO0Oo0O ( )
 for iI1 in ii11i [ 'object' ] :
  if ( iI1 [ 'owner' ] [ 'name' ] . encode ( 'utf-8' ) . strip ( ) not in [ 'True Sport' , 'QTV1' , 'QTV3' ] ) :
   i1I11i = 'http://c2.cdn.truelife.vn/offica/community/avatar?c=%s&m=1' % iI1 [ 'ownerId' ]
   OoOoOO00 = '[B][COLOR green]%s[/COLOR][/B] - ' % iI1 [ 'owner' ] [ 'name' ] . encode ( 'utf-8' ) . strip ( )
   I11i = ''
   O0O = '[B]Đang chiếu[/B]'
   if iI1 [ 'categoryName' ] . encode ( 'utf-8' ) != 'Khác' : I11i = '[B]%s[/B]: ' % iI1 [ 'categoryName' ] . encode ( 'utf-8' ) . strip ( )
   if iI1 [ 'title' ] . encode ( 'utf-8' ) != 'Không rõ' : O0O = '[COLOR yellow]%s[/COLOR]' % iI1 [ 'title' ] . encode ( 'utf-8' ) . strip ( )
   Oo ( OoOoOO00 + I11i + O0O , iI1 [ 'ownerId' ] , i1I11i , 'channelprogram' )
   if 2 - 2: o0 * i1 * ii1IiI1i % OOooOOo / I11iIi1I / IiiIII111iI
 IiII = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 IiII = xbmc . translatePath ( os . path . join ( IiII , "temp.jpg" ) )
 urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/megafun.jpg' , IiII )
 iI1Ii11111iIi = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , IiII )
 i1i1II = xbmcgui . WindowDialog ( )
 i1i1II . addControl ( iI1Ii11111iIi )
 #i1i1II . doModal ( )
 if 96 - 96: o0OO0 - Oo0ooO0oo0oO . I1i1iI1i - o00ooo0 / o00 * Oo0oO0ooo
def o0oOoO00o ( channelid ) :
 i1oOOoo00O0O = i1111 ( channelid )
 i11 = I11 ( )
 Oo0o0000o0o0 = datetime . datetime . fromtimestamp ( i11 ) . strftime ( '%Y-%m-%d %H:%M:%S' )
 oOo0oooo00o ( '[B]%s: Đang chiếu...[/B]' % ( Oo0o0000o0o0 ) , channelid , 'playvideo' , '' , '' )
 if 65 - 65: O0o * i1iIIII * I1
 for O0OoOoo00o in reversed ( i1oOOoo00O0O [ 'object' ] ) :
  iiiI11 = O0OoOoo00o [ 'dateTimeBegin' ] . split ( '.' ) [ 0 ]
  OOooO = time . mktime ( time . strptime ( iiiI11 , '%Y-%m-%d %H:%M:%S' ) )
  if OOooO < i11 :
   OOoO00o = '[B]%s[/B]: ' % O0OoOoo00o [ 'dateTimeBegin' ] . encode ( 'utf-8' ) . strip ( ) . split ( '.' ) [ 0 ]
   I11i = ''
   II111iiii = '[B]Đang chiếu[/B]'
   if O0OoOoo00o [ 'categoryName' ] . encode ( 'utf-8' ) != 'Khác' : I11i = '[COLOR yellow]%s[/COLOR]: ' % O0OoOoo00o [ 'categoryName' ] . encode ( 'utf-8' ) . strip ( )
   if O0OoOoo00o [ 'title' ] . encode ( 'utf-8' ) != 'Không rõ' : II111iiii = '[B]%s[/B]' % O0OoOoo00o [ 'title' ] . encode ( 'utf-8' ) . strip ( )
   oOo0oooo00o ( OOoO00o + I11i + II111iiii , channelid , 'playvideo' , O0OoOoo00o [ 'dateTimeBegin' ] , str ( O0OoOoo00o [ 'duration' ] ) )
   if 48 - 48: I1Ii . IiIi1Iii1I1 - IiIi1Iii1I1 % IiIi1Iii1I1 - o00ooo0 * Oo0oO0ooo
def O00OooO0 ( channelid , starttime , duration ) :
 Ooooo = o00o ( channelid )
 IiI1I1 = Ooooo [ 'object' ] [ 0 ] [ 'streamingUrl' ] . split ( '&' ) [ 0 ] . replace ( 'c=' , '' )
 IiI1I1 = IiI1I1 . replace ( 'vstv018' , 'vstv093' )
 if starttime != '' or duration != '' :
  OOooO = time . mktime ( time . strptime ( starttime . split ( '.' ) [ 0 ] , '%Y-%m-%d %H:%M:%S' ) )
  OoO000 = OOooO + int ( duration ) * 60
  OOoO00o = datetime . datetime . fromtimestamp ( OOooO ) . strftime ( '%H%M' )
  IIiiIiI1 = datetime . datetime . fromtimestamp ( OOooO ) . strftime ( '%y%m%d' )
  iiIiIIi = ooOoo0O ( IiI1I1 , IIiiIiI1 , OOoO00o )
 else :
  iiIiIIi = OooO0 ( IiI1I1 )
 II11iiii1Ii = xbmc . Player ( )
 II11iiii1Ii . play ( iiIiIIi )
 if 70 - 70: o00ooo0 / ii1I % IiIi1Iii1I1 % i11iIiiIii . OOooOOo
def I11 ( ) :
 O0o0Oo = urllib2 . Request ( "http://truelife.vn/offica/community/action?_f=7&jsoncallback=Ext.data.JsonP.callback2" )
 Oo00OOOOO = urllib2 . urlopen ( O0o0Oo )
 O0OO00o0OO = Oo00OOOOO . read ( )
 Oo00OOOOO . close ( )
 O0OO00o0OO = '' . join ( O0OO00o0OO . splitlines ( ) )
 O0OO00o0OO = O0OO00o0OO . replace ( "Ext.data.JsonP.callback2(" , "" )
 O0OO00o0OO = O0OO00o0OO . replace ( ")" , "" )
 I11i1 = json . loads ( O0OO00o0OO )
 iIi1ii1I1 = I11i1 [ 'header' ] [ 'sysdate' ] . replace ( ' ICT' , '' ) . encode ( 'utf-8' )
 o0I11II1i = time . mktime ( time . strptime ( iIi1ii1I1 , '%a %b %d %H:%M:%S %Y' ) )
 return o0I11II1i
 if 23 - 23: I1i1iI1i / Oo0ooO0oo0oO + Oo0oO0ooo + Oo0oO0ooo / ii1IiI1i
def o00o ( channelid ) :
 O0o0Oo = urllib2 . Request ( "http://truelife.vn/offica/truelifetv/lib/action?_f=119&tvChannelId=%s&ownerId=1532&jsoncallback=Ext.data.JsonP.tvprofile" % channelid )
 O0o0Oo . add_header ( 'Host' , 'truelife.vn' )
 O0o0Oo . add_header ( 'Accept-Encoding' , 'gzip, deflate' )
 O0o0Oo . add_header ( 'Referer' , 'http://megafun.vn/tv/' )
 O0o0Oo . add_header ( 'Cookie' , 'ojid="UryGHmUCni0KfiuwTUS2zetq|QZcIptDEA4Rd4pyY3GUauEPigwgClr3zopggcFFuzcqH90Y3MdEz9BOdNMAeYFL3kHVnrovgSQcEM7wp05s6Ovedh74CQjH6krC9J4Yqiq|DuqGSPeU2gaX9VKCJvDE1HIHREnmHbaJbKVVNyAsEMqwvy162y0dPlCA5mNkifc6O4j0GJgCCLiKGAzj69vma5O2h7XkqLpvQI2vNeA="' )
 O0o0Oo . add_header ( 'Connection' , 'keep-alive' )
 Oo00OOOOO = urllib2 . urlopen ( O0o0Oo )
 O0OO00o0OO = Oo00OOOOO . read ( )
 Oo00OOOOO . close ( )
 O0OO00o0OO = '' . join ( O0OO00o0OO . splitlines ( ) )
 O0OO00o0OO = O0OO00o0OO . replace ( "Ext.data.JsonP.tvprofile(" , "" )
 O0OO00o0OO = O0OO00o0OO . replace ( ")" , "" )
 I11i1 = json . loads ( O0OO00o0OO )
 return I11i1
 if 26 - 26: o0
def i1111 ( channelid ) :
 O0o0Oo = urllib2 . Request ( "http://truelife.vn/offica/tvchannel/tvshow/action?_f=14&communityId=%s&jsoncallback=Ext.data.JsonP.tvshow1205151412" % channelid )
 O0o0Oo . add_header ( 'Host' , 'truelife.vn' )
 O0o0Oo . add_header ( 'Accept-Encoding' , 'gzip, deflate' )
 O0o0Oo . add_header ( 'Referer' , 'http://megafun.vn/tv/' )
 O0o0Oo . add_header ( 'Cookie' , 'ojid="UryGHmUCni0KfiuwTUS2zetq|QZcIptDEA4Rd4pyY3GUauEPigwgClr3zopggcFFuzcqH90Y3MdEz9BOdNMAeYFL3kHVnrovgSQcEM7wp05s6Ovedh74CQjH6krC9J4Yqiq|DuqGSPeU2gaX9VKCJisQ26UQYnnCkwbck2oeVngMSDmkUKxjgYQoWsu|6GGsifc6O4j0GJgCCLiKGAzj69vma5O2h7XkqLpvQI2vNeA="' )
 O0o0Oo . add_header ( 'Connection' , 'keep-alive' )
 Oo00OOOOO = urllib2 . urlopen ( O0o0Oo )
 O0OO00o0OO = Oo00OOOOO . read ( )
 Oo00OOOOO . close ( )
 O0OO00o0OO = '' . join ( O0OO00o0OO . splitlines ( ) )
 O0OO00o0OO = O0OO00o0OO . replace ( "Ext.data.JsonP.tvshow1205151412(" , "" )
 O0OO00o0OO = O0OO00o0OO . replace ( ")" , "" )
 I11i1 = json . loads ( O0OO00o0OO )
 return I11i1
 if 12 - 12: o0 % o0OO0 / IiIi1Iii1I1 % Oo0ooO0oo0oO
def oOooOoO0Oo0O ( ) :
 O0o0Oo = urllib2 . Request ( "http://truelife.vn/offica/tvchannel/tvshow/action?_f=17&ownerId=1532&jsoncallback=Ext.data.JsonP.tvshow1205151412" )
 O0o0Oo . add_header ( 'Host' , 'truelife.vn' )
 O0o0Oo . add_header ( 'Accept-Encoding' , 'gzip, deflate' )
 O0o0Oo . add_header ( 'Referer' , 'http://megafun.vn/tv/' )
 O0o0Oo . add_header ( 'DNT' , '1' )
 O0o0Oo . add_header ( 'Connection' , 'keep-alive' )
 Oo00OOOOO = urllib2 . urlopen ( O0o0Oo )
 O0OO00o0OO = Oo00OOOOO . read ( )
 Oo00OOOOO . close ( )
 O0OO00o0OO = '' . join ( O0OO00o0OO . splitlines ( ) )
 O0OO00o0OO = O0OO00o0OO . replace ( "Ext.data.JsonP.tvshow1205151412(" , "" )
 O0OO00o0OO = O0OO00o0OO . replace ( ")" , "" )
 I11i1 = json . loads ( O0OO00o0OO )
 return I11i1
 if 29 - 29: o0
def iI ( ) :
 O0o0Oo = urllib2 . Request ( urllib . unquote_plus ( "http://s22.ctl.vsolutions.vn/ctl/tvlive/s/?script&json" ) )
 O0o0Oo . add_header ( 'Host' , 's22.ctl.vsolutions.vn' )
 O0o0Oo . add_header ( 'Accept-Encoding' , 'gzip, deflate' )
 Oo00OOOOO = urllib2 . urlopen ( O0o0Oo )
 O0OO00o0OO = Oo00OOOOO . read ( )
 Oo00OOOOO . close ( )
 O0OO00o0OO = '' . join ( O0OO00o0OO . splitlines ( ) )
 O0OO00o0OO = O0OO00o0OO . replace ( "null(" , "" )
 O0OO00o0OO = O0OO00o0OO . replace ( ")" , "" )
 I11i1 = json . loads ( O0OO00o0OO )
 return I11i1
 if 28 - 28: o00 - I1 . I1 + o0OO0 - o0 + iiI
def ooOoo0O ( vstv , date , st ) :
 oOoOooOo0o0 = str ( int ( time . time ( ) ) )
 OOOO = base64 . b64encode ( oOoOooOo0o0 )
 OOO00 = ""
 for iiiiiIIii in range ( 1 , 7 ) :
  O000OO0 = random . randrange ( 0 , len ( "ABCDEFGHIJKLMNOPQRSTUVXYZ1234567890" ) )
  OOO00 = OOO00 + "ABCDEFGHIJKLMNOPQRSTUVXYZ1234567890" [ O000OO0 : O000OO0 + 1 ]
 I11iii1Ii = "" ;
 for I1IIiiIiii in range ( 0 , len ( OOOO ) ) :
  I11iii1Ii = I11iii1Ii + OOOO [ I1IIiiIiii : I1IIiiIiii + 1 ]
  if ( I1IIiiIiii < len ( OOO00 ) ) :
   I11iii1Ii = I11iii1Ii + OOO00 [ I1IIiiIiii : I1IIiiIiii + 1 ]
 O000oo0O = base64 . b64encode ( I11iii1Ii )
 OOOOi11i1 = ""
 for IIIii1II1II in range ( 0 , len ( O000oo0O ) - 1 ) :
  OOOOi11i1 = OOOOi11i1 + O000oo0O [ IIIii1II1II : IIIii1II1II + 1 ]
  if ( IIIii1II1II < len ( OOO00 ) ) :
   OOOOi11i1 = OOOOi11i1 + OOO00 [ IIIii1II1II : IIIii1II1II + 1 ]
 OOOOi11i1 = OOOOi11i1 . replace ( "=" , "" )
 i1I1iI = { 'location' : '' , 'device_type' : '2' , 'mf_code' : vstv , 'device_id' : '487142' , 'date' : date , 'channel_id' : '1' , 'member_id' : '107805' , 'end_time' : '2359' , 'app_v' : '63' , 'manufacturer_id' : 'E94F6043C85AF86080CA27A439A1D766' , 'start_time' : st , 'tid' : OOOOi11i1 , 'profile' : '2' }
 oo0OooOOo0 = urllib . urlencode ( i1I1iI )
 if 92 - 92: i1iIIII . Oo0oO0ooo + Oo0ooO0oo0oO
 O0o0Oo = urllib2 . Request ( urllib . unquote_plus ( IIiiIiI1 ( "u" , "3enp5a-kpOTp6aPi7unr49rpo-vjpOuqpNjd1uPj2uGk4uTX3uHapOnr5Nmi6ufh" ) ) )
 O0o0Oo . add_header ( 'Content-Type' , 'application/x-www-form-urlencoded; charset=utf-8' )
 O0o0Oo . add_header ( 'User-Agent' , 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; Nexus 5 Build/KOT49H)' )
 O0o0Oo . add_header ( 'Host' , 'ott.mytvnet.vn' )
 O0o0Oo . add_header ( 'Connection' , 'Keep-Alive' )
 O0o0Oo . add_header ( 'Accept-Encoding' , 'gzip' )
 Oo00OOOOO = urllib2 . urlopen ( O0o0Oo , oo0OooOOo0 )
 O0OO00o0OO = Oo00OOOOO . read ( )
 Oo00OOOOO . close ( )
 O0OO00o0OO = '' . join ( O0OO00o0OO . splitlines ( ) )
 O0OO00o0OO = O0OO00o0OO . replace ( "null(" , "" )
 O0OO00o0OO = O0OO00o0OO . replace ( ")" , "" )
 I11i1 = json . loads ( O0OO00o0OO )
 O0OO00o0OO = I11i1 [ 'data' ] [ 'url' ]
 return O0OO00o0OO
 if 28 - 28: i1 * I11iIi1I - Oo0ooO0oo0oO * I1 * O0o / IiiIII111iI
def OooO0 ( vstv ) :
 O0o0Oo = urllib2 . Request ( urllib . unquote_plus ( "http://truelife.vn/offica/resourcesubcription/action?_f=6666&c=%s&q=high&type=tv" ) % ( vstv ) )
 O0o0Oo . add_header ( 'Host' , 'truelife.vn' )
 O0o0Oo . add_header ( 'Accept-Encoding' , 'gzip, deflate' )
 O0o0Oo . add_header ( 'Cookie' , 'ojid="dspsns19Lgzd0JHP2kJt|qI9iwnktcCR7lIlfhJM8vYlsqnyhQ7Xlmh2Mfm0jf4cm0ly8DMtoNkb4LIJysPDFP0/cuXcCXjTYxsofpWHjNJFo6hcah5xggY/g4xS7Avl24d4WcPzYgzRd79ETkW2RrzizZBjeNk7hihYpWYbyc/z2Q1jL/Q6kpw0u92OERt0BaxPHC8j|vYqOE2Pnd/h2DdkurOJPoJEi4Ia9KiV3Qs="' )
 O0o0Oo . add_header ( 'User-Agent' , 'Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53' )
 Oo00OOOOO = urllib2 . urlopen ( O0o0Oo )
 O0OO00o0OO = Oo00OOOOO . read ( )
 Oo00OOOOO . close ( )
 O0OO00o0OO = '' . join ( O0OO00o0OO . splitlines ( ) )
 O0OO00o0OO = O0OO00o0OO . replace ( "null(" , "" )
 O0OO00o0OO = O0OO00o0OO . replace ( ")" , "" )
 I11i1 = json . loads ( O0OO00o0OO )
 OooO0OoOOOO = I11i1 [ "object" ] [ 0 ] [ "token" ]
 i1Ii = I11i1 [ "object" ] [ 0 ] [ "time" ]
 o00OO00OoO = iI ( ) [ "cdn" ] [ "server" ]
 O0OO00o0OO = 'http://m3.mytvnet.vn/ilive.m3u8?c=' + vstv + '&q=high&token=' + OooO0OoOOOO + '&time=' + i1Ii
 return O0OO00o0OO
 if 60 - 60: IiiIII111iI * o0OO0 - IiiIII111iI % o0 - IiIi1Iii1I1 + OOooOOo
def O00Oo000ooO0 ( url ) :
 O0OO00o0OO = ""
 if os . path . exists ( url ) == True :
  O0OO00o0OO = open ( url ) . read ( )
 else :
  O0o0Oo = urllib2 . Request ( url )
  O0o0Oo . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
  Oo00OOOOO = urllib2 . urlopen ( O0o0Oo )
  O0OO00o0OO = Oo00OOOOO . read ( )
  Oo00OOOOO . close ( )
 O0OO00o0OO = '' . join ( O0OO00o0OO . splitlines ( ) ) . replace ( '\'' , '"' )
 O0OO00o0OO = O0OO00o0OO . replace ( '\n' , '' )
 O0OO00o0OO = O0OO00o0OO . replace ( '\t' , '' )
 O0OO00o0OO = re . sub ( '  +' , ' ' , O0OO00o0OO )
 O0OO00o0OO = O0OO00o0OO . replace ( '> <' , '><' )
 return O0OO00o0OO
 if 100 - 100: iiI + I1 - o00 + i11iIiiIii * O0o
def IIiiIiI1 ( k , e ) :
 iII = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for o0ooOooo000oOO in range ( len ( e ) ) :
  Oo0oOOo = k [ o0ooOooo000oOO % len ( k ) ]
  Oo0OoO00oOO0o = chr ( ( 256 + ord ( e [ o0ooOooo000oOO ] ) - ord ( Oo0oOOo ) ) % 256 )
  iII . append ( Oo0OoO00oOO0o )
 return "" . join ( iII )
 if 80 - 80: o00ooo0 + o00 - o00 % i1iIIII
def oOo0oooo00o ( name , channelid , mode , starttime , duration ) :
 OoOO0oo0o = sys . argv [ 0 ] + "?name=" + urllib . quote_plus ( name ) + "&channelid=" + urllib . quote_plus ( str ( channelid ) ) + "&mode=" + str ( mode ) + "&starttime=" + urllib . quote_plus ( starttime ) + "&duration=" + str ( duration )
 II11i1I11Ii1i = True
 O000O0oOO0 = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = '' )
 O000O0oOO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 II11i1I11Ii1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoOO0oo0o , listitem = O000O0oOO0 )
 return II11i1I11Ii1i
 if 68 - 68: I1Ii % i1 . I1 . I1i1iI1i
def Oo ( name , channelid , channelimg , mode ) :
 OoOO0oo0o = sys . argv [ 0 ] + "?name=" + urllib . quote_plus ( name ) + "&channelid=" + urllib . quote_plus ( str ( channelid ) ) + "&mode=" + str ( mode )
 II11i1I11Ii1i = True
 O000O0oOO0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = channelimg )
 O000O0oOO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 II11i1I11Ii1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoOO0oo0o , listitem = O000O0oOO0 , isFolder = True )
 return II11i1I11Ii1i
 if 92 - 92: i1iIIII . I1Ii
def i1i ( parameters ) :
 iiI111I1iIiI = { }
 if 41 - 41: I11iIi1I . IiIi1Iii1I1 + iiI * Oo0ooO0oo0oO % I11iIi1I * I11iIi1I
 if parameters :
  iIIIIi1iiIi1 = parameters [ 1 : ] . split ( "&" )
  for iii1i1iiiiIi in iIIIIi1iiIi1 :
   Iiii = iii1i1iiiiIi . split ( '=' )
   if ( len ( Iiii ) ) == 2 :
    iiI111I1iIiI [ Iiii [ 0 ] ] = Iiii [ 1 ]
 return iiI111I1iIiI
 if 75 - 75: o0OO0 % Oo0ooO0oo0oO % Oo0ooO0oo0oO . I1Ii
III1iII1I1ii = xbmc . translatePath ( Oo0Ooo . getAddonInfo ( 'profile' ) )
if 61 - 61: ii1IiI1i
if os . path . exists ( III1iII1I1ii ) == False :
 os . mkdir ( III1iII1I1ii )
O0OOO = os . path . join ( III1iII1I1ii , 'visitor' )
if 10 - 10: o00 * Oo0oO0ooo % o0OO0 / OOooOOo / o0OO0
if os . path . exists ( O0OOO ) == False :
 from random import randint
 iIIi1i1 = open ( O0OOO , "w" )
 iIIi1i1 . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 iIIi1i1 . close ( )
 if 10 - 10: Oo0oO0ooo
def OOooOO000 ( utm_url ) :
 OOoOoo = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  O0o0Oo = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : OOoOoo }
 )
  Oo00OOOOO = urllib2 . urlopen ( O0o0Oo ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return Oo00OOOOO
 if 85 - 85: I1i1iI1i % i1iIIII % IiIi1Iii1I1
def Oo00oo0oO ( group , name ) :
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
  IIiIi1iI = "1.0"
  i1IiiiI1iI = open ( O0OOO ) . read ( )
  i1iIi = "Megafun"
  ooOOoooooo = "UA-52209804-2"
  II1I = "www.viettv24.com"
  O0 = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   i1II1Iiii1I11 = O0 + "?" + "utmwv=" + IIiIi1iI + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( i1iIi ) + "&utmac=" + ooOOoooooo + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , i1IiiiI1iI , "1" , "1" , "2" ] )
   if 9 - 9: I1i1iI1i / I11iIi1I - OOooOOo / o0 / ii1I - Oo0ooO0oo0oO
   if 91 - 91: i1iIIII % i1 % ii1I
   if 20 - 20: o00 % O0o / O0o + O0o
   if 45 - 45: o00ooo0 - I1 - o0 - IiiIII111iI . ii1IiI1i / iiI
   if 51 - 51: iiI + i1iIIII
  else :
   if group == "None" :
    i1II1Iiii1I11 = O0 + "?" + "utmwv=" + IIiIi1iI + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( i1iIi + "/" + name ) + "&utmac=" + ooOOoooooo + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , i1IiiiI1iI , "1" , "1" , "2" ] )
    if 8 - 8: o00ooo0 * o0OO0 - O0o - IiiIII111iI * o00 % OOooOOo
    if 48 - 48: iiI
    if 11 - 11: Oo0oO0ooo + o0 - IiiIII111iI / Oo0ooO0oo0oO + I11iIi1I . ii1IiI1i
    if 41 - 41: O0o - iiI - iiI
    if 68 - 68: o00 % I1Ii
   else :
    i1II1Iiii1I11 = O0 + "?" + "utmwv=" + IIiIi1iI + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( i1iIi + "/" + group + "/" + name ) + "&utmac=" + ooOOoooooo + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , i1IiiiI1iI , "1" , "1" , "2" ] )
    if 88 - 88: ii1I - IiIi1Iii1I1 + o00
    if 40 - 40: OOooOOo * O0o + o00 % i1iIIII
    if 74 - 74: o00ooo0 - I11iIi1I + o0 + I1Ii / o0OO0
    if 23 - 23: iiI
    if 85 - 85: O0o
    if 84 - 84: OOooOOo . ii1I % o0 + O0o % o0 % IiiIII111iI
  print "============================ POSTING ANALYTICS ============================"
  OOooOO000 ( i1II1Iiii1I11 )
  if 42 - 42: IiiIII111iI / Oo0oO0ooo / Oo0ooO0oo0oO + i1iIIII / o0OO0
  if not group == "None" :
   o0OoOO000ooO0 = O0 + "?" + "utmwv=" + IIiIi1iI + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( II1I ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + i1iIi + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( i1iIi ) + "&utmac=" + ooOOoooooo + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , i1IiiiI1iI , "1" , "2" ] )
   if 56 - 56: i1iIIII
   if 86 - 86: ii1IiI1i % I1Ii
   if 15 - 15: i1 * OOooOOo + i11iIiiIii
   if 6 - 6: IiIi1Iii1I1 / i11iIiiIii + i1iIIII * o00ooo0
   if 80 - 80: ii1IiI1i
   if 83 - 83: Oo0oO0ooo . i11iIiiIii + ii1IiI1i . Oo0ooO0oo0oO * Oo0oO0ooo
   if 53 - 53: ii1IiI1i
   if 31 - 31: IiiIII111iI
   try :
    print "============================ POSTING TRACK EVENT ============================"
    OOooOO000 ( o0OoOO000ooO0 )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 80 - 80: I1Ii . i11iIiiIii - Oo0ooO0oo0oO
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 25 - 25: IiiIII111iI
oOo0oO = i1i ( sys . argv [ 2 ] )
OOOO0oo0 = oOo0oO . get ( 'mode' )
I11iiI1i1 = oOo0oO . get ( 'channelid' )
I1i1Iiiii = oOo0oO . get ( 'name' )
OOo0oO00ooO00 = oOo0oO . get ( 'starttime' )
oOO0O00oO0Ooo = oOo0oO . get ( 'duration' )
if 67 - 67: IiiIII111iI - o00
if type ( OOo0oO00ooO00 ) == type ( str ( ) ) :
 OOo0oO00ooO00 = urllib . unquote_plus ( OOo0oO00ooO00 )
if type ( I11iiI1i1 ) == type ( str ( ) ) :
 I11iiI1i1 = urllib . unquote_plus ( I11iiI1i1 )
if type ( I1i1Iiiii ) == type ( str ( ) ) :
 I1i1Iiiii = urllib . unquote_plus ( I1i1Iiiii )
 if 36 - 36: I1
I11iI = str ( sys . argv [ 1 ] )
if OOOO0oo0 == 'channelprogram' :
 Oo00oo0oO ( "Browse" , I1i1Iiiii )
 o0oOoO00o ( I11iiI1i1 )
elif OOOO0oo0 == 'playvideo' :
 Oo00oo0oO ( "Play" , I1i1Iiiii + "/" + I11iiI1i1 )
 I1iI1ii1II = xbmcgui . DialogProgress ( )
 I1iI1ii1II . create ( 'megafun.vn' , 'Loading video. Please wait...' )
 O00OooO0 ( I11iiI1i1 , OOo0oO00ooO00 , oOO0O00oO0Ooo )
 I1iI1ii1II . close ( )
 del I1iI1ii1II
else :
 Oo00oo0oO ( "None" , "None" )
 ooO0OO000o ( )
xbmcplugin . endOfDirectory ( int ( I11iI ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
