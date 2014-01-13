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


        # create a TreeStore with one string column to use as the model
        self.treestore = gtk.TreeStore(str)

        # we'll add some data now - 4 rows with 3 child rows each
        for parent in range(4):
            piter = self.treestore.append(None, ['parent %i' % parent])
            for child in range(3):
                self.treestore.append(piter, ['child %i of parent %i' %
                                              (child, parent)])

        # create the TreeView using treestore
        self.treeview = gtk.TreeView(self.treestore)

        # create the TreeViewColumn to display the data
        self.tvcolumn = gtk.TreeViewColumn('Column 0')

        # add tvcolumn to treeview
        self.treeview.append_column(self.tvcolumn)

        # create a CellRendererText to render the data
        self.cell = gtk.CellRendererText()

        # add the cell to the tvcolumn and allow it to expand
        self.tvcolumn.pack_start(self.cell, True)

        # set the cell "text" attribute to column 0 - retrieve text
        # from that column in treestore
        self.tvcolumn.add_attribute(self.cell, 'text', 0)

        # make it searchable
        self.treeview.set_search_column(0)

        # Allow sorting on the column
        self.tvcolumn.set_sort_column_id(0)

        # Allow drag and drop reordering of rows
        self.treeview.set_reorderable(True)

        # Put vertical boxes into main window
        self.finestra.add(self.treeview)

        # Show main window
        self.finestra.show_all()

        # Signal handlers
        self.finestra.connect('destroy', self.chiudi)

    def main(self):
        gtk.main()

# ClassInterfaccia Instance

if __name__ == '__main__':
    interfaccia = ClassInterfaccia()
    interfaccia.main()
