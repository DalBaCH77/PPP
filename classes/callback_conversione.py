# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#
# PPP: class ClassConversione
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
from callback_formattazione import ClassFormattazione
from decimal import *
from sqlalchemy import create_engine


class ClassConversione(ClassChiudi, ClassStatus, ClassScelta, ClassMessaggi):
    """Class to convert list from xls/pdf file in a usefull python list"""

    def converti(self, data = None):

        # COD Color table
        codice_asterisco = '#ccff33'
        codice_np = '#ffff99'
        codice_prezziario = None

        # Set the filename
        self.filename = self.dialogo_scegli()
        self.invia_stato("Conversione file " + 
                                     self.filename + 
                                     " iniziata")

        # Define the file kind and apply the correct conversion
        tipo = guess_type(self.filename)
        if  tipo == ('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', None):
            self.lista = self.converti_excel()
            
            # Import data in the list
            for i in range(len(self.lista)):

                # Calculate the product of quantita and prezzo and store it
                lista_importo = str(Decimal(Decimal(self.lista[i][4])*Decimal(self.lista[i][5])).quantize(Decimal('.01'), rounding=ROUND_DOWN))
                lista_importo = self.valuta_euro(lista_importo)
                self.lista[i].append(lista_importo) #self.lista[i][6]
                self.lista[i][4] = self.quantita(self.lista[i][4])
                self.lista[i][5] = self.valuta_euro(self.lista[i][5])

                # Convert the cod to usefull form
                lista_cod, modifica = self.codifica_codice(self.lista[i][1])
                self.lista[i].append(lista_cod)      #self.lista[i][7]

                # Identify the color of cod column and store it
#                print modifica
                if modifica == "cod_ok":
                    self.lista[i].append(codice_prezziario) #self.lista[i][8]
                elif modifica == "cod_mod":
                    self.lista[i].append(codice_asterisco) #self.lista[i][8]
                elif modifica == "cod_np":
                    self.lista[i].append(codice_np) #self.lista[i][8]
        else:
            self.invia_stato("Importazione del file " 
                             + self.filename 
                             + " non effettuata")
            self.messaggio_errore("Il file che si sta tentando di convertire non è tra quelli gestiti dal programma")
        
        # Import data in the treestore
        if len(self.lista) != 0:
            for i in range(len(self.lista)):
                self.archivio.append(None, [self.lista[i][0],   #1
                                            self.lista[i][1],   #2
                                            self.lista[i][2],   #3
                                            self.lista[i][3],   #4
                                            self.lista[i][4],   #5
                                            self.lista[i][5],   #6
                                            self.lista[i][6],   #7
                                            self.lista[i][8]])  #8
    
    def converti_excel(self, data = None):

        self.invia_stato("Modulo di conversione da file excel attivato")
        file_da_convertire = open_workbook(self.filename)
        foglio = file_da_convertire.sheet_by_index(0)

        for i in range(foglio.nrows):
            self.lista.append(foglio.row_values(i,0))

        self.invia_stato("File excel importato")
        return self.lista

    def codifica_codice(self, dato):
        """
        To identify if the cod is equal to the one used in prezziario or is a 
        new price or is modified
        """

        dato_mod = dato
        risultato = None

        # Verify if cod is in the prezziario

        # Verify if the cod that is in the prezziario is modified (*)
        if dato_mod[-1] == '*':
            while dato_mod[-1] == '*':
                dato_mod = dato_mod[:-1]
            risultato = "cod_mod"
        else:
            risultato = "cod_ok"

        # Code the cod in the correct form to be process by the program
        if dato_mod.find('.0') != -1:
            while dato_mod.find('.0') != -1:
                dato_mod = dato_mod.replace('.0','.')

#        print dato_mod, risultato
        return dato_mod, risultato
