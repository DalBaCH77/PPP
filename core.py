#

#------------------------------------------------------------------------------
#
# PPP: GUI
#
#------------------------------------------------------------------------------

# Import built-in lib
import sys
sys.path.append('classes')
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
from callback_chiudi import class_chiudi

#------------------------------------------------------------------------------
# GUI class
#------------------------------------------------------------------------------

class class_interfaccia(class_chiudi):
    
    def __init__(self):
        
        # Main Window
        self.finestra = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.finestra.set_title("PPP merda")
        self.finestra.set_border_width(0)
        self.finestra.set_size_request(800,600)

        # Show main window
        self.finestra.show()

        # Signal handlers
        self.finestra.connect('destroy',self.chiudi)

    def main(self):
        gtk.main()

# class_interfaccia Instance
if __name__ == '__main__':
    interfaccia = class_interfaccia()
    interfaccia.main()
