import wx



class DodatkiView(wx.Panel):

    def __init__(self,value1=None,value2=None,cena=None,parent=None,UpdateLayout=None,**kwargs):
        super(DodatkiView,self).__init__(parent=parent,**kwargs)
        self.UpdateLayout = UpdateLayout
        self.InitUI()
        if value1:
            self.value1.SetLabel(str(value1))
        if value2:
            self.value2.SetLabel(str(value2))
        if cena:
            self.cenaZL2.SetLabel(str(cena))
        self.UpdateLayout()

        #Dialog
        self.remove_offer_dlg = wx.MessageDialog(self.Parent, "Czy na pewno chcesz usunąć dodatek", "Usuń Dodatek",wx.YES_NO)
        self.remove_offer_dlg.SetYesNoLabels("&Tak", "&Nie")

    def InitUI(self):
        self.value1 =     wx.TextCtrl(parent=self)
        self.value2 =            wx.TextCtrl(parent=self)
        self.cenaZL2 =          wx.TextCtrl(parent=self)


        self.data_sizer =             wx.GridSizer(2)
        #gs.SetSize(800,500)
        self.data_sizer.AddMany([
            (wx.StaticText(self,label="Wartość 1"),1, wx.EXPAND),(self.value1,        1, wx.EXPAND),
            (wx.StaticText(self,label="Wartość 2"),1, wx.EXPAND),(self.value2,       1, wx.EXPAND),
            (wx.StaticText(self,label="Cena "),1, wx.EXPAND),(self.cenaZL2,1, wx.EXPAND)])

        self.main_sizer = wx.GridSizer(2)
        remove_btn = wx.Button(self,label="Usuń")
        self.Bind(wx.EVT_BUTTON, self.RemoveDodatek)

        self.main_sizer.Add(self.data_sizer,0,wx.EXPAND)
        self.main_sizer.Add(remove_btn,0,wx.EXPAND)
        self.SetSizerAndFit(self.main_sizer)
        self.main_sizer.Layout()
    #----------------------------------------------------------------------
    def RemoveDodatek(self, event):
        if self.remove_offer_dlg.ShowModal() == wx.ID_YES:
            self.Destroy()
            self.UpdateLayout()


        
