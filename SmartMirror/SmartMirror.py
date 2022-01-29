import tkinter as tk

class SmartMirror(tk.Frame):

	def __init__(self,
		         master=None, 
		         weather=None, 
		         calendar=None, 
		         quote=None, 
		         time=None, 
		         date=None):

		tk.Frame.__init__(self,master,bg='black')
		self.master = master
		self.weather=weather
		self.calendar=calendar
		self.quote=quote
		self.time=time
		self.date=date
		self.place(relwidth=1,relheight=1)
		

		weatherLabel = tk.Label(self, text=self.weather, bg='black', fg='white')
		weatherLabel.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.1)

		calendarLabel = tk.Label(self, text=self.calendar, bg='black', fg='white')
		calendarLabel.place(relx=0.1, rely=0.2, relwidth=0.2, relheight=0.1)

		quoteLabel = tk.Label(self, text=self.quote, bg='black', fg='white')
		quoteLabel.place(relx=0.7, rely=0.7, relwidth=0.2, relheight=0.1)



root = tk.Tk()
canvas = tk.Canvas(root, height=800, width=900)
canvas.pack()

smartMirror = SmartMirror(root,"98","walk","good job","8:30","February 1st")
root.mainloop()