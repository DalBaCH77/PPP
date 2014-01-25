# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#
# PPP: class ClassFormattazione
#
#------------------------------------------------------------------------------

# Import built-in lib
import gtk
from mimetypes import guess_type

# Import personal class
from callback_chiudi import ClassChiudi
from callback_status import ClassStatus
from callback_filechooser import ClassScelta
from xlrd import open_workbook
from callback_messaggi import ClassMessaggi
from decimal import Decimal

class ClassFormattazione(ClassChiudi, ClassStatus, ClassScelta, ClassMessaggi):
    """Class to store various format for treeview"""

    def valuta_euro(self, data):
        data = str('{0:.2F}'.format(Decimal(data)))
        data = data.replace('.',',')
        cent = len(data)-6
        while cent > 0 :
            data = data[:cent] + '.' + data[cent:]
            cent = cent-3
        data = u'\u20AC ' + data
        return data
    
    def quantita(self, data):
        data = str('{0:.3F}'.format(Decimal(data)))
        data = data.replace('.',',')
        cent = len(data)-7
        while cent > 0 :
            data = data[:cent] + '.' + data[cent:]
            cent = cent-3
        return data
