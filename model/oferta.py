from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .db_conf import Base, Session, engine
from datetime import datetime

from model.element4 import Element4, Dodatki_Element4
from model.element5 import Element5, Dodatki_Element5
from model.element2 import Element2, Dodatki_Element2
from model.element3 import Element3, Dodatki_Element3
from model.element1 import Element1, Dodatki_Element1

DATA_FORMAT = '%Y-%m-%d'

class Oferta(Base):
    __tablename__ = "oferta"
    id = Column(Integer, primary_key=True)
    value1 = Column(String(512))
    date = Column(Date(), default=datetime.utcnow)
    value2 = Column(String(512))
    value3 = Column(String(512))
    value4 = Column(String(512))
    value5 = Column(String(512))
    value6 = Column(String(512))
    value7 = Column(String(512))
    value8 = Column(String(512))
    value9 = Column(String(512))
    postanowienia = relationship("Postanowienia",cascade="all, delete, delete-orphan" ,lazy='subquery')
    element1 = relationship("Element1",cascade="all, delete, delete-orphan",lazy='subquery')
    element2 = relationship("Element2",cascade="all, delete, delete-orphan",lazy='subquery')
    element3 = relationship("Element3",cascade="all, delete, delete-orphan",lazy='subquery')
    element4 = relationship("Element4",cascade="all, delete, delete-orphan",lazy='subquery')
    element5 = relationship("Element5",cascade="all, delete, delete-orphan",lazy='subquery')

    def __init__(self, value1, date, value2, value3,value4,value5,value6,value7,value8,value9,postanowienia=None,id=None):
        self.value1 = value1
        self.date = date
        self.value2 = value2
        self.value3 = value3
        self.value4 = value4
        self.value5 = value5
        self.value6 = value6
        self.value7 =value7
        self.value8 = value8
        self.value9 = value9
        if  postanowienia:
            self.postanowienia = postanowienia
        else: self.postanowienia = []
        if id:
            self.id=id

class Postanowienia(Base):
    __tablename__ = "postanowienia"
    id = Column(Integer, primary_key=True)
    dodatki_value1 = Column(String(512))
    id_element = Column(Integer, ForeignKey('oferta.id', ondelete="cascade"), nullable=False)

    def __init__(self, dodatki_value1):
        self.dodatki_value1 = dodatki_value1

class OfertaService:
    sess = Session()
    Base.metadata.create_all(engine)

    def __init__(self, id=None):
        if id:
            self.oferta = self.sess.query(Oferta).filter_by(id=id).first()

    def GetOffers(self,offerName = ""):
        if offerName !="":
            oferty = self.sess.query(Oferta.id,Oferta.value1,Oferta.date).filter(Oferta.value1.like('%'+offerName+'%')).order_by(Oferta.id.desc()).all()
        else:
            oferty = self.sess.query(Oferta.id,Oferta.value1,Oferta.date).order_by(Oferta.id.desc()).all()
        self.sess.close()
        return oferty
    def RemoveOffer(self,id):
        self.sess.query(Oferta).filter_by(id=id).delete()
        self.sess.commit()

        self.sess.close()
    def GetOfferById(self,id):
        oferta =  self.sess.query(Oferta).filter_by(id=id).first()
        self.sess.close()
        return oferta
    def GetElementBy(self,column,value,element_type):
        oferta =  self.sess.query(element_type).filter(getattr(element_type, column).like("%" + value + "%")).all()
        self.sess.close()
        return oferta
    def EditOffer(self,oferta):
        if oferta.id == None:
            oferta = self.AddOffer(oferta)  
        else:
            self.sess.query(Postanowienia).filter_by(id_element=self.id_oferta).delete()
            of_db = self.sess.query(Oferta).filter_by(id=self.id_oferta).first()
            of_db.value1 = str(oferta.value1)
            if oferta.date != '':
                of_db.date = datetime.strptime(oferta.date,DATA_FORMAT)
            else:
                of_db.date = datetime.now().strptime(oferta.date,DATA_FORMAT)    
            of_db.value2 = str(oferta.value2)
            of_db.value3 = str(oferta.value3)
            of_db.value4 = str(oferta.value4)
            of_db.value5 = str(oferta.value5)
            of_db.value6 = str(oferta.value6)
            of_db.value7 = str(oferta.value7)
            of_db.value8 = str(oferta.value8)

            of_db.value9 = str(oferta.value9)
            of_db.postanowienia = oferta.postanowienia
            self.sess.commit()
            self.sess.close()
        return oferta
    def AddOffer(self,oferta):

        if oferta.date == '':
            oferta.date = None
        else:
            oferta.date = datetime.strptime(oferta.date, DATA_FORMAT)
        self.sess.add(oferta)
        self.sess.commit()
        self.id_oferta = oferta.id
        oferta.postanowienia = []
        self.oferta = oferta
        self.sess.close()
        return oferta

    def AddOfferElement(self, element):
        oferta = self.sess.query(Oferta).filter_by(id=self.id_oferta).first()
        el_type = self.GetOfferElType(element)
        if el_type == Element1:
            oferta.element1.append(element)
        if el_type == Element2:
            oferta.element2.append(element)
        if el_type == Element3:
            oferta.element3.append(element)
        if el_type == Element4:
            oferta.element4.append(element)
        if el_type == Element5:
            oferta.element5.append(element)

        self.sess.commit()
        element_id = element.id        
        self.sess.close()
        return element_id
    def GetOfferElType(self,el):
        if type(el) == Element1:
            el_type = Element1
        elif type(el) == Element2:
            el_type = Element2
        elif type(el) == Element3:
            el_type = Element3
        elif type(el) == Element4:
            el_type = Element4
        elif type(el) == Element5:
            el_type = Element5
        return el_type        

    def RemoveOfferElement(self, element):
        el_type =self.GetOfferElType(element)
        self.sess.query(el_type).filter_by(id=element.id).delete()
    def AddDodatki(self,el,dodatki):
        el_type =self.GetOfferElType(el)
        main_element = self.sess.query(el_type).filter_by(
            id=el.id).first()
        main_element.dodatki =[]
        self.sess.commit()
        main_element.dodatki = dodatki
        self.sess.commit()
        self.sess.close()
        
    def EditOfferElement(self, el):
        el.oferta_id = self.id_oferta
        if el.id != None:
            el_type =self.GetOfferElType(el)
            
            self.sess.commit()
            self.sess.query(el_type).filter_by(id=el.id).update({column: getattr(el, column) for column in el_type.__table__.columns.keys()})
            self.sess.commit()
            el_id = el.id     
            self.sess.close()
            self.AddDodatki(el,el.dodatki) # Add dodatki remove and add dodatki instead of update

        else:
            el_id=self.AddOfferElement(el)

        self.sess.close()
        return el_id

   