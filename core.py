# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#
# PPP: GUI
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
from callback_chiudi import ClassChiudi
from callback_status import ClassStatus
from callback_conversione import ClassConversione
from callback_formattazione import ClassFormattazione

#------------------------------------------------------------------------------
# GUI class
#------------------------------------------------------------------------------

class ClassInterfaccia(ClassChiudi, 
                       ClassStatus, 
                       ClassConversione, 
                       ClassFormattazione):
    """Class to define caracteristics of the program window system"""

    def __init__(self):
        
        # Set Main Window
        self.finestra = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.finestra.set_title("PPP merda")
        self.finestra.set_border_width(0)
        self.finestra.set_size_request(800, 600)

        # Set vertical boxes
        self.scaffale = gtk.VBox(False, 0)

        # Set Menu
        self.menu_file = gtk.Menu()
        self.menu_edit = gtk.Menu()

        # Set menu bar
        self.menu_barra = gtk.MenuBar()

        # Set menu items
        self.icona_nuovo = gtk.ImageMenuItem(gtk.STOCK_NEW)
        self.icona_apri = gtk.ImageMenuItem(gtk.STOCK_OPEN)
        self.icona_converti = gtk.ImageMenuItem(gtk.STOCK_CONVERT)
        self.icona_esci = gtk.ImageMenuItem(gtk.STOCK_QUIT)

#        self.icona_menu_file = gtk.ImageMenuItem(gtk.STOCK_FILE)
        self.icona_menu_file = gtk.MenuItem("File")
        self.icona_menu_edit = gtk.ImageMenuItem(gtk.STOCK_EDIT)
#        self.icona_menu_edit = gtk.MenuItem("Modifica")

        # Set submenu
        self.icona_menu_file.set_submenu(self.menu_file)
        self.icona_menu_edit.set_submenu(self.menu_edit)

        # Append menu items to menu
        self.menu_file.append(self.icona_nuovo)
        self.menu_file.append(self.icona_apri)
        self.menu_edit.append(self.icona_converti)
        self.menu_file.append(self.icona_esci)

        self.menu_barra.append(self.icona_menu_file)
        self.menu_barra.append(self.icona_menu_edit)

        # Show menu items
        self.icona_nuovo.show()
        self.icona_apri.show()
        self.icona_converti.show()
        self.icona_esci.show()

        self.icona_menu_file.show()
        self.icona_menu_edit.show()

        self.menu_barra.show()

        # Add menu to vbox
        self.scaffale.pack_start(self.menu_barra, False, False, 0)

        # Set scrolled window
        self.scorrevole = gtk.ScrolledWindow(None, None)

        # Set treestore
        self.lista = []
        self.archivio = gtk.TreeStore(int, str, str, str, str, str, str, str)
#        for i in range(len(self.lista)):
#            self.archivio.append(None, [self.lista[i]])
        self.griglia = gtk.TreeView(self.archivio)
        self.colonna_progr = gtk.TreeViewColumn("N")
        self.colonna_cod = gtk.TreeViewColumn("Codice")
        self.colonna_desc = gtk.TreeViewColumn("Descrizione")
        self.colonna_um = gtk.TreeViewColumn("U.M.")
        self.colonna_qta = gtk.TreeViewColumn("Quantità")
        self.colonna_pu = gtk.TreeViewColumn("Prezzo")
        self.colonna_imp = gtk.TreeViewColumn("Importo")

        self.griglia.append_column(self.colonna_progr)
        self.griglia.append_column(self.colonna_cod)
        self.griglia.append_column(self.colonna_desc)
        self.griglia.append_column(self.colonna_um)
        self.griglia.append_column(self.colonna_qta)
        self.griglia.append_column(self.colonna_pu)
        self.griglia.append_column(self.colonna_imp)

        self.cella_progressivo = gtk.CellRendererText()
        self.cella_progressivo.set_property('xalign',0.5)

        self.cella_codice = gtk.CellRendererText()

        self.cella_descrizione = gtk.CellRendererText()

        self.cella_unitamisura = gtk.CellRendererText()
        self.cella_unitamisura.set_property('xalign',1) 

        self.cella_quantita = gtk.CellRendererText()
        self.cella_quantita.set_property('xalign',1) 

        self.cella_prezzo = gtk.CellRendererText()
        self.cella_prezzo.set_property('xalign',1) 

        self.cella_importo = gtk.CellRendererText()
        self.cella_importo.set_property('xalign',1) 

        self.colonna_progr.pack_start(self.cella_progressivo, True)
        self.colonna_progr.add_attribute(self.cella_progressivo, "text", 0)
        self.colonna_progr.set_sort_column_id(0)

        self.colonna_cod.pack_start(self.cella_codice, True)
        self.colonna_cod.add_attribute(self.cella_codice, "text", 1)
        self.colonna_cod.set_sort_column_id(1)
        self.colonna_cod.add_attribute(self.cella_codice, "cell-background", 7)

        self.colonna_desc.pack_start(self.cella_descrizione, True)
        self.colonna_desc.add_attribute(self.cella_descrizione, "text", 2)
        self.colonna_desc.set_sort_column_id(2)

        self.colonna_um.pack_start(self.cella_unitamisura, True)
        self.colonna_um.add_attribute(self.cella_unitamisura, "text", 3)
        self.colonna_um.set_sort_column_id(3)

        self.colonna_qta.pack_start(self.cella_quantita, True)
        self.colonna_qta.add_attribute(self.cella_quantita, "text", 4)
        self.colonna_qta.set_sort_column_id(4)

        self.colonna_pu.pack_start(self.cella_prezzo, True)
        self.colonna_pu.add_attribute(self.cella_prezzo, "text", 5)
        self.colonna_pu.set_sort_column_id(5)

        self.colonna_imp.pack_start(self.cella_importo, True)
        self.colonna_imp.add_attribute(self.cella_importo, "text", 6)
        self.colonna_imp.set_sort_column_id(6)

        self.griglia.show()

        # Add tree to scrolled window
        self.scorrevole.add_with_viewport(self.griglia)

        # Show scrolled window
        self.scorrevole.show()

        # Add scrolled window to vbox
        self.scaffale.pack_start(self.scorrevole, True, True, 0)

        # Set status bar
        self.barra_stato = gtk.Statusbar()
        self.barra_stato.show()
        self.indicatore_stato = self.barra_stato.get_context_id("Barra di stato")
        self.messaggio_stato = self.invia_stato("Programma inizializzato")

        # Add status bar to vbox
        self.scaffale.pack_end(self.barra_stato, False, False, 0)

        # Put vertical boxes into main window
        self.finestra.add(self.scaffale)

        # Show boxes
        self.scaffale.show()

        # Show main window
        self.finestra.show()

        # Signal handlers
        self.finestra.connect('destroy', self.chiudi)
        self.icona_esci.connect('activate', self.chiudi)
        self.icona_converti.connect('activate', self.converti)

    def main(self):
        gtk.main()

# ClassInterfaccia Instance

if __name__ == '__main__':
    interfaccia = ClassInterfaccia()
    interfaccia.main()
