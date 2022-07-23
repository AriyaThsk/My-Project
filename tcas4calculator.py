import numpy as np
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from tkinter import *
from tkinter import ttk  # ttk -> themed tk (for Combobox)
import pandas as pd

window = Tk()
window.title("TCAS Round 4 scores calculator for MU")
window.geometry("750x1000")

lbl0 = Label(window,text = "GPAX")
lbl0.grid(column=0,row=1)
txt0 = Entry(window,width=10)
txt0.grid(column=1,row=1)

lbl1 = Label(window,text = "กรุณากรอกคะแนนของคุณ\nหากช่องใดไม่มีให้ใส่เครื่องหมาย -")
lbl1.grid(column=0,row=0)

lbl2 = Label(window,text = "O-NET")
lbl2.grid(column=0,row=2)

lbl3 = Label(window,text = "ภาษาไทย")
lbl3.grid(column=0,row=3)
txt1 = Entry(window,width=10)
txt1.grid(column=1,row=3)

lbl4 = Label(window,text ="สังคมศึกษา")
lbl4.grid(column=0,row=4)
txt2 = Entry(window,width=10)
txt2.grid(column=1,row=4)

lbl5 = Label(window,text ="ภาษาอังกฤษ")
lbl5.grid(column=0,row=5)
txt3 = Entry(window,width=10)
txt3.grid(column=1,row=5)

lbl6 = Label(window,text ="คณิตศาสตร์")
lbl6.grid(column=0,row=6)
txt4 = Entry(window,width=10)
txt4.grid(column=1,row=6)

lbl7 = Label(window,text ="วิทยาศาสตร์")
lbl7.grid(column=0,row=7)
txt5 = Entry(window,width=10)
txt5.grid(column=1,row=7)

lbl8 = Label(window,text = "GAT/PAT")
lbl8.grid(column=0,row=8)

lbl9 = Label(window,text = "GAT")
lbl9.grid(column=0,row=9)
txt6 = Entry(window,width=10)
txt6.grid(column=1,row=9)

lbl10 = Label(window,text = "PAT 1")
lbl10.grid(column=0,row=10)
txt7 = Entry(window,width=10)
txt7.grid(column=1,row=10)

lbl11 = Label(window,text = "PAT 2")
lbl11.grid(column=0,row=11)
txt8 = Entry(window,width=10)
txt8.grid(column=1,row=11)

lbl12 = Label(window,text = "PAT 3")
lbl12.grid(column=0,row=12)
txt9 = Entry(window,width=10)
txt9.grid(column=1,row=12)

lbl13 = Label(window,text = "PAT 4")
lbl13.grid(column=0,row=13)
txt10 = Entry(window,width=10)
txt10.grid(column=1,row=13)

lbl14 = Label(window,text = "PAT 5")
lbl14.grid(column=0,row=14)
txt11 = Entry(window,width=10)
txt11.grid(column=1,row=14)

lbl15 = Label(window,text = "PAT 6")
lbl15.grid(column=0,row=15)
txt12 = Entry(window,width=10)
txt12.grid(column=1,row=15)

lbl16 = Label(window,text = "PAT 7")
lbl16.grid(column=0,row=16)
txt13 = Entry(window,width=10)
txt13.grid(column=1,row=16)


faculty_list = ['คณะเภสัชศาสตร์','คณะสาธารณสุขศาสตร์','คณะเทคนิคการแพทย์ สาขาเทคนิคการแพทย์','คณะกายภาพบำบัด สาขากายภาพบำบัด',
                'คณะพยาบาลศาสตร์','คณะแพทยศาสตร์โรงพยาบาลรามาธิบดี สาขาพยาบาลศาสตร์','คณะวิทยาศาสตร์','คณะสิ่งแวดล้อมและทรัพยากรศาสตร์','คณะเทคโนโลยีสารสนเทศและการสื่อสาร',
                'คณะวิศวกรรมศาสตร์ สาขาวิชาวิศวกรรมไฟฟ้า','คณะศิลปศาสตร์ สาขาวิชาภาษาอังกฤษ','วิทยาลัยศาสนศึกษา']


lbl17 = Label(window,text = "เลือกคณะที่ต้องการให้คำนวณคะแนน")
lbl17.grid(column=1,row=21)

cbo1 = ttk.Combobox(window,value=faculty_list,state="readonly",width=45)
cbo1.grid(column=1,row=22)
cbo1.current(0)

lbl18 = Label(window,text = "เลือกคณะที่1")
lbl18.grid(column=0,row=22)

cbo2 = ttk.Combobox(window,value=faculty_list,state="readonly",width=45)
cbo2.grid(column=1,row=23)
cbo2.current(1)

lbl19 = Label(window,text = "เลือกคณะที่2")
lbl19.grid(column=0,row=23)

df1 = pd.read_csv('highest.csv')
df2 = pd.read_csv('lowest.csv')

def calculate():
        
    if cbo1.get() == faculty_list[0]: #PY
        
        if (float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))<300:
            lbl20.configure(text = "คะแนนของคุณไม่ผ่านเกณฑ์")
        elif txt8.get() == "-":
            lbl20.configure(text = "คุณมีคะแนนไม่ครบตามเกณฑ์")
        else :
            gpax = (float(txt0.get())/4)*6000
            onet = ((float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))/500)*9000
            gat = float(txt6.get())/300*3000
            pat = float(txt8.get())/300*12000
            result = gpax + onet + gat + pat
            lbl20.configure(text = result)
            
            fig = Figure(figsize=(4,3), dpi=60)
            fig.add_subplot().plot(df1['fac'], df1['PY'])
            fig.add_subplot().plot(df2['fac'], df2['PY'])
            fig.add_subplot().scatter(df1['fac'], df1['PY'])
            fig.add_subplot().scatter(df2['fac'], df2['PY'])
            fig.add_subplot().plot(df2['fac'],np.array([result,result]))
            fig.add_subplot().scatter(df2['fac'],np.array([result,result]))
            
            canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().grid(column=1,row=33)
               
    if cbo1.get() == faculty_list[1]: #PH
        
        if (float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))<150:
            lbl20.configure(text = "คะแนนของคุณไม่ผ่านเกณฑ์")
        elif txt8.get() == "-":
            lbl20.configure(text = "คุณมีคะแนนไม่ครบตามเกณฑ์")
        else :
            gpax = (float(txt0.get())/4)*6000
            onet = ((float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))/500)*9000
            gat = (float(txt6.get())/300)*6000
            pat = (float(txt8.get())/300)*9000
            result = gpax + onet + gat + pat
            lbl20.configure(text = result)
            
            fig = Figure(figsize=(4,3), dpi=60)
            fig.add_subplot().plot(df1['fac'], df1['PH'])
            fig.add_subplot().plot(df2['fac'], df2['PH'])
            fig.add_subplot().scatter(df1['fac'], df1['PH'])
            fig.add_subplot().scatter(df2['fac'], df2['PH'])
            fig.add_subplot().plot(df2['fac'],np.array([result,result]))
            fig.add_subplot().scatter(df2['fac'],np.array([result,result]))
            
            canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().grid(column=1,row=33)
            
         
    if cbo1.get() == faculty_list[2]: #MT
        if float(txt1.get())<45 or float(txt2.get())<40 or float(txt3.get())<35 or float(txt4.get())<35 or float(txt5.get())<40 or (float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))<200:
            lbl20.configure(text = "คะแนนของคุณไม่ผ่านเกณฑ์")
        elif txt8.get() == "-":
            lbl20.configure(text = "คุณมีคะแนนไม่ครบตามเกณฑ์")
        else:
            gpax = (float(txt0.get())/4)*6000
            onet = ((float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))/500)*9000
            gat = (float(txt6.get())/300)*6000
            pat = (float(txt8.get())/300)*9000
            result = gpax + onet + gat + pat
            lbl20.configure(text = result)
            
            fig = Figure(figsize=(4,3), dpi=60)
            fig.add_subplot().plot(df1['fac'], df1['MT'])
            fig.add_subplot().plot(df2['fac'], df2['MT'])
            fig.add_subplot().scatter(df1['fac'], df1['MT'])
            fig.add_subplot().scatter(df2['fac'], df2['MT'])
            fig.add_subplot().plot(df2['fac'],np.array([result,result]))
            fig.add_subplot().scatter(df2['fac'],np.array([result,result]))
            
            canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().grid(column=1,row=33)
        
            
    if cbo1.get() == faculty_list[3]: #PT
        
        if (float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))<150:
            lbl20.configure(text = "คะแนนของคุณไม่ผ่านเกณฑ์")
        elif txt8.get() == "-":
            lbl20.configure(text = "คุณมีคะแนนไม่ครบตามเกณฑ์")
        else:
            gpax = (float(txt0.get())/4)*6000
            onet = ((float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))/500)*9000
            gat = (float(txt6.get())/300)*6000
            pat = (float(txt8.get())/300)*9000
            result = gpax + onet + gat + pat
            lbl20.configure(text = result)
            
            fig = Figure(figsize=(4,3), dpi=60)
            fig.add_subplot().plot(df1['fac'], df1['PT'])
            fig.add_subplot().plot(df2['fac'], df2['PT'])
            fig.add_subplot().scatter(df1['fac'], df1['PT'])
            fig.add_subplot().scatter(df2['fac'], df2['PT'])
            fig.add_subplot().plot(df2['fac'],np.array([result,result]))
            fig.add_subplot().scatter(df2['fac'],np.array([result,result]))
            
            canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().grid(column=1,row=33)
        
    
    if cbo1.get() == faculty_list[4]: #NS
        
        if float(txt1.get())<30 or float(txt2.get())<30 or float(txt3.get())<30 or float(txt4.get())<30 or float(txt5.get())<30 or float(txt6.get())<90 or float(txt8.get())<60:
            lbl20.configure(text = "คะแนนของคุณไม่ผ่านเกณฑ์")
        elif txt8.get() == "-":
            lbl20.configure(text = "คุณมีคะแนนไม่ครบตามเกณฑ์")
        else:
            gpax = (float(txt0.get())/4)*6000
            onet = ((float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))/500)*9000
            gat = (float(txt6.get())/300)*6000
            pat = (float(txt8.get())/300)*9000
            result = gpax + onet + gat + pat
            lbl20.configure(text = result)
            
            fig = Figure(figsize=(4,3), dpi=60)
            fig.add_subplot().plot(df1['fac'], df1['NS'])
            fig.add_subplot().plot(df2['fac'], df2['NS'])
            fig.add_subplot().scatter(df1['fac'], df1['NS'])
            fig.add_subplot().scatter(df2['fac'], df2['NS'])
            fig.add_subplot().plot(df2['fac'],np.array([result,result]))
            fig.add_subplot().scatter(df2['fac'],np.array([result,result]))
            
            canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().grid(column=1,row=33)
       
    
    if cbo1.get() == faculty_list[5]: #NR
        
        if float(txt3.get())<30:
            lbl20.configure(text = "คะแนนของคุณไม่ผ่านเกณฑ์")
        elif txt8.get() == "-":
            lbl20.configure(text = "คุณมีคะแนนไม่ครบตามเกณฑ์")
        else:
            gpax = (float(txt0.get())/4)*6000
            onet = ((float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))/500)*9000
            gat = (float(txt6.get())/300)*6000
            pat = (float(txt8.get())/300)*9000
            result = gpax + onet + gat + pat
            lbl20.configure(text = result)
            
            fig = Figure(figsize=(4,3), dpi=60)
            fig.add_subplot().plot(df1['fac'], df1['NR'])
            fig.add_subplot().plot(df2['fac'], df2['NR'])
            fig.add_subplot().scatter(df1['fac'], df1['NR'])
            fig.add_subplot().scatter(df2['fac'], df2['NR'])
            fig.add_subplot().plot(df2['fac'],np.array([result,result]))
            fig.add_subplot().scatter(df2['fac'],np.array([result,result]))
            
            canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().grid(column=1,row=33)
 
           
    if cbo1.get() == faculty_list[6]: #SC
    
        if float(txt1.get())<30 or float(txt2.get())<30 or float(txt3.get())<30 or float(txt4.get())<30 or float(txt5.get())<30:
            lbl20.configure(text = "คะแนนของคุณไม่ผ่านเกณฑ์")
        elif txt7.get() == "-" or txt8.get() == "-":
            lbl20.configure(text = "คุณมีคะแนนไม่ครบตามเกณฑ์")
        else:
            gpax = (float(txt0.get())/4)*6000
            onet = ((float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))/500)*9000
            gat = float(txt6.get())/300*3000
            pat = float(txt7.get())/300*3000 + float(txt8.get())/300*9000
            result = gpax + onet + gat + pat
            lbl20.configure(text = result)
            
            fig = Figure(figsize=(4,3), dpi=60)
            fig.add_subplot().plot(df1['fac'], df1['SC'])
            fig.add_subplot().plot(df2['fac'], df2['SC'])
            fig.add_subplot().scatter(df1['fac'], df1['SC'])
            fig.add_subplot().scatter(df2['fac'], df2['SC'])
            fig.add_subplot().plot(df2['fac'],np.array([result,result]))
            fig.add_subplot().scatter(df2['fac'],np.array([result,result]))
            
            canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().grid(column=1,row=33)
            
    
    if cbo1.get() == faculty_list[7]: #EN
        if txt7.get() == "-" or txt8.get() == "-":
            lbl20.configure(text = "คุณมีคะแนนไม่ครบตามเกณฑ์")
        else:
            gpax = (float(txt0.get())/4)*6000
            onet = ((float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))/500)*9000
            gat = float(txt6.get())/300*3000
            pat = float(txt7.get())/300*3000 + float(txt8.get())/300*9000
            result = gpax + onet + gat + pat
            lbl20.configure(text = result)
            
            fig = Figure(figsize=(4,3), dpi=60)
            fig.add_subplot().plot(df1['fac'], df1['EN'])
            fig.add_subplot().plot(df2['fac'], df2['EN'])
            fig.add_subplot().scatter(df1['fac'], df1['EN'])
            fig.add_subplot().scatter(df2['fac'], df2['EN'])
            fig.add_subplot().plot(df2['fac'],np.array([result,result]))
            fig.add_subplot().scatter(df2['fac'],np.array([result,result]))
            
            canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().grid(column=1,row=33)
        
            
    if cbo1.get() == faculty_list[8]: #ICT
        
        if float(txt3.get())<30 and float(txt4.get())<20:
            lbl20.configure(text = "คะแนนของคุณไม่ผ่านเกณฑ์")
        elif txt7.get() == "-" or txt8.get() == "-":
            lbl20.configure(text = "คุณมีคะแนนไม่ครบตามเกณฑ์")
        else:
            gpax = (float(txt0.get())/4)*6000
            onet = ((float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))/500)*9000
            gat = float(txt6.get())/300*3000
            pat = float(txt7.get())/300*6000 + float(txt8.get())/300*6000
            result = gpax + onet + gat + pat
            lbl20.configure(text = result)
            
            fig = Figure(figsize=(4,3), dpi=60)
            fig.add_subplot().plot(df1['fac'], df1['ICT'])
            fig.add_subplot().plot(df2['fac'], df2['ICT'])
            fig.add_subplot().scatter(df1['fac'], df1['ICT'])
            fig.add_subplot().scatter(df2['fac'], df2['ICT'])
            fig.add_subplot().plot(df2['fac'],np.array([result,result]))
            fig.add_subplot().scatter(df2['fac'],np.array([result,result]))
            
            canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().grid(column=1,row=33)

    if cbo1.get() == faculty_list[9]: #EG
        
        if float(txt1.get())<30 or float(txt2.get())<30 or float(txt3.get())<30 or float(txt4.get())<30 or float(txt5.get())<30:
            lbl20.configure(text = "คะแนนของคุณไม่ผ่านเกณฑ์")
        elif txt9.get() == "-":
            lbl20.configure(text = "คุณมีคะแนนไม่ครบตามเกณฑ์")
        else:
            gpax = (float(txt0.get())/4)*6000
            onet = ((float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))/500)*9000
            gat = float(txt6.get())/300*4500
            pat = float(txt8.get())/300*4500 + float(txt9.get())/300*6000
            result = gpax + onet + gat + pat
            lbl20.configure(text = result)
            
            fig = Figure(figsize=(4,3), dpi=60)
            fig.add_subplot().plot(df1['fac'], df1['EG'])
            fig.add_subplot().plot(df2['fac'], df2['EG'])
            fig.add_subplot().scatter(df1['fac'], df1['EG'])
            fig.add_subplot().scatter(df2['fac'], df2['EG'])
            fig.add_subplot().plot(df2['fac'],np.array([result,result]))
            fig.add_subplot().scatter(df2['fac'],np.array([result,result]))
            
            canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().grid(column=1,row=33)
        
    
    if cbo1.get() == faculty_list[10]: #:LA
        
        if float(txt3.get())<40 or (float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))<150:
            lbl20.configure(text = "คะแนนของคุณไม่ผ่านเกณฑ์")
        else:
            gpax = (float(txt0.get())/4)*6000
            onet = ((float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))/500)*9000
            gat = float(txt6.get())/300*15000
            result = gpax + onet + gat
            lbl20.configure(text = result)
            
            fig = Figure(figsize=(4,3), dpi=60)
            fig.add_subplot().plot(df1['fac'], df1['LA'])
            fig.add_subplot().plot(df2['fac'], df2['LA'])
            fig.add_subplot().scatter(df1['fac'], df1['LA'])
            fig.add_subplot().scatter(df2['fac'], df2['LA'])
            fig.add_subplot().plot(df2['fac'],np.array([result,result]))
            fig.add_subplot().scatter(df2['fac'],np.array([result,result]))
            
            canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().grid(column=1,row=33)
            
        
    if cbo1.get() == faculty_list[11]: #CRS
        gpax = (float(txt0.get())/4)*6000
        onet = ((float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))/500)*9000
        gat = float(txt6.get())/300*15000
        result = gpax + onet + gat
        lbl20.configure(text = result)
        
        fig = Figure(figsize=(4,3), dpi=60)
        fig.add_subplot().plot(df1['fac'], df1['CRS'])
        fig.add_subplot().plot(df2['fac'], df2['CRS'])
        fig.add_subplot().scatter(df1['fac'], df1['CRS'])
        fig.add_subplot().scatter(df2['fac'], df2['CRS'])
        fig.add_subplot().plot(df2['fac'],np.array([result,result]))
        fig.add_subplot().scatter(df2['fac'],np.array([result,result]))
            
        canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(column=1,row=33)
        
 #2   

    if cbo2.get() == faculty_list[0]: #PY
        
        if (float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))<300:
            lbl21.configure(text = "คะแนนของคุณไม่ผ่านเกณฑ์")
        elif txt8.get() == "-":
            lbl20.configure(text = "คุณมีคะแนนไม่ครบตามเกณฑ์")
        else :
            gpax = (float(txt0.get())/4)*6000
            onet = ((float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))/500)*9000
            gat = float(txt6.get())/300*3000
            pat = float(txt8.get())/300*12000
            result = gpax + onet + gat + pat
            lbl21.configure(text = result)
            
            fig = Figure(figsize=(4,3), dpi=60)
            fig.add_subplot().plot(df1['fac'], df1['PY'])
            fig.add_subplot().plot(df2['fac'], df2['PY'])
            fig.add_subplot().scatter(df1['fac'], df1['PY'])
            fig.add_subplot().scatter(df2['fac'], df2['PY'])
            fig.add_subplot().plot(df2['fac'],np.array([result,result]))
            fig.add_subplot().scatter(df2['fac'],np.array([result,result]))
            
            canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().grid(column=2,row=33)
            
               
    if cbo2.get() == faculty_list[1]: #PH
        
        if (float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))<150:
            lbl21.configure(text = "คะแนนของคุณไม่ผ่านเกณฑ์")
        elif txt8.get() == "-":
            lbl21.configure(text = "คุณมีคะแนนไม่ครบตามเกณฑ์")
        else :
            gpax = (float(txt0.get())/4)*6000
            onet = ((float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))/500)*9000
            gat = (float(txt6.get())/300)*6000
            pat = (float(txt8.get())/300)*9000
            result = gpax + onet + gat + pat
            lbl21.configure(text = result)
            
            fig = Figure(figsize=(4,3), dpi=60)
            fig.add_subplot().plot(df1['fac'], df1['PH'])
            fig.add_subplot().plot(df2['fac'], df2['PH'])
            fig.add_subplot().scatter(df1['fac'], df1['PH'])
            fig.add_subplot().scatter(df2['fac'], df2['PH'])
            fig.add_subplot().plot(df2['fac'],np.array([result,result]))
            fig.add_subplot().scatter(df2['fac'],np.array([result,result]))
            
            canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().grid(column=2,row=33)
            
            
         
    if cbo2.get() == faculty_list[2]: #MT
        if float(txt1.get())<45 or float(txt2.get())<40 or float(txt3.get())<35 or float(txt4.get())<35 or float(txt5.get())<40 or (float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))<200:
            lbl21.configure(text = "คะแนนของคุณไม่ผ่านเกณฑ์")
        elif txt8.get() == "-":
            lbl21.configure(text = "คุณมีคะแนนไม่ครบตามเกณฑ์")
        else:
            gpax = (float(txt0.get())/4)*6000
            onet = ((float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))/500)*9000
            gat = (float(txt6.get())/300)*6000
            pat = (float(txt8.get())/300)*9000
            result = gpax + onet + gat + pat
            lbl21.configure(text = result)
            
            fig = Figure(figsize=(4,3), dpi=60)
            fig.add_subplot().plot(df1['fac'], df1['MT'])
            fig.add_subplot().plot(df2['fac'], df2['MT'])
            fig.add_subplot().scatter(df1['fac'], df1['MT'])
            fig.add_subplot().scatter(df2['fac'], df2['MT'])
            fig.add_subplot().plot(df2['fac'],np.array([result,result]))
            fig.add_subplot().scatter(df2['fac'],np.array([result,result]))
            
            canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().grid(column=2,row=33)
        
            
    if cbo2.get() == faculty_list[3]: #PT
        
        if (float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))<150:
            lbl21.configure(text = "คะแนนของคุณไม่ผ่านเกณฑ์")
        elif txt7.get() == "-" or txt8.get() == "-":
            lbl21.configure(text = "คุณมีคะแนนไม่ครบตามเกณฑ์")
        else:
            gpax = (float(txt0.get())/4)*6000
            onet = ((float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))/500)*9000
            gat = (float(txt6.get())/300)*6000
            pat = (float(txt8.get())/300)*9000
            result = gpax + onet + gat + pat
            lbl21.configure(text = result)
            
            fig = Figure(figsize=(4,3), dpi=60)
            fig.add_subplot().plot(df1['fac'], df1['PT'])
            fig.add_subplot().plot(df2['fac'], df2['PT'])
            fig.add_subplot().scatter(df1['fac'], df1['PT'])
            fig.add_subplot().scatter(df2['fac'], df2['PT'])
            fig.add_subplot().plot(df2['fac'],np.array([result,result]))
            fig.add_subplot().scatter(df2['fac'],np.array([result,result]))
            
            canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().grid(column=2,row=33)
        
    
    if cbo2.get() == faculty_list[4]: #NS
        
        if float(txt1.get())<30 or float(txt2.get())<30 or float(txt3.get())<30 or float(txt4.get())<30 or float(txt5.get())<30 or float(txt6.get())<90 or float(txt8.get())<60:
            lbl21.configure(text = "คะแนนของคุณไม่ผ่านเกณฑ์")
        elif txt8.get() == "-":
            lbl21.configure(text = "คุณมีคะแนนไม่ครบตามเกณฑ์")
        else:
            gpax = (float(txt0.get())/4)*6000
            onet = ((float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))/500)*9000
            gat = (float(txt6.get())/300)*6000
            pat = (float(txt8.get())/300)*9000
            result = gpax + onet + gat + pat
            lbl21.configure(text = result)
            
            fig = Figure(figsize=(4,3), dpi=60)
            fig.add_subplot().plot(df1['fac'], df1['NS'])
            fig.add_subplot().plot(df2['fac'], df2['NS'])
            fig.add_subplot().scatter(df1['fac'], df1['NS'])
            fig.add_subplot().scatter(df2['fac'], df2['NS'])
            fig.add_subplot().plot(df2['fac'],np.array([result,result]))
            fig.add_subplot().scatter(df2['fac'],np.array([result,result]))
            
            canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().grid(column=2,row=33)
       
    
    if cbo2.get() == faculty_list[5]: #NR
        
        if float(txt3.get())<30:
            lbl21.configure(text = "คะแนนของคุณไม่ผ่านเกณฑ์")
        elif txt8.get() == "-":
            lbl21.configure(text = "คุณมีคะแนนไม่ครบตามเกณฑ์")
        else:
            gpax = (float(txt0.get())/4)*6000
            onet = ((float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))/500)*9000
            gat = (float(txt6.get())/300)*6000
            pat = (float(txt8.get())/300)*9000
            result = gpax + onet + gat + pat
            lbl21.configure(text = result)
            
            fig = Figure(figsize=(4,3), dpi=60)
            fig.add_subplot().plot(df1['fac'], df1['NR'])
            fig.add_subplot().plot(df2['fac'], df2['NR'])
            fig.add_subplot().scatter(df1['fac'], df1['NR'])
            fig.add_subplot().scatter(df2['fac'], df2['NR'])
            fig.add_subplot().plot(df2['fac'],np.array([result,result]))
            fig.add_subplot().scatter(df2['fac'],np.array([result,result]))
            
            canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().grid(column=2,row=33)

    
           
    if cbo2.get() == faculty_list[6]: #SC
    
        if float(txt1.get())<30 or float(txt2.get())<30 or float(txt3.get())<30 or float(txt4.get())<30 or float(txt5.get())<30:
            lbl21.configure(text = "คะแนนของคุณไม่ผ่านเกณฑ์")
        elif txt7.get() == "-" or txt8.get() == "-":
            lbl21.configure(text = "คุณมีคะแนนไม่ครบตามเกณฑ์")
        else:
            gpax = (float(txt0.get())/4)*6000
            onet = ((float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))/500)*9000
            gat = float(txt6.get())/300*3000
            pat = float(txt7.get())/300*3000 + float(txt8.get())/300*9000
            result = gpax + onet + gat + pat
            lbl21.configure(text = result)
            
            fig = Figure(figsize=(4,3), dpi=60)
            fig.add_subplot().plot(df1['fac'], df1['SC'])
            fig.add_subplot().plot(df2['fac'], df2['SC'])
            fig.add_subplot().scatter(df1['fac'], df1['SC'])
            fig.add_subplot().scatter(df2['fac'], df2['SC'])
            fig.add_subplot().plot(df2['fac'],np.array([result,result]))
            fig.add_subplot().scatter(df2['fac'],np.array([result,result]))
            
            canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().grid(column=2,row=33)
            
    
    if cbo2.get() == faculty_list[7]: #EN
        if txt7.get() == "-" or txt8.get() == "-":
            lbl21.configure(text = "คุณมีคะแนนไม่ครบตามเกณฑ์")
        else:
            gpax = (float(txt0.get())/4)*6000
            onet = ((float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))/500)*9000
            gat = float(txt6.get())/300*3000
            pat = float(txt7.get())/300*3000 + float(txt8.get())/300*9000
            result = gpax + onet + gat + pat
            lbl21.configure(text = result)
        
            fig = Figure(figsize=(4,3), dpi=60)
            fig.add_subplot().plot(df1['fac'], df1['EN'])
            fig.add_subplot().plot(df2['fac'], df2['EN'])
            fig.add_subplot().scatter(df1['fac'], df1['EN'])
            fig.add_subplot().scatter(df2['fac'], df2['EN'])
            fig.add_subplot().plot(df2['fac'],np.array([result,result]))
            fig.add_subplot().scatter(df2['fac'],np.array([result,result]))
        
            canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().grid(column=2,row=33)
        
            
    if cbo2.get() == faculty_list[8]: #ICT
        
        if float(txt3.get())<30 or float(txt4.get())<20:
            lbl21.configure(text = "คะแนนของคุณไม่ผ่านเกณฑ์")
        elif txt7.get() == "-" or txt8.get() == "-":
            lbl21.configure(text = "คุณมีคะแนนไม่ครบตามเกณฑ์")
        else:
            gpax = (float(txt0.get())/4)*6000
            onet = ((float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))/500)*9000
            gat = float(txt6.get())/300*3000
            pat = float(txt7.get())/300*6000 + float(txt8.get())/300*6000
            result = gpax + onet + gat + pat
            lbl21.configure(text = result)
            
            fig = Figure(figsize=(4,3), dpi=60)
            fig.add_subplot().plot(df1['fac'], df1['ICT'])
            fig.add_subplot().plot(df2['fac'], df2['ICT'])
            fig.add_subplot().scatter(df1['fac'], df1['ICT'])
            fig.add_subplot().scatter(df2['fac'], df2['ICT'])
            fig.add_subplot().plot(df2['fac'],np.array([result,result]))
            fig.add_subplot().scatter(df2['fac'],np.array([result,result]))
            
            canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().grid(column=2,row=33)
            

    if cbo2.get() == faculty_list[9]: #EG
        
        if float(txt1.get())<30 or float(txt2.get())<30 or float(txt3.get())<30 or float(txt4.get())<30 or float(txt5.get())<30:
            lbl21.configure(text = "คะแนนของคุณไม่ผ่านเกณฑ์")
        elif txt9.get() == "-":
            lbl21.configure(text = "คุณมีคะแนนไม่ครบตามเกณฑ์")
        else:
            gpax = (float(txt0.get())/4)*6000
            onet = ((float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))/500)*9000
            gat = float(txt6.get())/300*4500
            pat = float(txt8.get())/300*4500 + float(txt9.get())/300*6000
            result = gpax + onet + gat + pat
            lbl21.configure(text = result)
            
            fig = Figure(figsize=(4,3), dpi=60)
            fig.add_subplot().plot(df1['fac'], df1['EG'])
            fig.add_subplot().plot(df2['fac'], df2['EG'])
            fig.add_subplot().scatter(df1['fac'], df1['EG'])
            fig.add_subplot().scatter(df2['fac'], df2['EG'])
            fig.add_subplot().plot(df2['fac'],np.array([result,result]))
            fig.add_subplot().scatter(df2['fac'],np.array([result,result]))
            
            canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().grid(column=2,row=33)
        
    
    if cbo2.get() == faculty_list[10]: #:LA
        
        if float(txt3.get())<40 or (float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))<150:
            lbl21.configure(text = "คะแนนของคุณไม่ผ่านเกณฑ์")
        else:
            gpax = (float(txt0.get())/4)*6000
            onet = ((float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))/500)*9000
            gat = float(txt6.get())/300*15000
            result = gpax + onet + gat
            lbl21.configure(text = result)
            
            fig = Figure(figsize=(4,3), dpi=60)
            fig.add_subplot().plot(df1['fac'], df1['LA'])
            fig.add_subplot().plot(df2['fac'], df2['LA'])
            fig.add_subplot().scatter(df1['fac'], df1['LA'])
            fig.add_subplot().scatter(df2['fac'], df2['LA'])
            fig.add_subplot().plot(df2['fac'],np.array([result,result]))
            fig.add_subplot().scatter(df2['fac'],np.array([result,result]))
            
            canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().grid(column=2,row=33)
            
        
    if cbo2.get() == faculty_list[11]: #CRS
        gpax = (float(txt0.get())/4)*6000
        onet = ((float(txt1.get())+float(txt2.get())+float(txt3.get())+float(txt4.get())+float(txt5.get()))/500)*9000
        gat = float(txt6.get())/300*15000
        result = gpax + onet + gat
        lbl21.configure(text = result)
        
        fig = Figure(figsize=(4,3), dpi=60)
        fig.add_subplot().plot(df1['fac'], df1['CRS'])
        fig.add_subplot().plot(df2['fac'], df2['CRS'])
        fig.add_subplot().scatter(df1['fac'], df1['CRS'])
        fig.add_subplot().scatter(df2['fac'], df2['CRS'])
        fig.add_subplot().plot(df2['fac'],np.array([result,result]))
        fig.add_subplot().scatter(df2['fac'],np.array([result,result]))
         
        canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(column=2,row=33)
        
    lbl22 = Label(window,text = "คณะที่ 1")
    lbl22.grid(column=1,row=32)
    lbl23 = Label(window,text = "คณะที่ 2")
    lbl23.grid(column=2,row=32)
    lbl24 = Label(window,text = "สีเขียวคือคะแนนของคุณ\nสีฟ้าคือคะแนนสูงสุด\nสีส้มคือคะแนนต่ำสุด")
    lbl24.grid(column=0,row=33)

def _quit():
    window.quit()
    window.destroy()

lbl20 = Label(window,text = " ")
lbl20.grid(column=2,row=22)

lbl21 = Label(window,text = " ")
lbl21.grid(column=2,row=23)   

lbl22 = Label(window,text = "คะแนนของคุณ")
lbl22.grid(column=2,row=21)   
       
btn1 = Button(window,text = "Calculate" ,command = calculate)
btn1.grid(column=1,row=30)

btn2 = Button(window,text = "Quit" ,command = _quit)
btn2.grid(column=1,row=31)

window.mainloop()