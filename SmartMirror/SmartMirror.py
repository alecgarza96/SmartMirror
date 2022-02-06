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
		self.formatData()

	def formatData(self):

		weatherLabel = tk.Label(self, text=self.weather, bg='black', fg='white')
		weatherLabel.place(relx=0.01, rely=0.1, relwidth=0.2, relheight=0.1)

		quoteLabel = tk.Label(self, text=self.quote, bg='black', fg='white')
		quoteLabel.place(relx=0.25, rely=0.65, relwidth=0.5, relheight=0.5)

		timeLabel = tk.Label(self, text=self.time, bg='black', fg='white')
		timeLabel.place(relx=0.8, rely=0.1, relwidth=0.2, relheight=0.1)

		dateLabel = tk.Label(self, text=self.date, bg='black', fg='white')
		dateLabel.place(relx=0.65, rely=0.2, relwidth=0.5, relheight=0.1)

		focusHeader = tk.Label(self, text="Focus", bg='black', fg='white')
		focusHeader.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.5)

		focusLabel = tk.Label(self, text=self.focus, bg='black', fg='white')
		focusLabel.place(relx=0.25, rely=0.30, relwidth=0.5, relheight=0.5)



