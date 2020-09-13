from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .db_conf import Base


class Element5(Base):
    __tablename__ = "Element5"
    id = Column(Integer, primary_key=True)
    value1 = Column(Integer)
    value2= Column(String(512))
    value3 = Column(String(512))
    value3 = Column(String(512))
    value4 = Column(String(512))
    value5 = Column(String(512))
    value6 = Column(String(512))
    value7 = Column(String(512))
    value8 = Column(String(512))
    oferta_id = Column(Integer, ForeignKey('oferta.id', ondelete="cascade"))
    cenaZL1 = Column(Integer())
    cenaZL2 = Column(Integer())
    cenaZL3 = Column(Integer())
    dodatki = relationship("Dodatki_Element5",
                           cascade="save-update, merge, delete",lazy='subquery')
    value9 = Column(String(512))
    
    def __init__(self, value1, value2, value3, value4, value5, value6, value7, value8,  value9, cenaZL1, cenaZL2, cenaZL3, oferta_id=None, id=None, dodatki=None):
        self.id = id
        self.value1 = value1
        self.value2= value2
        self.value3 = value3
        self.value4 = value4
        self.value5 = value5
        self.value6 = value6
        self.value7 = value7
        self.value8 = value8
        if dodatki:
            self.dodatki = dodatki
        self.value9 = value9
        self.oferta_id = oferta_id
        self.cenaZL1 = cenaZL1
        self.cenaZL2 = cenaZL2
        self.cenaZL3 = cenaZL3


class Dodatki_Element5(Base):
    __tablename__ = "dodatki_Element5"
    id = Column(Integer, primary_key=True)
    dodatki_value1 = Column(String(512))
    value1 = Column(String(512))
    cenaZL2 = Column(Integer)
    id_element = Column(Integer, ForeignKey('Element5.id', ondelete="cascade"))

    def __init__(self, value1, value2, cenaZL2):
        self.value1 = value1
        self.value2 = value2
        self.cenaZL2 = cenaZL2
