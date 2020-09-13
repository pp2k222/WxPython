import wx
import wx.grid
#from dodatki import Dodatki
from db.element1 import Element1, Dodatki_Element1
from element import ElementView
import re
INT_REGEX = '[^0-9]+'
class Element1View(ElementView):

    def __init__(self, parent=None,data_representation = None,show_remove_button=True,default_offer=Element1(1,'','','','','','','','',0,0,0),*args, **kw):
        super(Element1View, self).__init__(parent=parent ,show_remove_button=show_remove_button,*args, **kw)
        self.data = data_representation
        if self.data == None:
            self._id = None
            self.data = default_offer
            self.data.dodatki = []
        else:
            self._id = data_representation.id 
        self.InitUI(self.data)

    #----------------------------------------------------------------------  
    def InitUI(self,data):
        self.value1 = wx.TextCtrl(parent=self,value=str(data.value1))
        self.value2= wx.TextCtrl(parent=self,value=data.value2)
        self.value3  = wx.TextCtrl(parent=self,value=str(data.value3 ))
        self.value4 = wx.TextCtrl(parent=self,value=data.value4 )
        self.value5 = wx.TextCtrl(parent=self,value=data.value5  )
        self.value6 = wx.TextCtrl(parent=self,value=data.value6 )
        self.value7 = wx.TextCtrl(parent=self,value=data.value7 )
        self.value8 = wx.TextCtrl(parent=self,value=data.value8)
        self.cenaZL1 = wx.TextCtrl(parent=self,value=str(data.cenaZL1))
        self.cenaZL2 = wx.TextCtrl(parent=self,value=str(data.cenaZL2))
        self.cenaZL3 = wx.TextCtrl(parent=self,value=str(data.cenaZL3))
        self.value9 = wx.TextCtrl(parent=self,value=data.value9)
        
        self.inputElements.append(self.value1)
        self.inputElements.append(self.value2)
        self.inputElements.append(self.value3)
        self.inputElements.append(self.value4)
        self.inputElements.append(self.value5)
        self.inputElements.append(self.value6)
        self.inputElements.append(self.value7)
        self.inputElements.append(self.value8)
        self.inputElements.append(self.cenaZL1)
        self.inputElements.append(self.cenaZL2)
        self.inputElements.append(self.cenaZL3)
        self.inputElements.append(self.value9)
        
        for dodatek in data.dodatki:
            self.AddDodatek(dodatek = dodatek)

        
        self.data_sizer.AddMany([
            (wx.StaticText(self,label="###"),1, wx.FIXED_MINSIZE),(wx.StaticText(self,label="Title"),1, wx.FIXED_MINSIZE),
            (wx.StaticText(self,label="Wartość 1"),1, wx.FIXED_MINSIZE),(self.value1,1, wx.EXPAND),
            (wx.StaticText(self,label="Wartość 2"),1, wx.FIXED_MINSIZE),(self.value2,1, wx.EXPAND),
            (wx.StaticText(self,label="Wartość 3"),1, wx.FIXED_MINSIZE),(self.value3,1, wx.EXPAND),
            (wx.StaticText(self,label="Wartość 4"),1, wx.FIXED_MINSIZE),(self.value4,1, wx.EXPAND),
            (wx.StaticText(self,label="Wartość 5"),1, wx.FIXED_MINSIZE),(self.value5, 1, wx.EXPAND),
            (wx.StaticText(self,label="Wartość 6"),1, wx.FIXED_MINSIZE),(self.value6, 1, wx.EXPAND),
            (wx.StaticText(self,label="Wartość 7"),1, wx.FIXED_MINSIZE),(self.value7, 1, wx.EXPAND),
            (wx.StaticText(self,label="Wartość 8"),1, wx.FIXED_MINSIZE),(self.value8, 1, wx.EXPAND),
            (wx.StaticText(self,label="Cena 1"   ),1, wx.FIXED_MINSIZE),(self.cenaZL1,1, wx.EXPAND),
            (wx.StaticText(self,label="Cena 2"   ),1, wx.FIXED_MINSIZE),(self.cenaZL2,1, wx.EXPAND),
            (wx.StaticText(self,label="Cena 3"   ),1, wx.FIXED_MINSIZE),(self.cenaZL3,1, wx.EXPAND),
            (wx.StaticText(self,label="Wartość 9"),1, wx.FIXED_MINSIZE),(self.value9,1, wx.EXPAND)])

        self.UpdateLayout()

    #----------------------------------------------------------------------
    def GetData(self):
        db_dodatki = list()
        for d in self.dodatki:
            if d:
                if d.cenaZL2.GetValue() == '':
                    cenaZL2 = 0
                else:
                    cenaZL2 = int(re.sub(INT_REGEX, '', d.cenaZL2.GetValue()))
                db_dodatki.append(Dodatki_Element1(
                    d.value2.GetValue(), d.value1.GetValue(), cenaZL2))
        if self.cenaZL1.GetValue() == '':
            cenaZL1 = 0
        else:
            cenaZL1 = int(re.sub(INT_REGEX, '', self.cenaZL1.GetValue()))
        if self.cenaZL2.GetValue() == '':
            cenaZL2 = 0
        else:
            cenaZL2 = int(re.sub(INT_REGEX, '', self.cenaZL2.GetValue()))
        if self.cenaZL2.GetValue() == '':
            cenaZL2 = 0
        else:
            cenaZL3 = int(re.sub(INT_REGEX, '', self.cenaZL2.GetValue()))
        element = Element1(self.value1.GetValue(), self.value2.GetValue(), self.value3.GetValue(), self.value4.GetValue(), self.value5.GetValue(),self.value6.GetValue(),self.value7.GetValue(),self.value8.GetValue(), self.value9.GetValue(), cenaZL1, cenaZL2, cenaZL3, dodatki=db_dodatki, id=self._id)
        return element
  