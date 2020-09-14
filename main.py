
import wx
import wx.lib.scrolledpanel as scrolled
from view.oferta import OfertaView
from model.oferta import OfertaService,Oferta 

import offer

from model.element1 import Element1
from model.element2 import Element2
from model.element3 import Element3
from model.element4 import Element4
from model.element5 import Element5
class MyForm(wx.Frame):
    
    #----------------------------------------------------------------------
    def __init__(self,oferta_id=None):
        wx.Frame.__init__(self, None, wx.ID_ANY, "ZHU Skoczylas", size=(1200,650))
        self.OFFER_TEMPLATE_ID = 1
        offService = OfertaService()
        if offService.GetOfferById(self.OFFER_TEMPLATE_ID) == None:
            offService.AddOffer(Oferta('','','','','','','','','','Pośrednik'))
            offService.AddOfferElement(Element1(1,'','','','','','','','','',0,0,0))
            offService.AddOfferElement(Element2(1,'', '', '', '', '','', '' , 0, 0, 0, dodatki=None, id=None))
            offService.AddOfferElement(Element3(1, '', '', '', '', '', '', '', 0, 0, 0))
            offService.AddOfferElement(Element4(1,'','','','','','','','','','',0,0,8))
            offService.AddOfferElement(Element5(1,'','','','','','','','',0,0,0))
        self.panel = wx.Panel(self, wx.ID_ANY)
        panel_sizer = wx.BoxSizer(wx.VERTICAL)
        panel_sizer.SetMinSize(self.GetSize()[0]-50,-1)
        # Creating the menubar.
        menuBar = wx.MenuBar()
        add_elements_menu= wx.Menu()        
        menu_add_Oferta = add_elements_menu.Append(wx.ID_ANY, "&Oferta"," Dodaj Oferta")        
        menuBar.Append(add_elements_menu,"&Dodaj &Oferte")

        configurate_default_offert_menu= wx.Menu()        
        configurate_offert_menu = configurate_default_offert_menu.Append(wx.ID_ANY, "&Konfiguracja","Oferta")        
        menuBar.Append(configurate_default_offert_menu,"&Przykładowa Oferta")
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.OfferConfiguration, configurate_offert_menu) 
        self.Bind(wx.EVT_MENU, self.AddOffer, menu_add_Oferta) 

        # Scrolled panel stuff
        self.scrolled_panel = scrolled.ScrolledPanel(self.panel, -1, style =wx.HSCROLL|wx.VSCROLL|wx.ALWAYS_SHOW_SB, name="panel1")
        #self.scrolled_panel.SetAutoLayout(1)
        self.scrolled_panel.SetupScrolling(scroll_x=False)
        self.element_sizer = wx.BoxSizer(wx.VERTICAL)
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.serachBar = wx.TextCtrl(parent=self.scrolled_panel) 
        self.serachBar.Bind(wx.EVT_TEXT,self.serachBarTextChange)
        self.main_sizer.Add(self.serachBar,0,wx.EXPAND)
        self.main_sizer.Add(self.element_sizer,1,wx.EXPAND)


        self.scrolled_panel.SetSizer(self.main_sizer)                   
        panel_sizer.Add(self.scrolled_panel, 1, wx.EXPAND)

        # Setting sizer and init layout
        self.InitUI(OfertaService().GetOffers())
        self.panel.SetSizer(panel_sizer)
        self.panel.Layout()

    #----------------------------------------------------------------------
    def InitUI(self,data): #data Oferta{nazwa:"string",date:"DateTime",id:int}
        self.displayOfferList(data)
       

    def displayOfferList(self,data):
        self.element_sizer.Clear(True)
        for oferta in data:
            if oferta.id != self.OFFER_TEMPLATE_ID:
                label_el = wx.Button(parent=self.scrolled_panel,label=(oferta.value1+"  "+oferta.date.strftime("%m/%d/%Y")))
                label_el.Bind(wx.EVT_BUTTON,lambda event,id=oferta.id: self.OpenOffer(event,id))
                self.element_sizer.Add(label_el,0,wx.EXPAND)
        self.panel.Layout()
    #----------------------------------------------------------------------
    def serachBarTextChange(self,event):
        self.displayOfferList(OfertaService().GetOffers(self.serachBar.GetValue()))
        
    #----------------------------------------------------------------------
    def OfferConfiguration(self,event):
        """
        Open configuration offer. Configuration Offer is template, every new offer will extend from this template
        """
        offer.OfferForm(self.OFFER_TEMPLATE_ID).Show()
        self.Hide()
        self.Close()
        self.Destroy()
    #----------------------------------------------------------------------
    def OpenOffer(self,event,id_oferta):
        offer.OfferForm(id_oferta).Show()
        self.Hide()
        self.Close()
        self.Destroy()
    #----------------------------------------------------------------------
    def AddOffer(self, event):
        offer.OfferForm().Show()
        self.Hide()
        self.Close()
        self.Destroy()
    #----------------------------------------------------------------------

# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm().Show()
    app.MainLoop()