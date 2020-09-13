import wx
import wx.grid
from datetime import datetime

#from dodatki import Dodatki
from db.oferta import Oferta, Postanowienia, OfertaService
from element import ElementView
import re
class OfertaView(ElementView):

    def __init__(self, parent=None,data_representation = None,default_offer=('','','','','','','','','','Pośrednik'),*args, **kw):
        super(OfertaView, self).__init__(parent=parent,show_remove_button=False ,*args, **kw)
        self.oferta = data_representation
        self.show_remove_button = False
        self.postanowienia = list()
        self.service = OfertaService()
        #init Oferta Data
        if self.oferta == None:
            self.oferta = default_offer
            self.oferta.date = datetime.today().strftime('%Y-%m-%d')
            self.id_oferta = None
        else:
            self.id_oferta = data_representation.id
            self.service.id_oferta = data_representation.id
        self.InitUI(self.oferta)

    #----------------------------------------------------------------------  
    def InitUI(self,data):

        self.value1 = wx.TextCtrl(parent=self,value=data.value1)
        self.data  = wx.TextCtrl(parent=self,value=str(data.date))
        self.value2  = wx.TextCtrl(parent=self,value=data.value2)
        self.value3  =  wx.TextCtrl(parent=self,value=data.value3)
        self.value4 = wx.TextCtrl(parent=self,value=data.value4)
        self.value5 =           wx.TextCtrl(parent=self,value=data.value5)
        self.value6 =      wx.TextCtrl(parent=self,value=data.value6)
        self.value7 =         wx.TextCtrl(parent=self,value=data.value7)
        self.value8 = wx.TextCtrl(parent=self,value=data.value8)
        self.value9 =   wx.TextCtrl(parent=self,value=str(data.value9))
    
        self.inputElements.append(self.value1)
        self.inputElements.append(self.data)
        self.inputElements.append(self.value2)
        self.inputElements.append(self.value3)
        self.inputElements.append(self.value4)
        self.inputElements.append(self.value5)
        self.inputElements.append(self.value6)
        self.inputElements.append(self.value7)
        self.inputElements.append(self.value8)
        self.inputElements.append(self.value9)

        
        for postanowienie in data.postanowienia:
            self.AddDodatek(dodatek = postanowienie)
        
        self.data_sizer.AddMany([
            (wx.StaticText(self,label="Wartość 1"),0, wx.EXPAND),(self.value1,0,wx.EXPAND),
            (wx.StaticText(self,label="Wartość 2 - Data"),0, wx.FIXED_MINSIZE),(self.data,0, wx.EXPAND),
            (wx.StaticText(self,label="Wartość 3"),0, wx.FIXED_MINSIZE),(self.value2,0, wx.EXPAND),
            (wx.StaticText(self,label="Wartość 4"),0, wx.FIXED_MINSIZE),(self.value3, 0, wx.EXPAND),
            (wx.StaticText(self,label="Wartość 5"),0, wx.FIXED_MINSIZE),(self.value4,0, wx.EXPAND),
            (wx.StaticText(self,label="Wartość 6"),0, wx.FIXED_MINSIZE),(self.value5,          0, wx.EXPAND),
            (wx.StaticText(self,label="Wartość 7"),0, wx.FIXED_MINSIZE),(self.value6,     0, wx.EXPAND),
            (wx.StaticText(self,label="Wartość 8"),0, wx.FIXED_MINSIZE),(self.value7,        0, wx.EXPAND),
            (wx.StaticText(self,label="Wartość 9"),0, wx.FIXED_MINSIZE),(self.value8,0, wx.EXPAND),
            (wx.StaticText(self,label="Wartość 10"),0, wx.FIXED_MINSIZE),(self.value9,  0, wx.EXPAND)])
        self.UpdateLayout()

    #----------------------------------------------------------------------
    def AddDodatek(self,event = None, dodatek=None):   
        if dodatek:     
            dod = PostanowienieView(parent=self,nazwa = dodatek.dodatki_value1, updatefunc = self.UpdateLayout)
        else:
            dod = PostanowienieView(parent=self, updatefunc = self.UpdateLayout)
        self.inputElements.append(dod.title)        
        self.dodatki_sizer.Add(dod,0, wx.EXPAND)
        self.postanowienia.append(dod)
        self.UpdateLayout()

    #----------------------------------------------------------------------
    def GetData(self):
        postanowienia_data = list()
            
        for p in self.postanowienia:
            if p:
                postanowienia_data.append(Postanowienia(p.title.GetValue()))
        return Oferta(
                self.value1.GetValue(), self.data.GetValue(), self.value2.GetValue(), self.value3.GetValue(),self.value4.GetValue(),self.value5.GetValue(),self.value6.GetValue(),self.value7.GetValue(),self.value8.GetValue(),self.value9.GetValue(),postanowienia = postanowienia_data,id = self.id_oferta)
       
    





class PostanowienieView(wx.Panel):
    def __init__(self,nazwa=None,parent=None,updatefunc=None,**kwargs):
        super(PostanowienieView,self).__init__(parent=parent,**kwargs)
        self.updatefunc = updatefunc
        self.InitUI()
        #Dialog
        self.remove_offer_dlg = wx.MessageDialog(self.Parent, "Czy na pewno chcesz usunąć dodatek", "Usuń Dodatek",wx.YES_NO)
        self.remove_offer_dlg.SetYesNoLabels("&Tak", "&Nie")
        if nazwa:
            self.title.SetLabel(nazwa)


    def InitUI(self):
        self.title =            wx.TextCtrl(parent=self)
     


        self.data_sizer =             wx.GridSizer(2)
        #gs.SetSize(800,500)
        self.data_sizer.AddMany([
            (wx.StaticText(self,label="Tytuł"),0, wx.FIXED_MINSIZE),(self.title,       0, wx.EXPAND)])

        self.main_sizer = wx.GridSizer(2)
        remove_btn = wx.Button(self,label="Usuń")
        self.Bind(wx.EVT_BUTTON, self.usunDodatek)

        self.main_sizer.Add(self.data_sizer,0,wx.EXPAND)
        self.main_sizer.Add(remove_btn,0,wx.EXPAND)
        self.SetSizerAndFit(self.main_sizer)
        self.main_sizer.Layout()

    def usunDodatek(self, event):
        if self.remove_offer_dlg.ShowModal() == wx.ID_YES:
            p = self.Parent
            self.Destroy()
            self.updatefunc()
