# -*- coding: utf-8 -*-
# core.py
#------------------------------------------------------------------------------
#                             +--------------+
#                             |     MODEL    |
#                             +--------------+
#                            /                \
#                           /                  \
#                       aggiorna             manipola
#                         /                      \
#                        /                        \
#                 +-----------+            +--------------+
#                 |   VIEW    |            |  CONTROLLER  |
#                 +-----------+            +--------------+
#                        \                        ^
#                         \                      /
#                         vede                 usa
#                           \                  /
#                            \                /
#                             v              / 
#                             +--------------+
#                             |    UTENTE    |
#                             +--------------+
#
# PPP: CONTROLLER Module
#
# Application pattern:
# MODEL | VIEW | CONTROLLER
# MODEL Module contains all data for database querying
# VIEW Module Contains all GUI for viewing all database data
# CONTROLLER Module contains app logic.
# All the binding method to frame widget are defined here''' 
#
#------------------------------------------------------------------------------

# Import built-in lib
import sys
sys.path.append('classes') # add 'classes' directory to path
try:
    import pygtk
    pygtk.require('2.0')
except:
    pass
try:
    import gtk
except:
    print 'GTK not available'
    sys.exit(1)

# Import personal class
from data import Modello
from view import Interfaccia

from callback_status import ClassStatus
from callback_chiudi import ClassChiudi
from callback_conversione import ClassConversione
#from callback_formattazione import ClassFormattazione

#------------------------------------------------------------------------------

class Controllore(object, ClassStatus, ClassChiudi, ClassConversione):
    '''Controller class for MVC-like pattern'''

    def __init__(self):

        self.lista = []
        self.model = Modello() # Model reference
        self.view = Interfaccia() # View reference
        self.invia_stato("Programma inizializzato correttamente")

        # Signal handlers
        self.view.finestra.connect('destroy', self.chiudi)
        self.view.icona_esci.connect('activate', self.chiudi)
        self.view.icona_converti.connect('activate', self.converti)
        self.view.icona_prezziario.connect('activate', self.converti_prezziarioPAT)

    def main(self):
        gtk.main()

if __name__ == '__main__':
    Avvio = Controllore()
    Avvio.main()
