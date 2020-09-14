import wx
import wx.grid
#from dodatki import Dodatki
from .dodatki import DodatkiView
from model.oferta import OfertaService
REMOVE_EL_MESSAGE = "Czy na pewno chcesz usunąć element"
REMOVE_EL_CAPTION = "Usuń Element"
class ElementView(wx.Panel):

    def __init__(self,data_representation = None,show_remove_button=True, parent=None,*args, **kw):
        super(ElementView, self).__init__(parent=parent ,*args, **kw)
        self.data = data_representation
        self.show_remove_button = show_remove_button
        self._id = None
        self.dodatki = list()
        self.inputElements = []

        #Dialog
        self.remove_offer_dlg = wx.MessageDialog(self.Parent, REMOVE_EL_MESSAGE,REMOVE_EL_CAPTION ,wx.YES_NO)
        self.remove_offer_dlg.SetYesNoLabels("&Tak", "&Nie")

        # def Sizers
        self.btn_sizer =  wx.BoxSizer(wx.HORIZONTAL)
        self.data_sizer = wx.GridSizer(2)
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.dodatki_sizer = wx.GridSizer(1)

        #"Dodaj Dodatek" and "Usuń Element" btn Create
        self.btn_add = wx.Button(parent=self,label="Dodaj Dodatek",size=(-1,50))
        self.btn_add.Bind(wx.EVT_BUTTON,self.AddDodatek)
        self.btn_sizer.Add(self.btn_add,1, wx.EXPAND)
        if self.show_remove_button:
            self.btn_rm = wx.Button(parent=self,label="Usuń Element",size=(-1,50))
            self.btn_rm.Bind(wx.EVT_BUTTON,self.Remove)
            self.btn_sizer.Add(self.btn_rm,1, wx.EXPAND)   
          
        #Set Size Sizers
        self.data_sizer.SetMinSize(self.Parent.GetSize()[0]-20,(self.data_sizer.GetSize()[1]))
        self.dodatki_sizer.SetMinSize(self.Parent.GetSize()[0]-20,(self.dodatki_sizer.GetSize()[1]))
        self.btn_sizer.SetMinSize(self.Parent.GetSize()[0]-20,(self.btn_sizer.GetSize()[1]))
        #Append subSizers to main sizer
        self.main_sizer.Add(self.data_sizer,0,wx.EXPAND)
        self.main_sizer.Add(self.dodatki_sizer,0,wx.EXPAND)
        self.main_sizer.Add(self.btn_sizer,0,wx.EXPAND)
        self.SetSizerAndFit(self.main_sizer)
        self.UpdateLayout()

 
        
    #----------------------------------------------------------------------
    def Remove(self,event=None):
        if self.remove_offer_dlg.ShowModal() == wx.ID_YES: # Show Remove dialog 
            p = self.Parent        
            OfertaService().RemoveOfferElement(self.data)
            self.Destroy()
            p.Layout() #Resize offer panel after remove element

    #----------------------------------------------------------------------
    def AddDodatek(self,event= None, dodatek=None):        
        if dodatek != None:
            dod = DodatkiView(parent=self,value1=dodatek.value1,cena=dodatek.cenaZL2,value2=dodatek.value2, UpdateLayout = self.UpdateLayout)
        else:
            dod = DodatkiView(parent=self, UpdateLayout= self.UpdateLayout)
        self.inputElements.append(dod.value1)
        self.inputElements.append(dod.value2)
        self.inputElements.append(dod.cenaZL2)
        self.dodatki.append(dod)
        self.dodatki_sizer.Add(dod,1, wx.EXPAND)
        self.UpdateLayout()

    #----------------------------------------------------------------------
    def UpdateLayout(self):  
        """
        
        Resize Element and Element children 

        """      
        self.main_sizer.SetMinSize(self.GetSize()[0],-1)
        self.main_sizer.SetSizeHints(self)
        self.dodatki_sizer.Layout()      
        self.Parent.FitInside()
    def GetData(self):
        pass

        
 