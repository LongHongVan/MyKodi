#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib , urllib2 , re , zlib , os , uuid , json
from xbmcswift2 import Plugin , xbmc , xbmcgui , xbmcaddon
oo000 = Plugin ( )
ii = "plugin://plugin.video.kodi4vn.phim60s"
oOOo = 10
if 59 - 59: Oo0Ooo . OO0OO0O0O0 * iiiIIii1IIi . iII111iiiii11 % I1IiiI
@ oo000 . route ( '/' )
def IIi1IiiiI1Ii ( ) :
 I11i11Ii = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 I11i11Ii = xbmc . translatePath ( os . path . join ( I11i11Ii , "temp.jpg" ) )
 urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/phim60s.jpg' , I11i11Ii )
 oO00oOo = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , I11i11Ii )
 OOOo0 = xbmcgui . WindowDialog ( )
 OOOo0 . addControl ( oO00oOo )
 #OOOo0 . doModal ( )
 if 54 - 54: i1 - o0 * i1oOo0OoO * iIIIiiIIiiiIi % Oo
 o0O = [
 { 'label' : 'Phim mới' , 'path' : '%s/latest/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/film-new.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Phim hot' , 'path' : '%s/hottest/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/film-hot.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Phim lẻ' , 'path' : '%s/movies/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/film-le.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Phim bộ' , 'path' : '%s/series/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/film-bo.html?p=%s' ) , 1 ) } ,
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
@ oo000 . route ( '/hottest/<murl>/<page>' )
def o0oOoO00o ( murl , page ) :
 o0O = i1ii1iIII ( murl , page , 'hottest' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( o0O )
 if 43 - 43: O0OOo . OO0OO0O0O0
@ oo000 . route ( '/movies/<murl>/<page>' )
def O0Oooo00 ( murl , page ) :
 o0O = i1ii1iIII ( murl , page , 'movies' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( o0O )
 if 87 - 87: I1IiiI / II1i . iIIIiiIIiiiIi * iII111iiiii11 - o00 * O0OOo
@ oo000 . route ( '/series/<murl>/<page>' )
def O0 ( murl , page ) :
 o0O = i1ii1iIII ( murl , page , 'series' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( o0O )
 if 34 - 34: o00 % i1 % iiiIIii1IIi % o00 * o00ooo0 / Oo
@ oo000 . route ( '/genres' )
def Iiii ( ) :
 o0O = [
 { 'label' : 'Hành Động' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/hanh-dong-1.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Võ Thuật' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/vo-thuat-2.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Chiến Tranh' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/chien-tranh-3.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Hình Sự' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/hinh-su-4.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Hoạt Hình' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/hoat-hinh-5.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Kinh Dị & Ma' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/kinh-di-ma-6.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Hài Hước' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/hai-huoc-7.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Viễn Tưởng' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/vien-tuong-8.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Phiêu Lưu' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/phieu-luu-9.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Thần Thoại' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/than-thoai-10.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Truyền Hình' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/truyen-hinh-11.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Cổ Trang' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/co-trang-12.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Tâm Lý' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/tam-ly-16.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Gia Đình' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/gia-dinh-15.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Tình Cảm' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/tinh-cam-17.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Thể Thao' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/the-thao-18.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Âm Nhạc' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/am-nhac-19.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Tài Liệu' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/tai-lieu-20.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Tiểu Sử' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/tieu-su-29.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Bí Ẩn' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/bi-an-23.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Giật Gân' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/giat-gan-24.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Lịch Sử' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/lich-su-25.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Viễn Tây' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/category/vien-tay-30.html?p=%s' ) , 1 ) }
 ]
 return oo000 . finish ( o0O )
 if 87 - 87: I1Ii111 / O0OOo + Oo0oO0ooo - O0OOo . O0OOo / i1
@ oo000 . route ( '/genres/<murl>/<page>' )
def iiIIIIi1i1 ( murl , page = 1 ) :
 o0O = i1ii1iIII ( murl , page , 'genres' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( o0O )
 if 54 - 54: ooOoO0o % OO0OO0O0O0 + o0 - o00ooo0 / o00O0oo
@ oo000 . route ( '/nations' )
def iIiiI1 ( ) :
 o0O = [
 { 'label' : 'Việt Nam' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/country/viet-nam-1.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Hàn Quốc' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/country/han-quoc-2.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Nhật Bản' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/country/nhat-ban-3.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Trung Quốc' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/country/trung-quoc-4.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Mỹ - Châu Âu' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/country/my-chau-au-5.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Hồng Kong' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/country/hong-kong-6.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Đài Loan' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/country/dai-loan-7.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Châu Á' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/country/chau-a-8.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Ấn Độ' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/country/an-do-10.html?p=%s' ) , 1 ) } ,
 { 'label' : 'Thái Lan' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim60s.info/country/thai-lan-11.html?p=%s' ) , 1 ) }
 ]
 return oo000 . finish ( o0O )
 if 68 - 68: o0 - Oo0Ooo - iIIIiiIIiiiIi / ooOoO0o - iIIIiiIIiiiIi + I1IiiI
@ oo000 . route ( '/nations/<murl>/<page>' )
def IiiIII111ii ( murl , page ) :
 o0O = i1ii1iIII ( murl , page , 'nations' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( o0O )
 if 3 - 3: o00ooo0 + OO0OO0O0O0
@ oo000 . route ( '/search/' )
def I1Ii ( ) :
 o0oOo0Ooo0O = oo000 . keyboard ( heading = 'Tìm kiếm' )
 if o0oOo0Ooo0O :
  OO00O0O0O00Oo = "http://m.phim60s.info/tim-kiem.html?keyword=&p=%s" . replace ( "keyword=" , "keyword=" + o0oOo0Ooo0O . replace ( " " , "+" ) )
  IIIiiiiiIii = '%s/search/%s/%s' % ( ii , urllib . quote_plus ( OO00O0O0O00Oo ) , 1 )
  oo000 . redirect ( IIIiiiiiIii )
  if 70 - 70: iIIIiiIIiiiIi . iIIIiiIIiiiIi - iIIIiiIIiiiIi / IiII * ooOoO0o
@ oo000 . route ( '/search/<murl>/<page>' )
def OoO000 ( murl , page ) :
 o0O = i1ii1iIII ( murl , page , 'search' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( o0O )
 if 42 - 42: I1Ii111 - I1IiiI / Oo0Ooo + ooOoO0o + iIIIiiIIiiiIi
@ oo000 . route ( '/mirrors/<murl>' )
def iIi ( murl ) :
 o0O = [ ]
 for II in iI ( murl ) :
  if "Zing" not in II [ "name" ] and "ClipVN" not in II [ "name" ] :
   iI11iiiI1II = { }
   iI11iiiI1II [ "label" ] = II [ "name" ] . strip ( )
   O0oooo0Oo00 = str ( uuid . uuid1 ( ) )
   Ii11iii11I = oo000 . get_storage ( O0oooo0Oo00 )
   Ii11iii11I [ "list" ] = II [ "eps" ]
   iI11iiiI1II [ "path" ] = '%s/eps/%s' % ( ii , urllib . quote_plus ( O0oooo0Oo00 ) )
   o0O . append ( iI11iiiI1II )
 return oo000 . finish ( o0O )
 if 72 - 72: ooOoO0o
@ oo000 . route ( '/eps/<eps_list>' )
def o0Oo00OOOOO ( eps_list ) :
 o0O = [ ]
 for O0O in oo000 . get_storage ( eps_list ) [ "list" ] :
  iI11iiiI1II = { }
  iI11iiiI1II [ "label" ] = O0O [ "name" ] . strip ( )
  iI11iiiI1II [ "is_playable" ] = True
  iI11iiiI1II [ "path" ] = '%s/play/%s' % ( ii , urllib . quote_plus ( O0O [ "url" ] ) )
  o0O . append ( iI11iiiI1II )
 return oo000 . finish ( o0O )
 if 83 - 83: o00O0oo + i1 * iII111i % iIIIiiIIiiiIi + o00O0oo
@ oo000 . route ( '/play/<url>' )
def Ii1iIIIi1ii ( url ) :
 o0oo0o0O00OO = xbmcgui . DialogProgress ( )
 o0oo0o0O00OO . create ( 'phim60s.info' , 'Loading video. Please wait...' )
 oo000 . set_resolved_url ( o0oO ( url ) )
 o0oo0o0O00OO . close ( )
 del o0oo0o0O00OO
 if 48 - 48: o00O0oo + o00O0oo / i1 / iiiIIii1IIi
def o0oO ( url ) :
 i1iiI11I = iiii ( url )
 oO0o0O0OOOoo0 = re . compile ( 'source src="(http://m.phim60s.info/.+?.mp4)"' ) . findall ( i1iiI11I ) [ 0 ]
 print oO0o0O0OOOoo0
 if "youtube" in i1iiI11I :
  IiIiiI = re . compile ( '(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)' ) . findall ( i1iiI11I )
  I1I = IiIiiI [ 0 ] [ len ( IiIiiI [ 0 ] ) - 1 ] . replace ( 'v/' , '' )
  return 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % I1I
 if "picasa" in i1iiI11I :
  oOO00oOO = re . compile ( 'src="(http://m.phim60s.info/picasa/.+?.mp4)"' ) . findall ( i1iiI11I ) [ 0 ]
  if oo000 . get_setting ( 'HQ' , bool ) :
   if "lh/photo" not in i1iiI11I :
    OoOo , iIo00O , OOO0OOO00oo = re . compile ( 'http://m.phim60s.info/picasa/(\d+)/\w+authkeyenterplus(.+?)/daukhac/(\d+).mp4' ) . findall ( oOO00oOO ) [ 0 ]
    Iii111II = "https://picasaweb.google.com/data/feed/api/user/%s/photoid/%s?authkey=%s&alt=json" % ( OoOo , OOO0OOO00oo , iIo00O )
    i1iiI11I = urllib2 . urlopen ( Iii111II ) . read ( )
    iiii11I = json . loads ( i1iiI11I ) [ "feed" ] [ "media$group" ] [ "media$content" ]
    for Ooo0OO0oOO in iiii11I :
     if ( Ooo0OO0oOO [ "type" ] == "video/mpeg4" ) and ( int ( Ooo0OO0oOO [ "height" ] ) <= 720 ) :
      oO0o0O0OOOoo0 = Ooo0OO0oOO [ "url" ]
   else :
    oOO00oOO = oOO00oOO . replace ( "http://m.phim60s.info/picasa/" , "https://picasaweb.google.com/" ) . strip ( ".mp4" )
    i1iiI11I = urllib2 . urlopen ( oOO00oOO ) . read ( )
    Iii111II = re . compile ( '(https://picasaweb.google.com/data/feed/tiny/user/\d+/photoid/\d+\?alt=jsonm&gupi=.+?)"' ) . findall ( i1iiI11I ) [ 0 ]
    i1iiI11I = urllib2 . urlopen ( Iii111II ) . read ( )
    iiii11I = json . loads ( i1iiI11I ) [ "feed" ] [ "media" ] [ "content" ]
    for Ooo0OO0oOO in iiii11I :
     if ( Ooo0OO0oOO [ "type" ] == "video/mpeg4" ) and ( int ( Ooo0OO0oOO [ "height" ] ) <= 720 ) :
      oO0o0O0OOOoo0 = Ooo0OO0oOO [ "url" ]
      if 50 - 50: o0
 return oO0o0O0OOOoo0
 if 34 - 34: o0 * i1 % o00ooo0 * Oo - o0
def i1ii1iIII ( url , page , route_name ) :
 II1III = int ( page ) + 1
 i1iiI11I = iiii ( url % page )
 IiIiiI = re . compile ( '<a href="(http://m.phim60s.info/watch/.+?)"><img[^>]*src="(.+?)"><h2>(.+?)</h2><p>(.+?)</p>' ) . findall ( i1iiI11I )
 o0O = [ ]
 for iI1iI1I1i1I , iIi11Ii1 , Ii11iII1 , Oo0O0O0ooO0O in IiIiiI :
  iI11iiiI1II = { }
  iI11iiiI1II [ "label" ] = "%s - %s" % ( Ii11iII1 , Oo0O0O0ooO0O )
  iI11iiiI1II [ "thumbnail" ] = iIi11Ii1
  iI11iiiI1II [ "path" ] = '%s/%s/%s' % ( ii , "mirrors" , urllib . quote_plus ( iI1iI1I1i1I ) )
  o0O . append ( iI11iiiI1II )
 if len ( o0O ) == oOOo :
  o0O . append ( { 'label' : 'Next >>' , 'path' : '%s/%s/%s/%s' % ( ii , route_name , urllib . quote_plus ( url ) , II1III ) , 'thumbnail' : 'http://icons.iconarchive.com/icons/rafiqul-hassan/blogger/128/Arrow-Next-icon.png' } )
 return o0O
 if 15 - 15: IiII + Oo - iII111iiiii11 / ooOoO0o
def iI ( murl ) :
 i1iiI11I = iiii ( murl )
 IiIiiI = re . compile ( '</video><br/>(.+?)<br/></div>' ) . findall ( i1iiI11I )
 oo000OO00Oo = IiIiiI [ 0 ] . split ( "<br/>" )
 if 51 - 51: o00 * iII111i + o00O0oo + iIIIiiIIiiiIi
 o0O0O00 = re . compile ( '<title>(.+?)</title>' ) . findall ( i1iiI11I ) [ 0 ]
 o000o = [ ]
 for II in oo000OO00Oo :
  I11IiI1I11i1i = re . compile ( '(.+?):<' ) . findall ( II ) [ 0 ] . strip ( )
  iI1ii1Ii = [ ]
  for oooo000 , iIIIi1 in re . compile ( '<a href="(.+?)"[^>]*>(.+?)</a>' ) . findall ( II ) :
   O0O = { }
   O0O [ "url" ] = oooo000
   O0O [ "name" ] = "Part %s - %s" % ( iIIIi1 , o0O0O00 )
   iI1ii1Ii . append ( O0O )
  II = { }
  II [ "name" ] = I11IiI1I11i1i
  II [ "eps" ] = iI1ii1Ii
  o000o . append ( II )
 return o000o
 if 20 - 20: I1IiiI + IiII - O0OOo
@ oo000 . cached ( TTL = 60 )
def iiii ( url ) :
 IiI11iII1 = urllib2 . Request ( url )
 IiI11iII1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3' )
 IiI11iII1 . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' )
 IiI11iII1 . add_header ( 'Accept-Encoding' , 'gzip, deflate, sdch' )
 IIII11I1I = urllib2 . urlopen ( IiI11iII1 )
 OOO0o = IIII11I1I . read ( )
 IIII11I1I . close ( )
 if "gzip" in IIII11I1I . info ( ) . getheader ( 'Content-Encoding' ) :
  OOO0o = zlib . decompress ( OOO0o , 16 + zlib . MAX_WBITS )
 OOO0o = '' . join ( OOO0o . splitlines ( ) ) . replace ( '\'' , '"' )
 OOO0o = OOO0o . replace ( '\n' , '' )
 OOO0o = OOO0o . replace ( '\t' , '' )
 OOO0o = re . sub ( '  +' , ' ' , OOO0o )
 OOO0o = OOO0o . replace ( '> <' , '><' )
 return OOO0o
 if 30 - 30: iiiIIii1IIi / O0OOo - Oo0oO0ooo - i1 % o00ooo0
if __name__ == '__main__' :
 oo000 . run ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
