import wx
from MainFrame import MainFrame


class MoodMaker(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":

# Main Program

    moodMaker = MoodMaker(0)
    moodMaker.MainLoop()
