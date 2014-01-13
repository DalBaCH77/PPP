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

#------------------------------------------------------------------------------
# GUI class
#------------------------------------------------------------------------------

class ClassInterfaccia(ClassChiudi, ClassStatus, ClassConversione):
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
            # progressivo(int)
            # codice(str)
            # descrizione(str)
            # um(str)
            # qta(float)
            # pu(float) 
#        self.treestore = gtk.TreeStore(int, str, str, str, float, float)
        self.treestore = gtk.TreeStore(str, str, str, str, str, str)
#        for i in range(len(self.lista)):
#            self.treestore.append(None, [self.lista[i]])
        self.treeview = gtk.TreeView(self.treestore)
        colonna_progr = gtk.TreeViewColumn("Progressivo")
        colonna_cod = gtk.TreeViewColumn("Codice")
        colonna_desc = gtk.TreeViewColumn("Descrizione")
        colonna_um = gtk.TreeViewColumn("Unità di misura")
        colonna_qta = gtk.TreeViewColumn("Quantità")
        colonna_pu = gtk.TreeViewColumn("Prezzo unitario")
        self.treeview.append_column(colonna_progr)
        self.treeview.append_column(colonna_cod)
        self.treeview.append_column(colonna_desc)
        self.treeview.append_column(colonna_um)
        self.treeview.append_column(colonna_qta)
        self.treeview.append_column(colonna_pu)
        cell = gtk.CellRendererText()
        colonna_progr.pack_start(cell, True)
        colonna_progr.add_attribute(cell, "text", 0)
        colonna_cod.pack_start(cell, True)
        colonna_cod.add_attribute(cell, "text", 1)
        colonna_desc.pack_start(cell, True)
        colonna_desc.add_attribute(cell, "text", 2)
        colonna_um.pack_start(cell, True)
        colonna_um.add_attribute(cell, "text", 3)
        colonna_qta.pack_start(cell, True)
        colonna_qta.add_attribute(cell, "text", 4)
        colonna_pu.pack_start(cell, True)
        colonna_pu.add_attribute(cell, "text", 5)

        self.treeview.show()

        # Add tree to scrolled window
        self.scorrevole.add_with_viewport(self.treeview)

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
