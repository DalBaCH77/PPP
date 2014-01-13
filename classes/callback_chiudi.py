#------------------------------------------------------------------------------
#
# PPP: class ClassChiudi
#
#------------------------------------------------------------------------------

# Import built-in lib
import gtk

class ClassChiudi:
    """Class to end correctly a generic window"""
    def chiudi(self, widget):
        print "PPP send destroy signal"
        gtk.main_quit()
