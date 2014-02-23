# -*- coding: utf-8 -*-
# data.py
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
# PPP: MODEL Module
#
# Database engine: provided by Sqlite
# Database O.R.M: provided by SqlAlchemy (no_declarative)
# All data are contained here.
# All the O.R.M. operation on data are defined here as
# Model-Class methods.
#
#------------------------------------------------------------------------------

# Import built-in lib
from sqlalchemy import create_engine, Column, Integer, Float#, Unicode
from sqlalchemy import ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import aliased
from sqlalchemy.orm import sessionmaker
from sqlalchemy import orm, func, desc, asc
from sqlalchemy import MetaData, exc
from sqlalchemy.types import Unicode

# Import personal class

#------------------------------------------------------------------------------

class Gara(object):
    '''class for sqlalchemy mapper'''

    pass

class Prezziario(object):
    '''class for sqlalchemy mapper'''

    pass

class Prezziari(object):
    '''class for sqlalchemy mapper'''

    pass

class Modello(object): 
    '''Model class with common application data'''
    
    base = declarative_base()
    engine = create_engine('sqlite:///DB.db', echo = False)
    metadata = MetaData()
    
    gara_tab = Table('gara', metadata,
        Column('id_gara', Integer(), primary_key=True),
        Column('cig', Integer()),
        Column('nome', Unicode(255)),
        Column('tipo', Unicode(255)),
    )
    
    prezziario_tab = Table('prezziario', metadata,
        Column('id_prezziario', Integer(), primary_key=True),
        Column('cod', Unicode(19)),
        Column('descrizione', Unicode(255)),
        Column('um', Unicode(255)),
        Column('prezzo', Unicode(255)),
        Column('prezziario', Unicode(8)),
    )
    
    prezziari_tab = Table('elenco_prezziari', metadata,
        Column('id_prezziario', Unicode(8), primary_key=True),
        Column('descrizione', Unicode(255)),
        Column('anno', Integer()),
    )
    
    # Map SQLAlchemy table definitions to python classes
    orm.mapper(Gara, gara_tab, properties={})

    orm.mapper(Prezziario, prezziario_tab, properties={})

    orm.mapper(Prezziari, prezziari_tab, properties={})

    def __init__(self):
        Modello.metadata.create_all(Modello.engine)
        session = sessionmaker(bind = Modello.engine)
        self.session = session()
        self.cols = {0: Prezziario.cod, 
                     1: Prezziario.descrizione,
                     2: Prezziario.um,
                     3: Prezziario.prezzo}
        
    def trova_cod(self, codice, nome_prezziario):
        '''
        '''
        cod = self.session.query(Prezziario).filter(Prezziario.cod == codice).filter(Prezziario.prezziario == nome_prezziario).first()
        return cod

    def importa_prezziario(self, codice, descrizione, um, prezzo, prezziario):
        dato = Prezziario()
        dato.cod = codice
        dato.descrizione = descrizione
        dato.um = um
        dato.prezzo = prezzo
        dato.prezziario = prezziario
        self.session.add(dato)

    def total_commit(self):
        '''external commit to use outside loop'''
        self.session.commit()

def main():
    '''test starter'''
    mod = Modello()


if __name__ == '__main__':
    main()
