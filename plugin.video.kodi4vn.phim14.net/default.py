#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib , urllib2 , re , zlib , ast , os , uuid
from xbmcswift2 import Plugin , xbmc , xbmcgui , xbmcaddon
oo000 = Plugin ( )
ii = "plugin://plugin.video.kodi4vn.phim14.net"
oOOo = 32
if 59 - 59: Oo0Ooo . OO0OO0O0O0 * iiiIIii1IIi . iII111iiiii11 % I1IiiI
@ oo000 . route ( '/' )
def IIi1IiiiI1Ii ( ) :
 I11i11Ii = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 I11i11Ii = xbmc . translatePath ( os . path . join ( I11i11Ii , "temp.jpg" ) )
 urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/phim14.jpg' , I11i11Ii )
 oO00oOo = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , I11i11Ii )
 OOOo0 = xbmcgui . WindowDialog ( )
 OOOo0 . addControl ( oO00oOo )
 #OOOo0 . doModal ( )
 if 54 - 54: i1 - o0 * i1oOo0OoO * iIIIiiIIiiiIi % Oo
 o0O = [
 { 'label' : 'Phim mới' , 'path' : '%s/latest/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/danh-sach/phim-moi/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim lẻ' , 'path' : '%s/movies/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/danh-sach/phim-le/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim bộ' , 'path' : '%s/series/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/danh-sach/phim-bo/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Theo thể loại' , 'path' : '%s/genres' % ii } ,
 { 'label' : 'Theo Quốc gia' , 'path' : '%s/nations' % ii } ,
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
@ oo000 . route ( '/movies/<murl>/<page>' )
def o0oOoO00o ( murl , page ) :
 o0O = i1ii1iIII ( murl , page , 'movies' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( o0O )
 if 43 - 43: O0OOo . OO0OO0O0O0
@ oo000 . route ( '/series/<murl>/<page>' )
def O0Oooo00 ( murl , page ) :
 o0O = i1ii1iIII ( murl , page , 'series' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( o0O )
 if 87 - 87: I1IiiI / II1i . iIIIiiIIiiiIi * iII111iiiii11 - o00 * O0OOo
@ oo000 . route ( '/genres' )
def O0 ( ) :
 o0O = [
 { 'label' : 'Hành Động' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-hanh-dong/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phiêu Lưu' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-phieu-luu/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Kinh Dị' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-kinh-di/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Tình Cảm' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-tinh-cam/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Hoạt Hình' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-hoat-hinh/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Võ Thuật' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-vo-thuat/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Hài Hước' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-hai-huoc/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Hình Sự' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-hinh-su/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Tâm Lý' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-tam-ly/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Viễn Tưởng' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-vien-tuong/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Thần Thoại' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-than-thoai/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Cổ trang' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-co-trang/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Chiến Tranh' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-chien-tranh/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Âm Nhạc' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-am-nhac/page-%s.html' ) , 1 ) } ,
 { 'label' : 'TV Show' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-tv-show/page-%s.html' ) , 1 ) }
 ]
 return oo000 . finish ( o0O )
 if 34 - 34: o00 % i1 % iiiIIii1IIi % o00 * o00ooo0 / Oo
@ oo000 . route ( '/genres/<murl>/<page>' )
def Iiii ( murl , page = 1 ) :
 o0O = i1ii1iIII ( murl , page , 'genres' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( o0O )
 if 87 - 87: I1Ii111 / O0OOo + Oo0oO0ooo - O0OOo . O0OOo / i1
@ oo000 . route ( '/nations' )
def iiIIIIi1i1 ( ) :
 o0O = [
 { 'label' : 'Hàn Quốc' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/quoc-gia/phim-han-quoc/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Trung Quốc' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/quoc-gia/phim-trung-quoc/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Đài Loan' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/quoc-gia/phim-dai-loan/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Việt Nam' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/quoc-gia/phim-viet-nam/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Mỹ' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/quoc-gia/phim-my/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Nhật Bản' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/quoc-gia/phim-nhat-ban/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Thái Lan' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/quoc-gia/phim-thai-lan/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Hồng Kông' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/quoc-gia/phim-hong-kong/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Philippines' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/quoc-gia/phim-philippines/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Châu Âu' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/quoc-gia/phim-chau-au/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Nước Khác' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/quoc-gia/phim-nuoc-khac/page-%s.html' ) , 1 ) }
 ]
 return oo000 . finish ( o0O )
 if 54 - 54: ooOoO0o % OO0OO0O0O0 + o0 - o00ooo0 / o00O0oo
@ oo000 . route ( '/nations/<murl>/<page>' )
def iIiiI1 ( murl , page ) :
 o0O = i1ii1iIII ( murl , page , 'nations' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( o0O )
 if 68 - 68: o0 - Oo0Ooo - iIIIiiIIiiiIi / ooOoO0o - iIIIiiIIiiiIi + I1IiiI
@ oo000 . route ( '/search/' )
def IiiIII111ii ( ) :
 i1iIIi1 = oo000 . keyboard ( heading = 'Tìm kiếm' )
 if i1iIIi1 :
  ii11iIi1I = "http://m.phim14.net/search/keyword/page-%s.html" . replace ( "keyword" , i1iIIi1 ) . replace ( " " , "-" )
  iI111I11I1I1 = '%s/search/%s/%s' % ( ii , urllib . quote_plus ( ii11iIi1I ) , 1 )
  oo000 . redirect ( iI111I11I1I1 )
  if 55 - 55: Oo % I1IiiI / II1i - I1Ii111 - OO0OO0O0O0 / i1
@ oo000 . route ( '/search/<murl>/<page>' )
def iii11iII ( murl , page ) :
 o0O = i1ii1iIII ( murl , page , 'search' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( o0O )
 if 42 - 42: Oo0oO0ooo + IiII
@ oo000 . route ( '/mirrors/<murl>' )
def OOoO000O0OO ( murl ) :
 o0O = [ ]
 for iiI1IiI in II ( murl ) :
  ooOoOoo0O = { }
  ooOoOoo0O [ "label" ] = iiI1IiI [ "name" ] . strip ( )
  OooO0 = str ( uuid . uuid1 ( ) )
  II11iiii1Ii = oo000 . get_storage ( OooO0 )
  II11iiii1Ii [ "list" ] = iiI1IiI [ "eps" ]
  ooOoOoo0O [ "path" ] = '%s/eps/%s' % ( ii , urllib . quote_plus ( OooO0 ) )
  o0O . append ( ooOoOoo0O )
 return oo000 . finish ( o0O )
 if 70 - 70: I1Ii111 / iiiIIii1IIi % O0OOo % Oo0Ooo . o0
@ oo000 . route ( '/eps/<eps_list>' )
def O0o0Oo ( eps_list ) :
 o0O = [ ]
 for Oo00OOOOO in oo000 . get_storage ( eps_list ) [ "list" ] :
  ooOoOoo0O = { }
  ooOoOoo0O [ "label" ] = Oo00OOOOO [ "name" ] . strip ( )
  ooOoOoo0O [ "is_playable" ] = True
  ooOoOoo0O [ "path" ] = '%s/play/%s' % ( ii , urllib . quote_plus ( Oo00OOOOO [ "url" ] ) )
  o0O . append ( ooOoOoo0O )
 return oo000 . finish ( o0O )
 if 85 - 85: O0OOo . o00ooo0 - iIIIiiIIiiiIi % O0OOo % i1
@ oo000 . route ( '/play/<url>' )
def OO0o00o ( url ) :
 oOOo0oo = xbmcgui . DialogProgress ( )
 oOOo0oo . create ( 'phim14.net' , 'Loading video. Please wait...' )
 oo000 . set_resolved_url ( o0oo0o0O00OO ( url ) )
 oOOo0oo . close ( )
 del oOOo0oo
 if 80 - 80: I1IiiI
def o0oo0o0O00OO ( url ) :
 oOOO0o0o = iiI1 ( url )
 if "youtube" in oOOO0o0o :
  i11Iiii = re . compile ( '(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)' ) . findall ( oOOO0o0o )
  iI = i11Iiii [ 0 ] [ len ( i11Iiii [ 0 ] ) - 1 ] . replace ( 'v/' , '' )
  return 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % iI
 if "http://m.phim14.net/grabvideo/" in oOOO0o0o :
  I1i1I1II = re . compile ( '"(http://m.phim14.net/grabvideo/.+?)"' ) . findall ( oOOO0o0o ) [ 0 ]
  if oo000 . get_setting ( 'HQ' , bool ) :
   I1i1I1II = I1i1I1II . replace ( "/grabvideo/" , "/grabvideo720/" )
  return I1i1I1II
  if 45 - 45: Oo0oO0ooo . Oo
def i1ii1iIII ( url , page , route_name ) :
 oO = int ( page ) + 1
 oOOO0o0o = iiI1 ( url % page )
 i11Iiii = re . compile ( '<a href="(http://m.phim14.net/phim/.+?)" class="content-items"><img src="(.+?)" alt="(.+?)"[^>]*><h3>.+?</h3><h4>.+?</h4><ul[^>]*><li>Năm phát hành: (.+?)</li><li>Thể loại: .+?</li></ul><p[^>]*>Trạng thái: (.+?)</p></a>' ) . findall ( oOOO0o0o )
 o0O = [ ]
 for ii1i1I1i , o00oOO0 , oOoo , iIii11I , OOO0OOO00oo in i11Iiii :
  ooOoOoo0O = { }
  ooOoOoo0O [ "label" ] = "%s (%s)" % ( oOoo , OOO0OOO00oo )
  ooOoOoo0O [ "thumbnail" ] = o00oOO0
  ooOoOoo0O [ "info" ] = { "year" : iIii11I }
  ooOoOoo0O [ "path" ] = '%s/%s/%s' % ( ii , "mirrors" , urllib . quote_plus ( ii1i1I1i . replace ( "/phim/" , "/xem-phim/" ) ) )
  o0O . append ( ooOoOoo0O )
 if len ( o0O ) == oOOo :
  o0O . append ( { 'label' : 'Next >>' , 'path' : '%s/%s/%s/%s' % ( ii , route_name , urllib . quote_plus ( url ) , oO ) , 'thumbnail' : 'http://icons.iconarchive.com/icons/rafiqul-hassan/blogger/128/Arrow-Next-icon.png' } )
 return o0O
 if 31 - 31: i1 - ooOoO0o . Oo0oO0ooo % Oo - OO0OO0O0O0
def II ( murl ) :
 oOOO0o0o = iiI1 ( murl )
 i11Iiii = re . compile ( '<span class="svname">(.+?)</span><span class="svep">(.+?)</span>' ) . findall ( oOOO0o0o )
 iii11 = re . compile ( '<title>(.+?)</title>' ) . findall ( oOOO0o0o ) [ 0 ]
 O0oo0OO0oOOOo = [ ]
 for i1i1i11IIi , II1III in i11Iiii :
  iI1iI1I1i1I = [ ]
  for iIi11Ii1 , Ii11iII1 in re . compile ( '<a[^>]*href="(.+?)"[^>]*>(.+?)</a>' ) . findall ( II1III ) :
   Oo00OOOOO = { }
   Oo00OOOOO [ "url" ] = iIi11Ii1
   Oo00OOOOO [ "name" ] = "Part %s - %s" % ( Ii11iII1 , iii11 . split ( " | " ) [ 0 ] )
   iI1iI1I1i1I . append ( Oo00OOOOO )
  iiI1IiI = { }
  iiI1IiI [ "name" ] = i1i1i11IIi
  iiI1IiI [ "eps" ] = iI1iI1I1i1I
  O0oo0OO0oOOOo . append ( iiI1IiI )
 return O0oo0OO0oOOOo
 if 51 - 51: i1 * iIIIiiIIiiiIi % iII111i * i1 % IiII / O0OOo
@ oo000 . cached ( TTL = 60 )
def iiI1 ( url ) :
 iIIIIii1 = urllib2 . Request ( url )
 iIIIIii1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1_1 like Mac OS X; da-dk) AppleWebKit/534.46.0 (KHTML, like Gecko) CriOS/19.0.1084.60 Mobile/9B206 Safari/7534.48.3' )
 iIIIIii1 . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' )
 iIIIIii1 . add_header ( 'Accept-Encoding' , 'gzip, deflate, sdch' )
 iIIIIii1 . add_header ( 'Cookie' , 'location.href=1' )
 oo000OO00Oo = urllib2 . urlopen ( iIIIIii1 )
 O0OOO0OOoO0O = oo000OO00Oo . read ( )
 oo000OO00Oo . close ( )
 if "gzip" in oo000OO00Oo . info ( ) . getheader ( 'Content-Encoding' ) :
  O0OOO0OOoO0O = zlib . decompress ( O0OOO0OOoO0O , 16 + zlib . MAX_WBITS )
 O0OOO0OOoO0O = '' . join ( O0OOO0OOoO0O . splitlines ( ) ) . replace ( '\'' , '"' )
 O0OOO0OOoO0O = O0OOO0OOoO0O . replace ( '\n' , '' )
 O0OOO0OOoO0O = O0OOO0OOoO0O . replace ( '\t' , '' )
 O0OOO0OOoO0O = re . sub ( '  +' , ' ' , O0OOO0OOoO0O )
 O0OOO0OOoO0O = O0OOO0OOoO0O . replace ( '> <' , '><' )
 return O0OOO0OOoO0O
 if 70 - 70: o00 * i1oOo0OoO * o00O0oo / II1i
if __name__ == '__main__' :
 oo000 . run ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
