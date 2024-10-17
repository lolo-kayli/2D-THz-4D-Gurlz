#!/usr/bin/env python
# coding: utf-8

# In[27]:


import tkinter as tk
from tkinter import *
from tkinter import ttk,filedialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg , NavigationToolbar2Tk


# In[28]:


#creates a main window
main = tk.Tk()
main.title("2D Terahertz 4D Gurlz")
# Set geometry (widthxheight)
main.geometry('350x200')


# In[29]:


#Create the tabs for the oscilliscope,and scanning controls
tabControl = ttk.Notebook(main)
osc = ttk.Frame(tabControl)
scan = ttk.Frame(tabControl)
tabControl.add(osc, text='Ocilliscope')
tabControl.add(scan, text='Scan')
tabControl.pack(expand = 1, fill ="both") 


# In[30]:


#Working on the oscilliscope tab
wavplte = Label(osc, text = "λ/4 Angle : ")
wavplte.grid()
wavplte_txt = Entry(osc, width=10)
wavplte_txt.grid(column =1, row =0)

znte = Label(osc, text = "ZnTe Angle : ")
znte.grid(column = 2, row =0)
znte_txt = Entry(osc, width=10)
znte_txt.grid(column = 3, row =0)

sampl = Label(osc, text = "Sample Angle : ")
sampl.grid(column = 4, row =0)
sampl_txt = Entry(osc, width=10)
sampl_txt.grid(column = 5, row =0)


# In[31]:


fig = plt.Figure(figsize = (5, 5), dpi = 100) 
y = [i**2 for i in range(101)] 
plot1 = fig.add_subplot(111) 
plot1.plot(y) 
canvas = FigureCanvasTkAgg(fig, master=osc)
canvas.draw()
canvas.get_tk_widget().grid(column = 3, row = 2)
toolbar_frame = ttk.Frame(osc)
toolbar_frame.grid(column = 3, row = 3)
toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
toolbar.update()
canvas.get_tk_widget().grid(column = 3, row = 2)


# In[32]:


#Working on the scanning tab
scan_indicator = Label(scan, text = "SCANNING IN PROGRESS " , fg = 'black', font = ("Helvetica",24,"bold"))
scan_indicator.grid()

fig = plt.Figure(figsize = (5, 5), dpi = 100) 
y = [i**2 for i in range(101)] 
plot1 = fig.add_subplot(111) 
plot1.plot(y) 
canvas = FigureCanvasTkAgg(fig, master=scan)
canvas.draw()
canvas.get_tk_widget().grid(column = 0, row = 2)
toolbar_frame = ttk.Frame(scan)
toolbar_frame.grid(column = 0, row = 3)
toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
toolbar.update()
canvas.get_tk_widget().grid(column = 0, row = 2)

scan_num = Label(scan, text = "# of scans")
scan_num.grid(column =2, row =0)
scan_num_txt = Entry(scan, width=10)
scan_num_txt.grid(column =2, row =1)
                 
mpp = Label(scan, text = "# measurements/position")
mpp.grid(column =2, row =2)
mpp_txt = Entry(scan, width=10)
mpp_txt.grid(column =2, row =3)
            
stps = Label(scan, text = "step size")
stps.grid(column =2, row =4)
stps_txt = Entry(scan, width=10)
stps_txt.grid(column =2, row =5)


# In[33]:


drct = Label(scan, text = "{location}".format(location = " "))
drct.grid(column =1, row =4)

def select_directory():
    # Open a dialog to select a directory
    directory = filedialog.askdirectory(title="Select Directory")
    
    if directory:
        drct = Label(scan, text = "{location}".format(location = str(directory)))
    else:
        messagebox.showwarning("No Selection", "No directory was selected.")

btn = ttk.Button(scan, text = 'Select Save Location', command = select_directory()) 
btn.grid(column = 0, row = 4)


# In[ ]:


main.mainloop()


# In[ ]:




