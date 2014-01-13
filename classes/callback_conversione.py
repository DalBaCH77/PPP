# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#
# PPP: class ClassConversione
#
#------------------------------------------------------------------------------

# -*- coding: utf-8 -*-

# Import built-in lib
import gtk
from mimetypes import guess_type

# Import personal class
from callback_chiudi import ClassChiudi
from callback_status import ClassStatus
from callback_filechooser import ClassScelta
from xlrd import open_workbook
from callback_messaggi import ClassMessaggi

class ClassConversione(ClassChiudi, ClassStatus, ClassScelta, ClassMessaggi):
    """Class to convert list from xls/pdf file in a usefull python list"""

    def converti(self, data = None):
        self.filename = self.dialogo_scegli()
        self.invia_stato("Conversione file " + 
                                     self.filename + 
                                     " iniziata")
        tipo = guess_type(self.filename)
        if  tipo == ('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', None):
            self.lista = self.converti_excel()
            self.invia_stato("Modulo di conversione da file excel attivato")
            print "prova"
            print self.lista
            for i in range(len(self.lista)):
                self.treestore.append(None, self.lista[i])

        else:
            self.invia_stato("Importazione del file " 
                             + self.filename 
                             + " non effettuata")
            self.messaggio_errore("Il file che si sta tentando di convertire non è tra quelli gestiti dal programma")
            
    def converti_excel(self, data = None):
        file_da_convertire = open_workbook(self.filename)
        foglio = file_da_convertire.sheet_by_index(0)
        for i in range(foglio.nrows):
            self.lista.append(foglio.row_values(i,0))
        return self.lista
