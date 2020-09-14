import wx
import wx.lib.scrolledpanel as scrolled
from view.element1 import Element1View
from view.element2 import Element2View
from view.element3 import Element3View
from view.element4 import Element4View
from view.element5 import Element5View
from model.oferta import OfertaService 
from view.oferta import OfertaView
import main
from view.umowa_pdf import generate_Umowa_PDF
from view.oferta_pdf import generate_Oferta_PDF
class OfferForm(wx.Frame):
    def __init__(self,oferta_id=None):
        wx.Frame.__init__(self, None, wx.ID_ANY, "ZHU Skoczylas Offer Creator", size=(1200,650),style=(wx.DEFAULT_FRAME_STYLE | wx.WANTS_CHARS))
        self.id_offer = oferta_id
        print(self.id_offer)
        self.panel = wx.Panel(self, wx.ID_ANY,size=(-1,50),pos=(0,0))
        self.OFFER_TEMPLATE_ID = 1
        # Setting up the menu.
        menu_bar = wx.MenuBar()
        
        oferta_Menu = wx.Menu()
        pdf_Menu = wx.Menu()
        # Creating the menu_bar.
        self.remove_offer_dlg = wx.MessageDialog(self, "Czy na pewno chcesz usunąć oferte", "Usuń Oferte",wx.YES_NO)
        self.remove_offer_dlg.SetYesNoLabels("&Tak", "&Nie")

        if oferta_id != self.OFFER_TEMPLATE_ID:
            add_elements_menu= wx.Menu()
            menu_add_Element1View = add_elements_menu.Append(wx.ID_ANY, "&Element1"," Dodaj Element1")
            menu_add_Element2View = add_elements_menu.Append(wx.ID_ANY, "&Element2"," Dodaj Element2")
            menu_add_Element3View = add_elements_menu.Append(wx.ID_ANY, "&Element3"," Dodaj Element3")
            menu_add_Element4View = add_elements_menu.Append(wx.ID_ANY, "&Element4"," Dodaj Element4")
            menu_add_Element5View = add_elements_menu.Append(wx.ID_ANY, "&Element5"," Dodaj Element5")
            menu_bar.Append(oferta_Menu,"&Oferta")
            remove_oferta = oferta_Menu.Append(wx.ID_ANY,'&Usuń','Usuń Oferte')
            self.Bind(wx.EVT_MENU, self.CreateElement1View, menu_add_Element1View)
            self.Bind(wx.EVT_MENU, self.CreateElement2View, menu_add_Element2View)
            self.Bind(wx.EVT_MENU, self.CreateElement3View, menu_add_Element3View)
            self.Bind(wx.EVT_MENU, self.CreateElement4View, menu_add_Element4View)
            self.Bind(wx.EVT_MENU, self.CreateElement5View, menu_add_Element5View)           
            
            self.Bind(wx.EVT_MENU, self.Remove, remove_oferta)      
            menu_bar.Append(add_elements_menu,"&Dodaj &Element") 



        save_oferta = oferta_Menu.Append(wx.ID_ANY,'&Zapisz','Zapisz Oferte')

        umowa_pdf = pdf_Menu.Append(wx.ID_ANY,"&Umowa","Generuj Umowe")
        ofeta_pdf = pdf_Menu.Append(wx.ID_ANY,"&Oferta","Generuj Oferte")

        
        
        menu_bar.Append(pdf_Menu,"&PDF")
        self.SetMenuBar(menu_bar) 

        
        # Set events to DodajElement menu

        # Set events to Oferta menu
        self.Bind(wx.EVT_MENU, self.Save, save_oferta)
        # Set events to pdf menu
        self.Bind(wx.EVT_MENU, self.OnSaveAsOferta, ofeta_pdf)
        self.Bind(wx.EVT_MENU, self.OnSaveAsUmowa, umowa_pdf)

        # Scrolled panel stuff
        self.scrolled_panel = scrolled.ScrolledPanel(self.panel, -1, pos=(20,50), style = wx.VSCROLL ,name="panel1")     
        #self.scrolled_panel.SetAutoLayout(1)
        self.scrolled_panel.SetupScrolling(scroll_x=False, scroll_y=True, scrollToTop=False,scrollIntoView=True)        
        self.element_sizer = wx.BoxSizer(wx.VERTICAL)
        self.element_sizer.SetMinSize(500,-1)
        self.scrolled_panel.SetSizer(self.element_sizer)

        #List Of ViewElements
        self.viewElements = list()
        self.element1_list = list()
        self.element2_list = list()
        self.element3_list = list()
        self.element4_list = list()
        self.element5_list = list()

        #Creating and binding Back Button
        self.back_button_Sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.backButton = wx.Button(parent=self.panel,label="Wyjdź",size=(100,50))
        self.save_back_button = wx.Button(parent=self.panel,label="Wyjdź i Zapisz",size=(100,50))      
        self.backButton.Bind(wx.EVT_BUTTON,self.Back)  
        self.save_back_button.Bind(wx.EVT_BUTTON,self.BackAndSave) 
        self.back_button_Sizer.Add(self.backButton,0, wx.FIXED_MINSIZE)
        self.back_button_Sizer.Add(self.save_back_button,0, wx.FIXED_MINSIZE)
        panel_Sizer = wx.BoxSizer(wx.VERTICAL)
        panel_Sizer.Add(self.back_button_Sizer,0,wx.EXPAND,border=5)
        panel_Sizer.Add(self.scrolled_panel, 1, wx.EXPAND,border=5)      

        # Create OfertaView Widget
        if oferta_id != None:
            if oferta_id == self.OFFER_TEMPLATE_ID:
                self.Render(OfertaService().GetOfferById(oferta_id),show_remove_button=False)
            else:
                self.Render(OfertaService().GetOfferById(oferta_id))
        else:
            self.oferta = OfertaView(self.scrolled_panel,default_offer=OfertaService().GetOfferById(self.OFFER_TEMPLATE_ID))
            self.viewElements.append(self.oferta)
            self.element_sizer.Add(self.oferta,0,  wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.panel.SetSizer(panel_Sizer)
        self.panel.Layout()

        #Set Events
        self.Bind(wx.EVT_SIZE,self.OnSize)
        self.Bind(wx.EVT_CHAR_HOOK, self.onKeyPress)

    #----------------------------------------------------------------------
    def onKeyPress(self,event):
        keycode = event.GetKeyCode()
        #315 Arrow UP
        #317 Arrow DOWN
        if keycode == 315 or keycode == 317:
            element = wx.Window.FindFocus()
            for x in range(len(self.viewElements)):                                             #}
                for y in range(len(self.viewElements[x].inputElements)):                        #Looking for element with focus
                    if self.viewElements[x].inputElements[y].GetId() == (element.GetId()):      #}
                        #Go down if it is possible
                        if keycode == 317:
                            if y == len(self.viewElements[x].inputElements)-1:# if it is last offer element 
                                if x < len(self.viewElements)-1:
                                    self.viewElements[x+1].inputElements[0].SetFocus()
                                    self.viewElements[x+1].inputElements[0].SetSelection(-1,-1)
                            else:   # if it is last control of offer element
                                self.viewElements[x].inputElements[y+1].SetFocus()
                                self.viewElements[x].inputElements[y+1].SetSelection(-1,-1)
                        else:
                            if y > 0:
                                self.viewElements[x].inputElements[y-1].SetFocus()
                                self.viewElements[x].inputElements[y-1].SetSelection(-1,-1)
                            else:
                                if x > 0:
                                    self.viewElements[x-1].inputElements[len(self.viewElements[x-1].inputElements)-1].SetFocus()
                                    self.viewElements[x-1].inputElements[len(self.viewElements[x-1].inputElements)-1].SetSelection(-1,-1)
        
        event.Skip()




    #----------------------------------------------------------------------
    def Remove(self,event):
        if self.remove_offer_dlg.ShowModal() == wx.ID_YES:
            if self.id_offer and self.id_offer != self.OFFER_TEMPLATE_ID:
                OfertaService().RemoveOffer(self.id_offer)
                self.Back()
            else: 
                self.Back()

    #----------------------------------------------------------------------
    def OnSize(self,event=None):
        children = self.element_sizer.GetChildren()
        for child in children:
            widget = child.GetWindow()
            widget.SetMinSize( (self.GetSize()[0]-50,(widget.GetSize()[1])))
        self.panel.SetSize( (self.GetSize()[0]-15,(self.GetSize()[1]-50)))
        self.panel.Layout()

    #----------------------------------------------------------------------
    def Back(self,event=None):
        main.MyForm().Show()
        self.Hide()
        self.Destroy()

    #----------------------------------------------------------------------
    def BackAndSave(self,event):
        self.Save(event)
        self.Back()

    #----------------------------------------------------------------------    
    def OnSaveAsUmowa(self, event):
        self.Save()
        with wx.FileDialog(self, "", wildcard="*.pdf",defaultFile= self.oferta.oferta.value1+"_"+self.oferta.oferta.value2+"_"+str(self.oferta.oferta.date)+"_Umowa.pdf",
                        style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return   

            pathname = fileDialog.GetPath()       
            generate_Umowa_PDF(OfertaService().GetOfferById(self.id_offer),pathname)

    #----------------------------------------------------------------------    
    def OnSaveAsOferta(self, event):
        self.Save()
        with wx.FileDialog(self, "", wildcard="*.pdf",defaultFile= self.oferta.oferta.value1+"_"+self.oferta.oferta.value2+"_"+str(self.oferta.oferta.date)+"_Oferta.pdf",

                        style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return    

            pathname = fileDialog.GetPath()
            generate_Oferta_PDF(OfertaService().GetOfferById(self.id_offer),pathname)
    #----------------------------------------------------------------------
    def RefreshLayout(self):
        self.scrolled_panel.Layout()
        self.scrolled_panel.FitInside()
        self.OnSize()
    def AddElementToLayout(self,element):
        self.element_sizer.Add(element,0,  wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.viewElements.append(element)
        self.RefreshLayout()
    #----------------------------------------------------------------------
    def CreateElement1View(self, event):
        element1 = Element1View(self.scrolled_panel,default_offer=OfertaService().GetOfferById(self.OFFER_TEMPLATE_ID).element1[0])
        self.AddElementToLayout(element1)
        self.element1_list.append(element1)
    #----------------------------------------------------------------------
    def CreateElement5View(self, event):
        element5 = Element5View(self.scrolled_panel,default_offer=OfertaService().GetOfferById(self.OFFER_TEMPLATE_ID).element5[0])
        self.AddElementToLayout(element5)
        self.element1_list.append(element5)

    #----------------------------------------------------------------------   
    def CreateElement4View(self, event):
        element4 = Element4View(self.scrolled_panel,default_offer=OfertaService().GetOfferById(self.OFFER_TEMPLATE_ID).element4[0])
        self.AddElementToLayout(element4)
        self.element3_list.append(element4)


    #----------------------------------------------------------------------
    def CreateElement2View(self, event):
        bvalue7 = Element2View(self.scrolled_panel,default_offer=OfertaService().GetOfferById(self.OFFER_TEMPLATE_ID).element2[0])
        self.AddElementToLayout(bvalue7)
        self.element2_list.append(bvalue7)

    #----------------------------------------------------------------------
    def CreateElement3View(self, event):
        element3 = Element3View(self.scrolled_panel,default_offer=OfertaService().GetOfferById(self.OFFER_TEMPLATE_ID).element3[0])
        self.AddElementToLayout(element3)
        self.element4_list.append(element3)

    #----------------------------------------------------------------------
    def Save(self,event=None):
        self.oferta.oferta = self.oferta.service.EditOffer(self.oferta.GetData())
        self.oferta.id_oferta = self.oferta.oferta.id
        self.edit_every_el_from_list(self.element1_list)
        self.edit_every_el_from_list(self.element2_list)
        self.edit_every_el_from_list(self.element3_list)
        self.edit_every_el_from_list(self.element4_list)
        self.edit_every_el_from_list(self.element5_list)
        
    def edit_every_el_from_list(self,elementList):
        for el in elementList:
            if el:
                self.oferta.service.EditOfferElement(el.GetData())   

    #----------------------------------------------------------------------
    def Render(self, oferta_dane , show_remove_button = True):
        self.oferta = OfertaView(self.scrolled_panel,oferta_dane)
        self.viewElements.append(self.oferta)
        self.element_sizer.Add(self.oferta,0,  wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5)

        for e1 in oferta_dane.element1:
            Element1_view = Element1View(parent=self.scrolled_panel,data_representation=e1 ,show_remove_button=show_remove_button)            
            self.element_sizer.Add(Element1_view ,0,  wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5)
            self.element1_list.append(Element1_view)
            self.viewElements.append(Element1_view)

        for e2 in oferta_dane.element2:
            Element2_view = Element2View(parent=self.scrolled_panel,data_representation=e2 ,show_remove_button=show_remove_button)            
            self.element_sizer.Add(Element2_view ,0,  wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5)
            self.element2_list.append(Element2_view)
            self.viewElements.append(Element2_view)

        for e3 in oferta_dane.element3:
            Element3_view = Element3View(parent=self.scrolled_panel,data_representation=e3 ,show_remove_button=show_remove_button)            
            self.element_sizer.Add(Element3_view ,0,  wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5)
            self.element3_list.append(Element3_view)
            self.viewElements.append(Element3_view)

        for e4 in oferta_dane.element4:
            Element4_view = Element1View(parent=self.scrolled_panel,data_representation=e4 ,show_remove_button=show_remove_button)            
            self.element_sizer.Add(Element4_view ,0,  wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5)
            self.element4_list.append(Element4_view)
            self.viewElements.append(Element4_view)

        for e5 in oferta_dane.element5:
            Element5_view = Element5View(parent=self.scrolled_panel,data_representation=e5 ,show_remove_button=show_remove_button)            
            self.element_sizer.Add(Element5_view ,0,  wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5)
            self.element5_list.append(Element5_view)
            self.viewElements.append(Element5_view)



        self.scrolled_panel.Layout()
        self.scrolled_panel.FitInside()   

   