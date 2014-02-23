# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#
# PPP: class ClassConversione
#
#------------------------------------------------------------------------------

# Import built-in lib
import gtk
import csv
#import locale
from mimetypes import guess_type

# Import personal class
from xlrd import open_workbook
#from callback_messaggi import ClassMessaggi
from callback_formattazione import ClassFormattazione
from decimal import *

#class ClassConversione(ClassChiudi, ClassStatus, ClassScelta, ClassMessaggi):
class ClassConversione(ClassFormattazione):
    """Class to convert list from xls/pdf file in a usefull python list"""

    def converti(self, dato = None):

        # COD Color table
        cod_mod = '#ccff33'
        cod_np = '#ffff99'
        cod_ok = '#ffffff'

        p10 = '#ff0000'
        p50 = '#ff7777'
        p100 = '#ffbbbb'
        m10 = '#0000ff'
        m50 = '#7777ff'
        m100 = '#bbbbff'

#        locale.setlocale(locale.LC_ALL, '')

        # Set the filename
        self.filename = self.view.finestra_apri()

        if self.filename == None:
            self.invia_stato("Conversione annullata dall'utente")
        else:
            self.invia_stato("Verifica compatibilità del file '" 
                             + self.filename 
                             + "' iniziata")
            self.lista = self.importa_file()

            if self.lista == []:
                self.invia_stato("Importazione del file '" 
                                 + self.filename 
                                 + "' non effettuata")
            else:

                for i in range(len(self.lista)):

                    importo = self.calcola_importo(self.lista[i][4], 
                                                   self.lista[i][5])
                    importo = self.valuta_euro(importo)
                    self.lista[i].append(importo) #self.lista[i][6]
                    self.lista[i][4] = self.quantita(self.lista[i][4])
#                    self.lista[i][5] = self.valuta_euro(self.lista[i][5])

                    # Convert the cod to usefull form
                    lista_cod, modifica = self.codifica_codice(self.lista[i][1])
                    self.lista[i].append(lista_cod) #self.lista[i][7]
 
                    # Verify the existence of cod in prezziario
                    temp = self.model.trova_cod(unicode(self.lista[i][7]),u'PRV_2014')
                    if temp == None:
                        modifica = "cod_np"
                        self.lista[i][7] = self.lista[i][1]
                    if modifica == "cod_ok":
                        self.lista[i].append(cod_ok) #self.lista[i][8]
                    elif modifica == "cod_mod":
                        self.lista[i].append(cod_mod) #self.lista[i][8]
                    elif modifica == "cod_np":
                        self.lista[i].append(cod_np) #self.lista[i][8]

                    # Verify the corrispondence of UM
                    if modifica != "cod_np" and unicode(self.lista[i][3]) != temp.um:
                        self.lista[i].append(cod_mod) #self.lista[i][9]
                    elif modifica == "cod_np" :
                        self.lista[i].append(cod_np) #self.lista[i][9]
                    else:
                        self.lista[i].append(cod_ok) #self.lista[i][9]

                    # Verify the corrispondence of PRICE

                    if modifica != "cod_np":
                        pu = Decimal(str(self.lista[i][5])).quantize(Decimal('.01'), rounding=ROUND_DOWN)
                        prezzo = Decimal(temp.prezzo).quantize(Decimal('.01'), rounding=ROUND_DOWN)
                        delta = (prezzo/pu) - 1

                    cod_pu = cod_ok

                    if modifica != "cod_np" and pu != prezzo:
                        #print str(pu)+"/"+str(prezzo)
                        if delta > 1 :
                            cod_pu = p10
                        elif delta < -1 :
                            cod_pu = m10
                        elif delta > 0 and delta <= 0.1 :
                            cod_pu = p50
                        elif delta < 0 and delta >= -0.1:
                            cod_pu = m50
                        elif delta > 0.1 and delta <= 1 :
                            cod_pu = p100
                        elif delta < -0.1 and delta >= -1 :
                            cod_pu = m100


                        self.lista[i].append(cod_pu) #self.lista[i][10]
                    elif modifica == "cod_np" :
                        self.lista[i].append(cod_np) #self.lista[i][10]
                    else:
                        self.lista[i].append(cod_ok) #self.lista[i][10]
                        


#                    print self.lista[i][1] + " --- " + self.lista[i][8] + " | " + self.lista[i][9]


            # Import data in the treestore
            if len(self.lista) != 0:
                for i in range(len(self.lista)):
                    self.view.archivio.append(None, [self.lista[i][0],   #0
                                                self.lista[i][1],   #1
                                                self.lista[i][2],   #2
                                                self.lista[i][3],   #3
                                                self.lista[i][4],   #4
                                                self.valuta_euro(self.lista[i][5]),   #5
                                                self.lista[i][6],   #6
                                                self.lista[i][8],   #7
                                                self.lista[i][9],  #8
                                                self.lista[i][10]])  #9
 
    def converti_prezziarioPAT(self, dato = None):
        """
        """
        # Set the filename
        self.filename = self.view.finestra_apri()

        if self.filename == None:
            self.invia_stato("Conversione annullata dall'utente")
        else:
            self.invia_stato("Verifica compatibilità del file '" 
                             + self.filename 
                             + "' iniziata")
            prezziario = self.importa_file()

            if prezziario == []:
                self.invia_stato("Importazione del file '" 
                                 + self.filename 
                                 + "' non effettuata")
            else:
                prezziario_mod = []

                # Erase blank line
                for i in range(len(prezziario)):
                    if prezziario[i] != []:
                        prezziario_mod.append(prezziario[i])
                        
                prezziario = prezziario_mod
                prezziario_mod = []

                for i in range(len(prezziario)):

                    codice = prezziario[i][0]
                    dato_corretto = []

                    if codice[1:2] == '.' and self.intero(codice[-1]):
                         
                        if codice.count('.') == 4 and len(prezziario[i]) != 4:                              # i is the index corrisponding not entire line
                            # j is the index of the completing line
                            j = i + 1
                            codice = prezziario[j][0]

                            while (codice[1:2] == '.' and self.intero(codice[-1])) == False and j <= len(prezziario):
                                j = j + 1
                                codice = prezziario[j][0]

                            dato_corretto = prezziario[i]


                            for n in range(j-i-1):

                                for t in range(len(prezziario[n + i + 1])):
                                    if t == 0:
                                        primo = prezziario[n + i + 1][t]
                                        ultimo = dato_corretto[len(dato_corretto) - 1]
                                        dato_corretto[len(dato_corretto) - 1] = ultimo + ", " + primo
                                    else:
                                        dato_corretto.append(prezziario[n + i + 1][t])
                            prezziario_mod.append(dato_corretto)
                        elif codice.count('.') == 4 and len(prezziario[i]) == 4:
                            dato_corretto = prezziario[i]
                            prezziario_mod.append(dato_corretto)
                        elif codice.count('.') < 4 and len(prezziario[i]) == 2:
                            prezziario[i].append('n.d.')
                            prezziario[i].append('n.d.')
                            dato_corretto = prezziario[i]
                            prezziario_mod.append(dato_corretto)
                        else:
                            dato_corretto = prezziario[i]
                prezziario = prezziario_mod
                prezziario_mod = []

                for i in range(len(prezziario)):
                    prezziario[i][3] = prezziario[i][3].replace('.','')
                    prezziario[i][3] = prezziario[i][3].replace(',','.')
                    self.model.importa_prezziario(unicode(prezziario[i][0], 
                                                          "ISO-8859-1"),
                                                  unicode(prezziario[i][1], 
                                                          "ISO-8859-1"),
                                                  unicode(prezziario[i][2], 
                                                          "ISO-8859-1"),
                                                  unicode(prezziario[i][3], 
                                                          "ISO-8859-1"),
                                                  unicode('PRV_2014'))
                self.model.session.commit()

    def intero(self, data):
        try:
            int(data)
            result = True
        except:
            result = False
        return result

    def importa_excel(self, dato = None):

        self.invia_stato("Modulo di importazione per file excel attivato")

        lista = []
        file_da_convertire = open_workbook(self.filename)
        foglio = file_da_convertire.sheet_by_index(0)

        for i in range(foglio.nrows):
            lista.append(foglio.row_values(i,0))
#            lista.append(unicode(foglio.row_values(i,0), "ISO-8859-1"))

        self.invia_stato("File excel '" + self.filename + "' importato")
        return lista

    def importa_txt(self, dato = None):

        self.invia_stato("Modulo di importazione per file di testo attivato")

        lista = []
        with open(self.filename, 'rb') as file_da_convertire:
            csv_reader = csv.reader(file_da_convertire, delimiter='\t')
            for row in csv_reader:
                lista.append(row)

#        for i in range(len(lista)):
#            for j in range(len(lista[i])):
#                lista[i][j] = unicode(lista[i][j], "ISO-8859-1")

        self.invia_stato("File txt '" + self.filename + "' importato")
        return lista

    def importa_file(self):
        """Define the file kind and apply the correct conversion"""

        tipo = guess_type(self.filename)
        if  tipo == ('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', None):
            lista = self.importa_excel()
        elif tipo == ('text/plain', None):
            lista = self.importa_txt()
#       elif qui ci vanno le altre tipologie di importazione pdf da primus... :
        else:
            lista = []
            self.view.messaggio_errore("Il file che si sta tentando di " + 
                                       "convertire non è tra quelli " +
                                       "gestiti dal programma")
        return lista    

    def calcola_importo(self, prezzo, quantita):
        """
        Calculate the product of quantita in str format and prezzo in str format
        and store it in importo as str
        """

        importo = Decimal(quantita)*Decimal(prezzo)
        importo = Decimal(importo).quantize(Decimal('.01'), 
                                            rounding=ROUND_DOWN)
        importo = str(importo)
        return importo

    def codifica_codice(self, dato):
        """
        To identify if the cod is equal to the one used in prezziario or is a 
        new price or is modified
        """

        dato_mod = dato
        risultato = None

        # Verify if cod is in the prezziario

        # ...

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

        return dato_mod, risultato

