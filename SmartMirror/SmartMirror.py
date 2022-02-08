import tkinter as tk

class SmartMirror(tk.Frame):

	def __init__(self,
		         master=None, 
		         weather=None, 
		         quote=None, 
		         time=None, 
		         date=None,
		         focus=None):

		tk.Frame.__init__(self,master,bg='black')
		self.master = master
		self.weather=weather
		self.quote=quote
		self.time=time
		self.date=date
		self.focus=focus
		self.place(relwidth=1,relheight=1)
		self.weatherLabel = None
		self.quoteLabel = None
		self.timeLabel = None
		self.dateLabel = None
		self.focusHeader = None
		self.focusLabel = None
		self.formatLabels()

	def formatLabels(self):

		self.weatherLabel = tk.Label(self, text=self.weather, bg='black', fg='white')
		self.weatherLabel.place(relx=0.01, rely=0.1, relwidth=0.2, relheight=0.1)

		self.quoteLabel = tk.Label(self, text=self.quote, bg='black', fg='white')
		self.quoteLabel.place(relx=0.25, rely=0.65, relwidth=0.5, relheight=0.5)

		self.timeLabel = tk.Label(self, text=self.time, bg='black', fg='white')
		self.timeLabel.place(relx=0.8, rely=0.1, relwidth=0.2, relheight=0.1)

		self.dateLabel = tk.Label(self, text=self.date, bg='black', fg='white')
		self.dateLabel.place(relx=0.65, rely=0.2, relwidth=0.5, relheight=0.1)

		self.focusHeader = tk.Label(self, text="Focus", bg='black', fg='white')
		self.focusHeader.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.5)

		self.focusLabel = tk.Label(self, text=self.focus, bg='black', fg='white')
		self.focusLabel.place(relx=0.25, rely=0.30, relwidth=0.5, relheight=0.5)



