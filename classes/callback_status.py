#------------------------------------------------------------------------------
#
# PPP: class ClassStatus
#
#------------------------------------------------------------------------------

# Import built-in lib
import gtk

class ClassStatus:
    """Class to send messagges to status bar"""

    barra_stato = gtk.Statusbar()
    indicatore_stato = barra_stato.get_context_id("Barra di stato")

    def invia_stato(self, messaggio):
        self.barra_stato.push(self.indicatore_stato, 
                              messaggio)

    def spedisci_stato(self):
        self,barra_stato.pop(self.indicatore_stato)
