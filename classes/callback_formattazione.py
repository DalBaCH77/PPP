# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#
# PPP: class ClassFormattazione
#
#------------------------------------------------------------------------------

# Import built-in lib
import gtk
from decimal import Decimal

# Import personal class

class ClassFormattazione():
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
