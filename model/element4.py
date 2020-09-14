from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .db_conf import Session, Base, engine


class Element4(Base):
    __tablename__ = "Element4"
    id = Column(Integer, primary_key=True)
    value1 = Column(Integer)
    value2 = Column(String(512))
    value3 = Column(String(512))
    value4 = Column(String(512))
    value5 = Column(String(512))
    value6 = Column(String(512))
    value7 = Column(String(512))
    value8 = Column(String(512))
    value10 = Column(String(512))
    cenaZL1 = Column(Integer())
    cenaZL2 = Column(Integer())
    cenaZL3 = Column(Integer())
    value9 = Column(String(512))
    oferta_id = Column(Integer, ForeignKey('oferta.id', ondelete="cascade"))
    dodatki = relationship(
        "Dodatki_Element4", cascade="save-update, merge, delete",lazy='subquery')

    def __init__(self, value1, value2, value3, value4, value5, value6, value7, value8,  value10, value9, cenaZL1, cenaZL2, cenaZL3, oferta_id=None, id=None, dodatki=None):
        self.id = id
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.value4 = value4
        self.value5 = value5
        self.value6 = value6
        self.value7 = value7
        self.value8 = value8
        self.value9 = value9
        self.value10 = value10
        if dodatki:
            self.dodatki = dodatki
        self.oferta_id = oferta_id
        self.cenaZL1 = cenaZL1
        self.cenaZL2 = cenaZL2
        self.cenaZL3 = cenaZL3


class Dodatki_Element4(Base):
    __tablename__ = "dodatki_Element4"
    id = Column(Integer, primary_key=True)
    dodatki_value1 = Column(String(512))
    value1 = Column(String(512))
    cenaZL2 = Column(Integer())
    id_element = Column(Integer, ForeignKey('Element4.id', ondelete="cascade"), nullable=False)

    def __init__(self, dodatki_value1, value1, cenaZL2):
        self.dodatki_value1 = dodatki_value1
        self.value1 = value1
        self.cenaZL2 = cenaZL2
