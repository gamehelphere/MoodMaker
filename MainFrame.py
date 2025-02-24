#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.1.0 on Tue Jan  7 11:29:23 2025
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade

from MaterializeMood import MaterializeMood

class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((664, 466))
        self.SetTitle("Daily Mood Maker Program")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        label_title = wx.StaticText(self.panel_1, wx.ID_ANY, "Mood Maker Program", style=wx.ALIGN_CENTER_HORIZONTAL)
        label_title.SetBackgroundColour(wx.Colour(255, 255, 0))
        label_title.SetForegroundColour(wx.Colour(50, 50, 204))
        label_title.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "System-ui"))
        sizer_1.Add(label_title, 0, wx.EXPAND, 0)

        label_mood = wx.StaticText(self.panel_1, wx.ID_ANY, "\n\n\n\nPress 'Start' button to begin.", style=wx.ALIGN_CENTER_HORIZONTAL | wx.ST_NO_AUTORESIZE)
        #label_mood = wx.StaticText(self.panel_1, wx.ID_ANY, "textMood", style=wx.ALIGN_CENTER | wx.ST_NO_AUTORESIZE)
        label_mood.SetBackgroundColour(wx.Colour(255, 255, 255))
        label_mood.SetFont(wx.Font(16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, 0, ""))
        label_mood.Wrap(100)
        sizer_1.Add(label_mood, 4, wx.ALL | wx.EXPAND, 5)
        #sizer_1.Add(label_mood, proportion = 1)

        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 8)

        self.button_start = wx.Button(self.panel_1, wx.ID_ANY, "Start")
        sizer_2.Add(self.button_start, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.button_exit = wx.Button(self.panel_1, wx.ID_ANY, "Exit")
        sizer_2.Add(self.button_exit, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()
        self.Centre()
        
        self.button_start.Bind(wx.EVT_BUTTON, self.button_start_click)
        self.button_exit.Bind(wx.EVT_BUTTON, self.button_exit_click)
                
        # end wxGlade
        
        self._materializeMood = MaterializeMood()
        self._label_mood = label_mood

    def button_start_click(self, event):  # wxGlade: MainFrame.<event_handler>
        #print("Event handler 'button_start_click' not implemented!")
        self._label_mood.SetLabel(self._materializeMood.makeMood())
        event.Skip()

    def button_exit_click(self, event):  # wxGlade: MainFrame.<event_handler>
        self.Close(True)

# end of class MainFrame


