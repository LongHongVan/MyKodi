#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib , urllib2 , re , zlib , os , uuid , json
from xbmcswift2 import Plugin , xbmc , xbmcgui , xbmcaddon
oo000 = Plugin ( )
ii = "plugin://plugin.video.kodi4vn.phimvang.org"
oOOo = 48
if 59 - 59: Oo0Ooo . OO0OO0O0O0 * iiiIIii1IIi . iII111iiiii11 % I1IiiI
@ oo000 . route ( '/' )
def IIi1IiiiI1Ii ( ) :
 I11i11Ii = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 I11i11Ii = xbmc . translatePath ( os . path . join ( I11i11Ii , "temp.jpg" ) )
 urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/phimvang.jpg' , I11i11Ii )
 oO00oOo = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , I11i11Ii )
 OOOo0 = xbmcgui . WindowDialog ( )
 OOOo0 . addControl ( oO00oOo )
 #OOOo0 . doModal ( )
 if 54 - 54: i1 - o0 * i1oOo0OoO * iIIIiiIIiiiIi % Oo
 o0O = [
 { 'label' : 'Phim mới' , 'path' : '%s/latest/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/phim-moi/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim HOT' , 'path' : '%s/hot/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/phim-hot/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim xem nhiều' , 'path' : '%s/most_view/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/phim-xem-nhieu/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim chiếu rạp' , 'path' : '%s/cine/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/phim-chieu-rap/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim bộ' , 'path' : '%s/series/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/phim-bo/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim lẻ' , 'path' : '%s/movies/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/phim-le/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Thể loại' , 'path' : '%s/genres' % ii } ,
 { 'label' : 'Quốc gia' , 'path' : '%s/nations' % ii } ,
 { 'label' : 'Tìm kiếm' , 'path' : '%s/search' % ii }
 ]
 return oo000 . finish ( o0O )
 if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * o00O0oo
@ oo000 . route ( '/latest/<murl>/<page>' )
def O0oOO0o0 ( murl , page ) :
 o0O = i1ii1iIII ( murl , page , 'latest' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( o0O )
 if 59 - 59: II1i * o00ooo0 / o00 * Oo0oO0ooo
@ oo000 . route ( '/hot/<murl>/<page>' )
def o0oOoO00o ( murl , page ) :
 o0O = i1ii1iIII ( murl , page , 'hot' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( o0O )
 if 43 - 43: O0OOo . OO0OO0O0O0
@ oo000 . route ( '/most_view/<murl>/<page>' )
def O0Oooo00 ( murl , page ) :
 o0O = i1ii1iIII ( murl , page , 'most_view' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( o0O )
 if 87 - 87: I1IiiI / II1i . iIIIiiIIiiiIi * iII111iiiii11 - o00 * O0OOo
@ oo000 . route ( '/cine/<murl>/<page>' )
def O0 ( murl , page ) :
 o0O = i1ii1iIII ( murl , page , 'cine' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( o0O )
 if 34 - 34: o00 % i1 % iiiIIii1IIi % o00 * o00ooo0 / Oo
@ oo000 . route ( '/movies/<murl>/<page>' )
def Iiii ( murl , page ) :
 o0O = i1ii1iIII ( murl , page , 'movies' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( o0O )
 if 87 - 87: I1Ii111 / O0OOo + Oo0oO0ooo - O0OOo . O0OOo / i1
@ oo000 . route ( '/series/<murl>/<page>' )
def iiIIIIi1i1 ( murl , page ) :
 o0O = i1ii1iIII ( murl , page , 'series' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( o0O )
 if 54 - 54: ooOoO0o % OO0OO0O0O0 + o0 - o00ooo0 / o00O0oo
@ oo000 . route ( '/genres' )
def iIiiI1 ( ) :
 o0O = [
 { 'label' : 'Clip Vui' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/the-loai/clip-vui/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Hành Động' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/the-loai/hanh-dong-xa-hoi-den/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Võ Thuật - Kiếm Hiệp' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/the-loai/vo-thuat-kiem-hiep/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Tâm Lý - Tình Cảm' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/the-loai/tam-ly-tinh-cam/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Hài Hước' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/the-loai/hai-huoc/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Kinh Dị - Ma' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/the-loai/kinh-di-ma/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Phiêu Lưu' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/the-loai/phieu-luu/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Thần Thoại' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/the-loai/than-thoai/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Viễn Tưởng' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/the-loai/vien-tuong/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Hoạt Hình' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/the-loai/hoat-hinh/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Chiến Tranh' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/the-loai/chien-tranh/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Thể Thao - Âm Nhạc' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/the-loai/the-thao-am-nhac/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim Việt Nam' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/the-loai/phim-viet-nam/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim Bộ Trung Quốc' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/the-loai/phim-bo-trung-quoc/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim Bộ Đài Loan' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/the-loai/phim-bo-dai-loan/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim Bộ Hàn Quốc' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/the-loai/phim-bo-han-quoc/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Music Box' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/the-loai/music-box/trang-%s.html' ) , 1 ) }
 ]
 return oo000 . finish ( o0O )
 if 68 - 68: o0 - Oo0Ooo - iIIIiiIIiiiIi / ooOoO0o - iIIIiiIIiiiIi + I1IiiI
@ oo000 . route ( '/genres/<murl>/<page>' )
def IiiIII111ii ( murl , page = 1 ) :
 o0O = i1ii1iIII ( murl , page , 'genres' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( o0O )
 if 3 - 3: o00ooo0 + OO0OO0O0O0
@ oo000 . route ( '/nations' )
def I1Ii ( ) :
 o0O = [
 { 'label' : 'Việt Nam' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/quoc-gia/viet-nam/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Trung Quốc' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/quoc-gia/trung-quoc/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Hàn Quốc' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/quoc-gia/han-quoc/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Nhật Bản' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/quoc-gia/nhat-ban/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Mỹ - Châu Âu' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/quoc-gia/my-chau-au/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Thái Lan' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/quoc-gia/thai-lan/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Châu Á' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/quoc-gia/chau-a/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Ấn Độ' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimvang.org/quoc-gia/an-do/trang-%s.html' ) , 1 ) }
 ]
 return oo000 . finish ( o0O )
 if 66 - 66: II1i
@ oo000 . route ( '/nations/<murl>/<page>' )
def oo0Ooo0 ( murl , page ) :
 o0O = i1ii1iIII ( murl , page , 'nations' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( o0O )
 if 46 - 46: O0OOo % O0OOo - I1Ii111 * iII111i % o00ooo0
@ oo000 . route ( '/search/' )
def OOooO0OOoo ( ) :
 iIii1 = oo000 . keyboard ( heading = 'Tìm kiếm' )
 if iIii1 :
  oOOoO0 = "http://phimvang.org/tim-kiem/tat-ca/keyword/trang-%s.html" . replace ( "keyword" , iIii1 ) . replace ( " " , "-" )
  O0OoO000O0OO = '%s/search/%s/%s' % ( ii , urllib . quote_plus ( oOOoO0 ) , 1 )
  oo000 . redirect ( O0OoO000O0OO )
  if 23 - 23: Oo0Ooo + o0
@ oo000 . route ( '/search/<murl>/<page>' )
def oOo ( murl , page ) :
 o0O = i1ii1iIII ( murl , page , 'search' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( o0O )
 if 63 - 63: i1oOo0OoO
@ oo000 . route ( '/mirrors/<murl>' )
def ooOoOoo0O ( murl ) :
 o0O = [ ]
 for OooO0 in II11iiii1Ii ( murl ) :
  OO0o = { }
  OO0o [ "label" ] = OooO0 [ "name" ] . strip ( )
  Ooo = str ( uuid . uuid1 ( ) )
  O0o0Oo = oo000 . get_storage ( Ooo )
  O0o0Oo [ "list" ] = OooO0 [ "eps" ]
  OO0o [ "path" ] = '%s/eps/%s' % ( ii , urllib . quote_plus ( Ooo ) )
  o0O . append ( OO0o )
 return oo000 . finish ( o0O )
 if 78 - 78: iiiIIii1IIi - II1i * iIIIiiIIiiiIi + iII111i + o00ooo0 + o00ooo0
@ oo000 . route ( '/eps/<eps_list>' )
def I11I11i1I ( eps_list ) :
 o0O = [ ]
 for ii11i1iIII in oo000 . get_storage ( eps_list ) [ "list" ] :
  OO0o = { }
  OO0o [ "label" ] = ii11i1iIII [ "name" ] . strip ( )
  OO0o [ "is_playable" ] = True
  OO0o [ "path" ] = '%s/play/%s' % ( ii , urllib . quote_plus ( ii11i1iIII [ "url" ] ) )
  o0O . append ( OO0o )
 return oo000 . finish ( o0O )
 if 3 - 3: I1IiiI / o0 % o00O0oo * Oo0Ooo / OO0OO0O0O0 * o00O0oo
@ oo000 . route ( '/play/<url>' )
def III1ii1iII ( url ) :
 oo0oooooO0 = xbmcgui . DialogProgress ( )
 oo0oooooO0 . create ( 'PhimVang.org' , 'Loading video. Please wait...' )
 oo000 . set_resolved_url ( i11Iiii ( url ) )
 oo0oooooO0 . close ( )
 del oo0oooooO0
 if 23 - 23: iII111i . i1
def i11Iiii ( url ) :
 Oo0O0OOOoo = oOoOooOo0o0 ( url )
 if "youtube" in Oo0O0OOOoo :
  OOOO = re . compile ( '(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)' ) . findall ( Oo0O0OOOoo )
  OOO00 = OOOO [ 0 ] [ len ( OOOO [ 0 ] ) - 1 ] . replace ( 'v/' , '' )
  return 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % OOO00
 if "picasaweb" in Oo0O0OOOoo :
  iiiiiIIii = 480
  if oo000 . get_setting ( 'HQ' , bool ) : iiiiiIIii = 720
  O000OO0 = ""
  I11iii1Ii = re . compile ( '"(https://picasaweb.google.com/.+?)"' ) . findall ( Oo0O0OOOoo ) [ 0 ]
  I11iii1Ii = I11iii1Ii . replace ( "&feat=directlink" , "" ) . replace ( "feat=directlink" , "" )
  if "lh/photo" not in I11iii1Ii :
   for I1IIiiIiii , O000oo0O , OOOOi11i1 in re . compile ( 'https://picasaweb.google.com/(\d+).*?\?authkey=(.+?)#(\d+)' ) . findall ( I11iii1Ii ) :
    IIIii1II1II = "https://picasaweb.google.com/data/feed/api/user/%s/photoid/%s?authkey=%s&alt=json" % ( I1IIiiIiii , OOOOi11i1 , O000oo0O )
    i1I1iI = json . loads ( urllib2 . urlopen ( IIIii1II1II ) . read ( ) ) [ "feed" ] [ "media$group" ] [ "media$content" ]
    for oo0OooOOo0 in i1I1iI :
     if ( oo0OooOOo0 [ "type" ] == "video/mpeg4" ) and ( int ( oo0OooOOo0 [ "height" ] ) <= iiiiiIIii ) :
      O000OO0 = oo0OooOOo0 [ "url" ]
  else :
   Oo0O0OOOoo = urllib2 . urlopen ( I11iii1Ii ) . read ( )
   IIIii1II1II = re . compile ( '(https://picasaweb.google.com/data/feed/tiny/user/\d+/photoid/\d+\?alt=jsonm&gupi=.+?)"' ) . findall ( Oo0O0OOOoo ) [ 0 ]
   Oo0O0OOOoo = urllib2 . urlopen ( IIIii1II1II ) . read ( )
   i1I1iI = json . loads ( Oo0O0OOOoo ) [ "feed" ] [ "media" ] [ "content" ]
   for oo0OooOOo0 in i1I1iI :
    if ( oo0OooOOo0 [ "type" ] == "video/mpeg4" ) and ( int ( oo0OooOOo0 [ "height" ] ) <= iiiiiIIii ) :
     O000OO0 = oo0OooOOo0 [ "url" ]
  return O000OO0
  if 92 - 92: o00ooo0 . o00O0oo + iII111i
def i1ii1iIII ( url , page , route_name ) :
 IiII1I11i1I1I = int ( page ) + 1
 Oo0O0OOOoo = oOoOooOo0o0 ( url % page )
 OOOO = re . compile ( '<h2><a href="(.+?)"[^>]*><span class="poster"><img[^>]*data-original="(.+?)" alt="(.+?)"/>' ) . findall ( Oo0O0OOOoo )
 o0O = [ ]
 for oO0Oo , oOOoo0Oo , o00OO00OoO in OOOO :
  OO0o = { }
  OO0o [ "label" ] = o00OO00OoO
  OO0o [ "thumbnail" ] = oOOoo0Oo
  OO0o [ "path" ] = '%s/%s/%s' % ( ii , "mirrors" , urllib . quote_plus ( "http://phimvang.org" + oO0Oo . replace ( "/phim/" , "/xem-phim/" ) ) )
  o0O . append ( OO0o )
 if len ( o0O ) == oOOo :
  o0O . append ( { 'label' : 'Next >>' , 'path' : '%s/%s/%s/%s' % ( ii , route_name , urllib . quote_plus ( url ) , IiII1I11i1I1I ) , 'thumbnail' : 'http://icons.iconarchive.com/icons/rafiqul-hassan/blogger/128/Arrow-Next-icon.png' } )
 return o0O
 if 60 - 60: iIIIiiIIiiiIi * Oo - iIIIiiIIiiiIi % iII111iiiii11 - O0OOo + o0
def II11iiii1Ii ( murl ) :
 Oo0O0OOOoo = oOoOooOo0o0 ( murl )
 OOOO = re . compile ( '<p class="epi"><b>(.+?)</b>(.+?)</p>' ) . findall ( Oo0O0OOOoo )
 O00Oo000ooO0 = re . compile ( '<title>(.+?)</title>' ) . findall ( Oo0O0OOOoo ) [ 0 ]
 OoO0O00 = [ ]
 for IIiII , o0ooOooo000oOO in OOOO :
  Oo0oOOo = [ ]
  for Oo0OoO00oOO0o , OOO00O in re . compile ( '<a href="(.+?)"[^>]*>(.+?)</a>' ) . findall ( o0ooOooo000oOO ) :
   ii11i1iIII = { }
   ii11i1iIII [ "url" ] = "http://phimvang.org" + Oo0OoO00oOO0o
   ii11i1iIII [ "name" ] = "Part %s - %s" % ( OOO00O , O00Oo000ooO0 )
   Oo0oOOo . append ( ii11i1iIII )
  if "Xem Full" in Oo0oOOo [ 0 ] [ "name" ] : del Oo0oOOo [ 0 ]
  OooO0 = { }
  OooO0 [ "name" ] = IIiII
  OooO0 [ "eps" ] = Oo0oOOo
  OoO0O00 . append ( OooO0 )
 return OoO0O00
 if 84 - 84: I1Ii111 * iIIIiiIIiiiIi / o00O0oo - OO0OO0O0O0
@ oo000 . cached ( TTL = 60 )
def oOoOooOo0o0 ( url ) :
 IiI1 = urllib2 . Request ( url )
 IiI1 . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' )
 IiI1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36' )
 IiI1 . add_header ( 'Accept-Encoding' , 'gzip, deflate, sdch' )
 Oo0O00Oo0o0 = urllib2 . urlopen ( IiI1 )
 O00O0oOO00O00 = Oo0O00Oo0o0 . read ( )
 Oo0O00Oo0o0 . close ( )
 if "gzip" in Oo0O00Oo0o0 . info ( ) . getheader ( 'Content-Encoding' ) :
  O00O0oOO00O00 = zlib . decompress ( O00O0oOO00O00 , 16 + zlib . MAX_WBITS )
 O00O0oOO00O00 = '' . join ( O00O0oOO00O00 . splitlines ( ) ) . replace ( '\'' , '"' )
 O00O0oOO00O00 = O00O0oOO00O00 . replace ( '\n' , '' )
 O00O0oOO00O00 = O00O0oOO00O00 . replace ( '\t' , '' )
 O00O0oOO00O00 = re . sub ( '  +' , ' ' , O00O0oOO00O00 )
 O00O0oOO00O00 = O00O0oOO00O00 . replace ( '> <' , '><' )
 return O00O0oOO00O00
 if 11 - 11: o00 . IiII
if __name__ == '__main__' :
 oo000 . run ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
