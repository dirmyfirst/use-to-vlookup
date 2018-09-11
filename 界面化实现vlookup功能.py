import wx
import wx.xrc
import pandas as pd
import time
import os


class MyFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = '两表相同数据查找合并', pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )				
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, "数据表1:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, "数据表2:", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_staticText1.Wrap( -1 )
		self.m_staticText2.Wrap( -1 )
		
		bSizer3.Add( self.m_staticText1, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		bSizer4.Add( self.m_staticText2, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, "Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.m_filePicker1.GetPickerCtrl().SetLabel("选择文件")
		
		self.m_filePicker2 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, "Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.m_filePicker2.GetPickerCtrl().SetLabel("选择文件")
		
		bSizer3.Add( self.m_filePicker1, 9, wx.ALIGN_CENTER|wx.ALL, 5 )
		bSizer4.Add( self.m_filePicker2, 9, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
		bSizer1.Add( bSizer5, 2, wx.EXPAND, 5 )
			
		self.m_button2 = wx.Button( self, wx.ID_ANY, "开始查找合并", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button2, 0, wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, size=(375, 240), style=wx.TE_MULTILINE | wx.HSCROLL )
		bSizer5.Add( self.m_textCtrl3, 0, wx.ALL|wx.BOTTOM|wx.EXPAND, 5 )

		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		self.m_button2.Bind( wx.EVT_BUTTON, self.begin )		

	
	def __del__( self ):
		pass
	
	def begin( self, event ):
		event.Skip()
		self.get_file_name1 = self.m_filePicker1.GetTextCtrl().GetValue()
		self.get_file_name2 = self.m_filePicker2.GetTextCtrl().GetValue()

		self.file_path1 = open(self.get_file_name1)
		self.file_path2 = open(self.get_file_name2)

		self.file_name1 = pd.read_csv(self.file_path1)
		self.file_name2 = pd.read_csv(self.file_path2)

		self.file_name11 = self.file_name1.rename(columns = {self.file_name1.columns[0]:'columns'})
		self.file_name12 = self.file_name2.rename(columns = {self.file_name2.columns[0]:'columns'})
		
		self.file3 = pd.merge(self.file_name11, self.file_name12, left_on = self.file_name11.columns[0], right_on = self.file_name12.columns[0], how='left')

		to_name = '合并后数据.csv'
		self.file3.to_csv(to_name, index = False)
		
		self.m_textCtrl3.AppendText(f'{self.get_file_name1}与' + '\n' + f'{self.get_file_name2}合并完成!' + '\n')
		self.m_textCtrl3.AppendText(f'生成的文件位于:' + '\n' + f'{os.path.join(os.getcwd(),to_name)}')
		
	

app = wx.App(False)
frame = MyFrame(None)
frame.Show(True)
app.MainLoop()

