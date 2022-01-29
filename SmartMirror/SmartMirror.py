import tkinter as tk

class SmartMirror(tk.Frame):

	def __init__(self,
		         master=None, 
		         weather=None, 
		         calendar=None, 
		         quote=None, 
		         time=None, 
		         date=None):

		tk.Frame.__init__(self,master)
		self.master = master
		self.place(relwidth=1,relheight=1)

		text = tk.Label(self, text="Just do it")
		text.place(x=70,y=90)


root = tk.Tk()
smartMirror = SmartMirror(root)
root.mainloop()