#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib , urllib2 , re , zlib , os
from xbmcswift2 import Plugin , xbmc , xbmcgui , xbmcaddon
from operator import itemgetter
oo000 = Plugin ( )
ii = "plugin://plugin.video.kodi4vn.anhtrang.org"
oOOo = 24
if 59 - 59: Oo0Ooo . OO0OO0O0O0 * iiiIIii1IIi . iII111iiiii11 % I1IiiI
@ oo000 . route ( '/' )
def IIi1IiiiI1Ii ( ) :
 I11i11Ii = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 I11i11Ii = xbmc . translatePath ( os . path . join ( I11i11Ii , "temp.jpg" ) )
 urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/anhtrang.jpg' , I11i11Ii )
 oO00oOo = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , I11i11Ii )
 OOOo0 = xbmcgui . WindowDialog ( )
 OOOo0 . addControl ( oO00oOo )
 #OOOo0 . doModal ( )
 if 54 - 54: i1 - o0 * i1oOo0OoO * iIIIiiIIiiiIi % Oo
 o0O = [
 { 'label' : 'Phim mới' , 'path' : '%s/latest/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/danh-sach/new/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim HD' , 'path' : '%s/hd/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/danh-sach/phim-hd/trang-%s.html' ) , 1 ) } ,
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
@ oo000 . route ( '/hd/<murl>/<page>' )
def o0oOoO00o ( murl , page ) :
 o0O = i1ii1iIII ( murl , page , 'hd' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( o0O )
 if 43 - 43: O0OOo . OO0OO0O0O0
@ oo000 . route ( '/genres' )
def O0Oooo00 ( ) :
 o0O = [
 { 'label' : 'Hài Hước' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/hai-huoc-1/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Hành Động' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/hanh-dong-2/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Võ Thuật' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/vo-thuat-8/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Viễn Tưởng' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/vien-tuong-3/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Tâm Lý - Tình Cảm' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/tam-ly-tinh-cam-4/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Kinh Dị' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/kinh-di-5/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Hoạt Hình' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/hoat-hinh-6/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Chiến Tranh' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/chien-tranh-13/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Thể Thao - Âm Nhạc' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/the-thao-am-nhac-12/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Hình Sự' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/hinh-su-15/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Phiêu Lưu' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/phieu-luu-14/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Cổ Trang' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/co-trang-16/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Tư Liệu - Lịch Sử' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/tu-lieu-lich-su-11/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Hài kịch - Clip hài' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/hai-kich-clip-hai-10/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Kinh Điển' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/kinh-dien-7/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Sân Khấu - Cải Lương' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/san-khau-cai-luong-9/trang-%s.html' ) , 1 ) }
 ]
 return oo000 . finish ( o0O )
 if 87 - 87: I1IiiI / II1i . iIIIiiIIiiiIi * iII111iiiii11 - o00 * O0OOo
@ oo000 . route ( '/genres/<murl>/<page>' )
def O0 ( murl , page = 1 ) :
 o0O = i1ii1iIII ( murl , page , 'genres' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( o0O )
 if 34 - 34: o00 % i1 % iiiIIii1IIi % o00 * o00ooo0 / Oo
@ oo000 . route ( '/nations' )
def Iiii ( ) :
 o0O = [
 { 'label' : 'Việt Nam' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/quoc-gia/viet-nam-3/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Trung Quốc' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/quoc-gia/trung-quoc-4/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Hàn Quốc' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/quoc-gia/han-quoc-5/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Nhật Bản' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/quoc-gia/nhat-ban-6/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Mỹ - Châu Âu' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/quoc-gia/my-chau-au-7/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Châu Á' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/quoc-gia/chau-a-8/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Ấn Độ' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/quoc-gia/an-do-9/trang-%s.html' ) , 1 ) }
 ]
 return oo000 . finish ( o0O )
 if 87 - 87: I1Ii111 / O0OOo + Oo0oO0ooo - O0OOo . O0OOo / i1
@ oo000 . route ( '/nations/<murl>/<page>' )
def iiIIIIi1i1 ( murl , page ) :
 o0O = i1ii1iIII ( murl , page , 'nations' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( o0O )
 if 54 - 54: ooOoO0o % OO0OO0O0O0 + o0 - o00ooo0 / o00O0oo
@ oo000 . route ( '/search/' )
def iIiiI1 ( ) :
 OoOooOOOO = oo000 . keyboard ( heading = 'Tìm kiếm' )
 if OoOooOOOO :
  i11iiII = "http://phim.anhtrang.org/tim-kiem/keyword/1/trang-%s.html" . replace ( "keyword" , OoOooOOOO ) . replace ( " " , "-" )
  I1iiiiI1iII = '%s/search/%s/%s' % ( ii , urllib . quote_plus ( i11iiII ) , 1 )
  oo000 . redirect ( I1iiiiI1iII )
  if 20 - 20: I1IiiI + Oo0Ooo - II1i % iIIIiiIIiiiIi . iII111iiiii11
@ oo000 . route ( '/search/<murl>/<page>' )
def Ooo00O00O0O0O ( murl , page ) :
 o0O = i1ii1iIII ( murl , page , 'search' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( o0O )
 if 90 - 90: i1 + I1Ii111 / iII111i % i1 - OO0OO0O0O0
@ oo000 . route ( '/mirrors/<murl>' )
def iIii1 ( murl ) :
 o0O = [ ]
 for oOOoO0 in O0OoO000O0OO ( murl ) :
  iiI1IiI = { }
  iiI1IiI [ "label" ] = oOOoO0 [ "name" ] . strip ( ": " )
  iiI1IiI [ "path" ] = '%s/eps/%s' % ( ii , urllib . quote_plus ( oOOoO0 [ "eps" ] ) )
  o0O . append ( iiI1IiI )
 return oo000 . finish ( o0O )
 if 13 - 13: i1oOo0OoO . Oo0Ooo - iiiIIii1IIi - Oo
@ oo000 . route ( '/eps/<eps_list>' )
def ii1I ( eps_list ) :
 OooO0 = II11iiii1Ii ( eps_list )
 OO0o = re . compile ( '&file=/xml.php\?id=(\d+)' ) . findall ( OooO0 ) [ 0 ]
 OooO0 = II11iiii1Ii ( "http://phim.anhtrang.org/xml.php?id=%s" % OO0o )
 Ooo = re . compile ( "<item><title>(.+?)</title>" ) . findall ( OooO0 ) [ 0 ]
 o0O = [ ]
 for O0o0Oo in re . compile ( '<item>(.+?)</item>' ) . findall ( OooO0 ) :
  Oo00OOOOO = re . compile ( "(\w+)-\w+.html" ) . findall ( O0o0Oo ) [ 0 ]
  iiI1IiI = { }
  if Oo00OOOOO . isdigit ( ) :
   iiI1IiI [ "label" ] = "Part %03d - %s" % ( int ( Oo00OOOOO ) , Ooo )
  else :
   O0O = re . split ( "(\d+)" , Oo00OOOOO . strip ( ) )
   if len ( O0O ) > 1 :
    iiI1IiI [ "label" ] = "Part %03d%s - %s" % ( int ( O0O [ 1 ] ) , O0O [ 2 ] , Ooo )
   else :
    iiI1IiI [ "label" ] = "Part %s - %s" % ( O0O [ 0 ] , Ooo )
    if 83 - 83: o00O0oo + i1 * iII111i % iIIIiiIIiiiIi + o00O0oo
  iiI1IiI [ "is_playable" ] = True
  I1iiiiI1iII = re . compile ( "<jwplayer:[h]*[d]*[.]*file\d*>(.+?)</jwplayer:[h]*[d]*[.]*file\d*>" ) . findall ( O0o0Oo )
  if oo000 . get_setting ( 'HQ' , bool ) :
   iiI1IiI [ "path" ] = '%s/play/%s' % ( ii , urllib . quote_plus ( I1iiiiI1iII [ - 1 ] ) )
  else :
   iiI1IiI [ "path" ] = '%s/play/%s' % ( ii , urllib . quote_plus ( I1iiiiI1iII [ 0 ] ) )
  o0O . append ( iiI1IiI )
 o0O = sorted ( o0O , key = itemgetter ( 'label' ) )
 return oo000 . finish ( o0O )
 if 27 - 27: OO0OO0O0O0 % I1IiiI * I1Ii111 + Oo0Ooo + iII111iiiii11 * I1IiiI
@ oo000 . route ( '/play/<url>' )
def o0oo0o0O00OO ( url ) :
 o0oO = xbmcgui . DialogProgress ( )
 o0oO . create ( 'AnhTrang.org' , 'Loading video. Please wait...' )
 oo000 . set_resolved_url ( I1i1iii ( url ) )
 o0oO . close ( )
 del o0oO
 if 20 - 20: iII111i
def I1i1iii ( url ) :
 if "youtube" in url :
  OO0o = re . compile ( '(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)' ) . findall ( url )
  oO00 = OO0o [ 0 ] [ len ( OO0o [ 0 ] ) - 1 ] . replace ( 'v/' , '' )
  return 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % oO00
 if "picasa" in url :
  return url
  if 53 - 53: iII111iiiii11 . I1IiiI
def i1ii1iIII ( url , page , route_name ) :
 ii1I1i1I = int ( page ) + 1
 OooO0 = II11iiii1Ii ( url % page )
 OO0o = re . compile ( '<div class="poster">(.*?)<a href="(.+?)" title="(.+?)"><img src="(.+?)"[^>]*/>' ) . findall ( OooO0 )
 o0O = [ ]
 for OOoo0O0 , iiiIi1i1I , Ooo , oOO00oOO in OO0o :
  iiI1IiI = { }
  iiI1IiI [ "label" ] = "%s (%s)" % ( Ooo , OOoo0O0 . replace ( '<span class="process"><span>' , "" ) . replace ( "</span></span>" , "" ) )
  iiI1IiI [ "thumbnail" ] = oOO00oOO . replace ( "http://" , "https://" )
  iiI1IiI [ "path" ] = '%s/%s/%s' % ( ii , "mirrors" , urllib . quote_plus ( iiiIi1i1I ) )
  o0O . append ( iiI1IiI )
 if len ( o0O ) == oOOo :
  o0O . append ( { 'label' : 'Next >>' , 'path' : '%s/%s/%s/%s' % ( ii , route_name , urllib . quote_plus ( url ) , ii1I1i1I ) , 'thumbnail' : 'http://icons.iconarchive.com/icons/rafiqul-hassan/blogger/128/Arrow-Next-icon.png' } )
 return o0O
 if 75 - 75: I1IiiI / iII111iiiii11 - OO0OO0O0O0 / Oo . i1 - I1IiiI
def O0OoO000O0OO ( murl ) :
 OooO0 = II11iiii1Ii ( murl )
 OO0o = re . compile ( '<p><a href="(.+?)" class="watch_now">XEM PHIM</a>' ) . findall ( OooO0 )
 OooO0 = II11iiii1Ii ( OO0o [ 0 ] )
 OO0o = re . compile ( '<tr class="listserver"><td valign="top" class="name">(.+?)</td>(.+?)</tr>' ) . findall ( OooO0 )
 O000OO0 = [ ]
 for I11iii1Ii , I1IIiiIiii in OO0o :
  O000oo0O = re . compile ( '<a href="(.+?)">' ) . findall ( I1IIiiIiii ) [ 0 ]
  oOOoO0 = { }
  oOOoO0 [ "name" ] = I11iii1Ii
  oOOoO0 [ "eps" ] = O000oo0O
  O000OO0 . append ( oOOoO0 )
 return O000OO0
 if 66 - 66: IiII / Oo - o0 . ooOoO0o / o0 * ooOoO0o
@ oo000 . cached ( TTL = 60 )
def II11iiii1Ii ( url ) :
 IIIii1II1II = urllib2 . Request ( url )
 IIIii1II1II . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' )
 IIIii1II1II . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36' )
 IIIii1II1II . add_header ( 'Accept-Encoding' , 'gzip, deflate, sdch' )
 i1I1iI = urllib2 . urlopen ( IIIii1II1II )
 oo0OooOOo0 = i1I1iI . read ( )
 i1I1iI . close ( )
 if "gzip" in i1I1iI . info ( ) . getheader ( 'Content-Encoding' ) :
  oo0OooOOo0 = zlib . decompress ( oo0OooOOo0 , 16 + zlib . MAX_WBITS )
 oo0OooOOo0 = '' . join ( oo0OooOOo0 . splitlines ( ) ) . replace ( '\'' , '"' )
 oo0OooOOo0 = oo0OooOOo0 . replace ( '\n' , '' )
 oo0OooOOo0 = oo0OooOOo0 . replace ( '\t' , '' )
 oo0OooOOo0 = re . sub ( '  +' , ' ' , oo0OooOOo0 )
 oo0OooOOo0 = oo0OooOOo0 . replace ( '> <' , '><' )
 return oo0OooOOo0
 if 92 - 92: o00ooo0 . o00O0oo + iII111i
if __name__ == '__main__' :
 oo000 . run ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
