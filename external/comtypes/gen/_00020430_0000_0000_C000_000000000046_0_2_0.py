# -*- coding: mbcs -*-
typelib_path = 'C:\\Windows\\System32\\stdole2.tlb'
_lcid = 0 # change this if required
from ctypes import *
from comtypes import GUID
from comtypes import CoClass
from comtypes.automation import IDispatch
OLE_COLOR = c_ulong
FONTSIZE = c_longlong
from comtypes import BSTR
from ctypes.wintypes import VARIANT_BOOL
from comtypes import dispid
from comtypes import DISPMETHOD, DISPPROPERTY, helpstring
FONTBOLD = VARIANT_BOOL
OLE_XPOS_PIXELS = c_int
FONTNAME = BSTR
from comtypes import IUnknown
OLE_HANDLE = c_int
from ctypes import HRESULT
OLE_XSIZE_HIMETRIC = c_int
OLE_YSIZE_HIMETRIC = c_int
OLE_XPOS_HIMETRIC = c_int
OLE_YPOS_HIMETRIC = c_int
from comtypes import helpstring
from comtypes import COMMETHOD
OLE_YPOS_PIXELS = c_int
from comtypes import GUID
FONTITALIC = VARIANT_BOOL
OLE_XSIZE_PIXELS = c_int
FONTUNDERSCORE = VARIANT_BOOL
OLE_YSIZE_PIXELS = c_int
FONTSTRIKETHROUGH = VARIANT_BOOL
from comtypes.automation import IEnumVARIANT
OLE_XPOS_CONTAINER = c_float
from comtypes.automation import DISPPARAMS
OLE_YPOS_CONTAINER = c_float
OLE_XSIZE_CONTAINER = c_float
OLE_YSIZE_CONTAINER = c_float
OLE_OPTEXCLUSIVE = VARIANT_BOOL
OLE_CANCELBOOL = VARIANT_BOOL
from comtypes.automation import EXCEPINFO
OLE_ENABLEDEFAULTBOOL = VARIANT_BOOL



# values for enumeration 'OLE_TRISTATE'
Unchecked = 0
Checked = 1
Gray = 2
OLE_TRISTATE = c_int # enum
class StdPicture(CoClass):
    _reg_clsid_ = GUID('{0BE35204-8F91-11CE-9DE3-00AA004BB851}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00020430-0000-0000-C000-000000000046}', 2, 0)
class Picture(IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{7BF80981-BF32-101A-8BBB-00AA00300CAB}')
    _idlflags_ = []
    _methods_ = []
class IPicture(IUnknown):
    _case_insensitive_ = True
    'Picture Object'
    _iid_ = GUID('{7BF80980-BF32-101A-8BBB-00AA00300CAB}')
    _idlflags_ = ['hidden']
StdPicture._com_interfaces_ = [Picture, IPicture]


# values for enumeration 'LoadPictureConstants'
Default = 0
Monochrome = 1
VgaColor = 2
Color = 4
LoadPictureConstants = c_int # enum
class Font(IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{BEF6E003-A874-101A-8BBA-00AA00300CAB}')
    _idlflags_ = []
    _methods_ = []
Font._disp_methods_ = [
    DISPPROPERTY([dispid(0)], BSTR, 'Name'),
    DISPPROPERTY([dispid(2)], c_longlong, 'Size'),
    DISPPROPERTY([dispid(3)], VARIANT_BOOL, 'Bold'),
    DISPPROPERTY([dispid(4)], VARIANT_BOOL, 'Italic'),
    DISPPROPERTY([dispid(5)], VARIANT_BOOL, 'Underline'),
    DISPPROPERTY([dispid(6)], VARIANT_BOOL, 'Strikethrough'),
    DISPPROPERTY([dispid(7)], c_short, 'Weight'),
    DISPPROPERTY([dispid(8)], c_short, 'Charset'),
]
IFontDisp = Font
IPicture._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'Handle',
              ( ['out', 'retval'], POINTER(OLE_HANDLE), 'phandle' )),
    COMMETHOD(['propget'], HRESULT, 'hPal',
              ( ['out', 'retval'], POINTER(OLE_HANDLE), 'phpal' )),
    COMMETHOD(['propget'], HRESULT, 'Type',
              ( ['out', 'retval'], POINTER(c_short), 'ptype' )),
    COMMETHOD(['propget'], HRESULT, 'Width',
              ( ['out', 'retval'], POINTER(OLE_XSIZE_HIMETRIC), 'pwidth' )),
    COMMETHOD(['propget'], HRESULT, 'Height',
              ( ['out', 'retval'], POINTER(OLE_YSIZE_HIMETRIC), 'pheight' )),
    COMMETHOD([], HRESULT, 'Render',
              ( ['in'], c_int, 'hdc' ),
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' ),
              ( ['in'], c_int, 'cx' ),
              ( ['in'], c_int, 'cy' ),
              ( ['in'], OLE_XPOS_HIMETRIC, 'xSrc' ),
              ( ['in'], OLE_YPOS_HIMETRIC, 'ySrc' ),
              ( ['in'], OLE_XSIZE_HIMETRIC, 'cxSrc' ),
              ( ['in'], OLE_YSIZE_HIMETRIC, 'cySrc' ),
              ( ['in'], c_void_p, 'prcWBounds' )),
    COMMETHOD(['propput'], HRESULT, 'hPal',
              ( ['in'], OLE_HANDLE, 'phpal' )),
    COMMETHOD(['propget'], HRESULT, 'CurDC',
              ( ['out', 'retval'], POINTER(c_int), 'phdcOut' )),
    COMMETHOD([], HRESULT, 'SelectPicture',
              ( ['in'], c_int, 'hdcIn' ),
              ( ['out'], POINTER(c_int), 'phdcOut' ),
              ( ['out'], POINTER(OLE_HANDLE), 'phbmpOut' )),
    COMMETHOD(['propget'], HRESULT, 'KeepOriginalFormat',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'pfkeep' )),
    COMMETHOD(['propput'], HRESULT, 'KeepOriginalFormat',
              ( ['in'], VARIANT_BOOL, 'pfkeep' )),
    COMMETHOD([], HRESULT, 'PictureChanged'),
    COMMETHOD([], HRESULT, 'SaveAsFile',
              ( ['in'], c_void_p, 'pstm' ),
              ( ['in'], VARIANT_BOOL, 'fSaveMemCopy' ),
              ( ['out'], POINTER(c_int), 'pcbSize' )),
    COMMETHOD(['propget'], HRESULT, 'Attributes',
              ( ['out', 'retval'], POINTER(c_int), 'pdwAttr' )),
    COMMETHOD([], HRESULT, 'SetHdc',
              ( ['in'], OLE_HANDLE, 'hdc' )),
]
################################################################
## code template for IPicture implementation
##class IPicture_Impl(object):
##    @property
##    def Handle(self):
##        '-no docstring-'
##        #return phandle
##
##    def _get(self):
##        '-no docstring-'
##        #return phpal
##    def _set(self, phpal):
##        '-no docstring-'
##    hPal = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Type(self):
##        '-no docstring-'
##        #return ptype
##
##    @property
##    def Width(self):
##        '-no docstring-'
##        #return pwidth
##
##    @property
##    def Height(self):
##        '-no docstring-'
##        #return pheight
##
##    def Render(self, hdc, x, y, cx, cy, xSrc, ySrc, cxSrc, cySrc, prcWBounds):
##        '-no docstring-'
##        #return 
##
##    @property
##    def CurDC(self):
##        '-no docstring-'
##        #return phdcOut
##
##    def SelectPicture(self, hdcIn):
##        '-no docstring-'
##        #return phdcOut, phbmpOut
##
##    def _get(self):
##        '-no docstring-'
##        #return pfkeep
##    def _set(self, pfkeep):
##        '-no docstring-'
##    KeepOriginalFormat = property(_get, _set, doc = _set.__doc__)
##
##    def PictureChanged(self):
##        '-no docstring-'
##        #return 
##
##    def SaveAsFile(self, pstm, fSaveMemCopy):
##        '-no docstring-'
##        #return pcbSize
##
##    @property
##    def Attributes(self):
##        '-no docstring-'
##        #return pdwAttr
##
##    def SetHdc(self, hdc):
##        '-no docstring-'
##        #return 
##

class StdFont(CoClass):
    _reg_clsid_ = GUID('{0BE35203-8F91-11CE-9DE3-00AA004BB851}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{00020430-0000-0000-C000-000000000046}', 2, 0)
class FontEvents(IDispatch):
    _case_insensitive_ = True
    'Event interface for the Font object'
    _iid_ = GUID('{4EF6100A-AF88-11D0-9846-00C04FC29993}')
    _idlflags_ = ['hidden']
    _methods_ = []
class IFont(IUnknown):
    _case_insensitive_ = True
    'Font Object'
    _iid_ = GUID('{BEF6E002-A874-101A-8BBA-00AA00300CAB}')
    _idlflags_ = ['hidden']
StdFont._com_interfaces_ = [Font, IFont]
StdFont._outgoing_interfaces_ = [FontEvents]

FontEvents._disp_methods_ = [
    DISPMETHOD([dispid(9)], None, 'FontChanged',
               ( ['in'], BSTR, 'PropertyName' )),
]
IFont._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'Name',
              ( ['out', 'retval'], POINTER(BSTR), 'pname' )),
    COMMETHOD(['propput'], HRESULT, 'Name',
              ( ['in'], BSTR, 'pname' )),
    COMMETHOD(['propget'], HRESULT, 'Size',
              ( ['out', 'retval'], POINTER(c_longlong), 'psize' )),
    COMMETHOD(['propput'], HRESULT, 'Size',
              ( ['in'], c_longlong, 'psize' )),
    COMMETHOD(['propget'], HRESULT, 'Bold',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'pbold' )),
    COMMETHOD(['propput'], HRESULT, 'Bold',
              ( ['in'], VARIANT_BOOL, 'pbold' )),
    COMMETHOD(['propget'], HRESULT, 'Italic',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'pitalic' )),
    COMMETHOD(['propput'], HRESULT, 'Italic',
              ( ['in'], VARIANT_BOOL, 'pitalic' )),
    COMMETHOD(['propget'], HRESULT, 'Underline',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'punderline' )),
    COMMETHOD(['propput'], HRESULT, 'Underline',
              ( ['in'], VARIANT_BOOL, 'punderline' )),
    COMMETHOD(['propget'], HRESULT, 'Strikethrough',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'pstrikethrough' )),
    COMMETHOD(['propput'], HRESULT, 'Strikethrough',
              ( ['in'], VARIANT_BOOL, 'pstrikethrough' )),
    COMMETHOD(['propget'], HRESULT, 'Weight',
              ( ['out', 'retval'], POINTER(c_short), 'pweight' )),
    COMMETHOD(['propput'], HRESULT, 'Weight',
              ( ['in'], c_short, 'pweight' )),
    COMMETHOD(['propget'], HRESULT, 'Charset',
              ( ['out', 'retval'], POINTER(c_short), 'pcharset' )),
    COMMETHOD(['propput'], HRESULT, 'Charset',
              ( ['in'], c_short, 'pcharset' )),
    COMMETHOD(['propget'], HRESULT, 'hFont',
              ( ['out', 'retval'], POINTER(OLE_HANDLE), 'phfont' )),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IFont)), 'ppfont' )),
    COMMETHOD([], HRESULT, 'IsEqual',
              ( ['in'], POINTER(IFont), 'pfontOther' )),
    COMMETHOD([], HRESULT, 'SetRatio',
              ( ['in'], c_int, 'cyLogical' ),
              ( ['in'], c_int, 'cyHimetric' )),
    COMMETHOD([], HRESULT, 'AddRefHfont',
              ( ['in'], OLE_HANDLE, 'hFont' )),
    COMMETHOD([], HRESULT, 'ReleaseHfont',
              ( ['in'], OLE_HANDLE, 'hFont' )),
]
################################################################
## code template for IFont implementation
##class IFont_Impl(object):
##    def _get(self):
##        '-no docstring-'
##        #return pname
##    def _set(self, pname):
##        '-no docstring-'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return psize
##    def _set(self, psize):
##        '-no docstring-'
##    Size = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return pbold
##    def _set(self, pbold):
##        '-no docstring-'
##    Bold = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return pitalic
##    def _set(self, pitalic):
##        '-no docstring-'
##    Italic = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return punderline
##    def _set(self, punderline):
##        '-no docstring-'
##    Underline = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return pstrikethrough
##    def _set(self, pstrikethrough):
##        '-no docstring-'
##    Strikethrough = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return pweight
##    def _set(self, pweight):
##        '-no docstring-'
##    Weight = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return pcharset
##    def _set(self, pcharset):
##        '-no docstring-'
##    Charset = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def hFont(self):
##        '-no docstring-'
##        #return phfont
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppfont
##
##    def IsEqual(self, pfontOther):
##        '-no docstring-'
##        #return 
##
##    def SetRatio(self, cyLogical, cyHimetric):
##        '-no docstring-'
##        #return 
##
##    def AddRefHfont(self, hFont):
##        '-no docstring-'
##        #return 
##
##    def ReleaseHfont(self, hFont):
##        '-no docstring-'
##        #return 
##

IFontEventsDisp = FontEvents
Picture._disp_methods_ = [
    DISPPROPERTY([dispid(0), 'readonly'], OLE_HANDLE, 'Handle'),
    DISPPROPERTY([dispid(2)], OLE_HANDLE, 'hPal'),
    DISPPROPERTY([dispid(3), 'readonly'], c_short, 'Type'),
    DISPPROPERTY([dispid(4), 'readonly'], OLE_XSIZE_HIMETRIC, 'Width'),
    DISPPROPERTY([dispid(5), 'readonly'], OLE_YSIZE_HIMETRIC, 'Height'),
    DISPMETHOD([dispid(6)], None, 'Render',
               ( [], c_int, 'hdc' ),
               ( [], c_int, 'x' ),
               ( [], c_int, 'y' ),
               ( [], c_int, 'cx' ),
               ( [], c_int, 'cy' ),
               ( [], OLE_XPOS_HIMETRIC, 'xSrc' ),
               ( [], OLE_YPOS_HIMETRIC, 'ySrc' ),
               ( [], OLE_XSIZE_HIMETRIC, 'cxSrc' ),
               ( [], OLE_YSIZE_HIMETRIC, 'cySrc' ),
               ( [], c_void_p, 'prcWBounds' )),
]
IPictureDisp = Picture
class Library(object):
    'OLE Automation'
    name = 'stdole'
    _reg_typelib_ = ('{00020430-0000-0000-C000-000000000046}', 2, 0)

__all__ = [ 'StdPicture', 'FONTNAME', 'VgaColor', 'OLE_XPOS_PIXELS',
           'OLE_COLOR', 'OLE_YSIZE_CONTAINER', 'LoadPictureConstants',
           'OLE_YPOS_HIMETRIC', 'OLE_YSIZE_PIXELS',
           'OLE_XSIZE_CONTAINER', 'Font', 'FONTITALIC',
           'OLE_OPTEXCLUSIVE', 'IPictureDisp', 'OLE_XSIZE_PIXELS',
           'FONTBOLD', 'Gray', 'OLE_YSIZE_HIMETRIC', 'IFontDisp',
           'IFontEventsDisp', 'Checked', 'OLE_YPOS_CONTAINER',
           'Monochrome', 'OLE_XPOS_HIMETRIC', 'IPicture',
           'FontEvents', 'Color', 'OLE_CANCELBOOL', 'Picture',
           'StdFont', 'OLE_XSIZE_HIMETRIC', 'OLE_HANDLE', 'Unchecked',
           'FONTSTRIKETHROUGH', 'FONTSIZE', 'IFont',
           'OLE_ENABLEDEFAULTBOOL', 'OLE_YPOS_PIXELS', 'Default',
           'OLE_XPOS_CONTAINER', 'OLE_TRISTATE', 'FONTUNDERSCORE']
from comtypes import _check_version; _check_version('1.1.11', 1575709685.550032)
