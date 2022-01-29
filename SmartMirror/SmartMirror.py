import tkinter as tk

class SmartMirror(tk.Frame):

	def __init__(self,
		         master=None, 
		         weather=None, 
		         calendar=None, 
		         quote=None, 
		         word=None,
		         time=None, 
		         date=None):

		tk.Frame.__init__(self,master,bg='black')
		self.master = master
		self.weather=weather
		self.calendar=calendar
		self.quote=quote
		self.word = word
		self.time=time
		self.date=date
		self.place(relwidth=1,relheight=1)
		self.formatData()

	def formatData(self):

		weatherLabel = tk.Label(self, text=self.weather, bg='black', fg='white')
		weatherLabel.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.1)

		calendarLabel = tk.Label(self, text=self.calendar, bg='black', fg='white')
		calendarLabel.place(relx=0.1, rely=0.2, relwidth=0.2, relheight=0.1)

		quoteLabel = tk.Label(self, text=self.quote, bg='black', fg='white')
		quoteLabel.place(relx=0.7, rely=0.7, relwidth=0.2, relheight=0.1)

		timeLabel = tk.Label(self, text=self.time, bg='black', fg='white')
		timeLabel.place(relx=0.1, rely=0.7, relwidth=0.2, relheight=0.1)

		dateLabel = tk.Label(self, text=self.date, bg='black', fg='white')
		dateLabel.place(relx=0.1, rely=0.8, relwidth=0.2, relheight=0.1)

		wordLabel = tk.Label(self, text=self.word, bg='black', fg='white')
		wordLabel.place(relx=0.7, rely=0.8, relwidth=0.2, relheight=0.1)



