#------------------------------------------------------------------------------
#
# PPP: class ClassMessaggi
#
#------------------------------------------------------------------------------

# Import built-in lib
import gtk

# Import personal class

class ClassMessaggi:
    """Class to convert list from xls/pdf file in a usefull python listset various dialogs window"""

    def messaggio_errore(self, data = None):
            messaggio = gtk.MessageDialog(None, 
                                          0,
                                          gtk.MESSAGE_ERROR, 
                                          gtk.BUTTONS_CLOSE,
                                          None)
            messaggio.set_markup(data)
            messaggio.run()
            messaggio.destroy()
