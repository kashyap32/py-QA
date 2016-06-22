import wx
import wikipedia
import os
import pyttsx
import wolframalpha
os.system("espeak 'welcome'")
app_id = "KEY" 
client = wolframalpha.Client(app_id)


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="PyDa")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        engine = pyttsx.init()
        voices = engine.getProperty('voices')

        engine.setProperty('voice', voices[0].id)

        input = self.txt.GetValue()
        input = input.lower()
        try:
        	res = client.query(input)
        	answer = next(res.results).text
        	print answer
                #os.system("espeak 'Theansweris'+str(answer)")
                engine.say(answer)
                engine.runAndWait()


       	except:
       		try:
       			input = input.split(' ')
       			input = ' '.join(input[2:])
       			answer1= wikipedia.summary(input)
       			print answer1
                        engine.say(answer1)
                        engine.runAndWait()


       		except:
       			print "I don't know"


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
