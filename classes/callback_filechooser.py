#------------------------------------------------------------------------------
#
# PPP: class ClassScelta
#
#------------------------------------------------------------------------------

# Import built-in lib
import gtk

# Import personal class
from callback_chiudi import ClassChiudi

class ClassScelta(ClassChiudi):
    """Class to open dialog to file chooser"""

    def dialogo_scegli(self, data = None):
        filename = None
        dialogo = gtk.FileChooserDialog(action = gtk.FILE_CHOOSER_ACTION_OPEN,
                                       buttons = (gtk.STOCK_CANCEL,
                                                  gtk.RESPONSE_CANCEL,
                                                  gtk.STOCK_OPEN,
                                                  gtk.RESPONSE_OK))
        risposta = dialogo.run()
        if risposta == gtk.RESPONSE_OK:
            filename = dialogo.get_filename()
        elif risposta == gtk.RESPONSE_CANCEL:
            print "Cancel"
        dialogo.destroy()
        return filename
