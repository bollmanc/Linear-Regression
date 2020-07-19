import pandas as pd
import numpy as np 
from sklearn import linear_model
import matplotlib.pyplot as plt 
import tkinter as tk
import sys
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


forecast_data = pd.read_excel(r'/Users/cale/Desktop/Forecasting Project/Book1.xlsx')
df = pd.DataFrame(forecast_data, columns = ['Year', 'Month', 'Surgeries', 'Sales'])


X = df[['Month']].astype(float)
Y = df[['Surgeries']].astype(float)
Y1 = df[['Sales']].astype(float)

regr = linear_model.LinearRegression()
regr.fit(X,Y) 

root = tk.Tk()
canvas1 = tk.Canvas(root, width = 500, height = 300)
canvas1.pack()

Intercept_result = ('Intercept: ', regr.intercept_)
label_Intercept = tk.Label(root, text=Intercept_result, justify = 'center')
canvas1.create_window(260, 220, window=label_Intercept)

Coefficients_result  = ('Coefficients: ', regr.coef_)
label_Coefficients = tk.Label(root, text=Coefficients_result, justify = 'center')
canvas1.create_window(260, 240, window=label_Coefficients)


label1 = tk.Label(root, text='Type Month: ')
canvas1.create_window(100, 100, window=label1)

entry1 = tk.Entry(root) 
canvas1.create_window(270, 100, window=entry1)


def values(): 
    global new_month 
    new_month = float(entry1.get()) 
    
    Prediction_result  = ('Predicted # of Cases: ', regr.predict([[new_month]]))
    label_Prediction = tk.Label(root, text= Prediction_result, bg='orange')
    canvas1.create_window(260, 280, window=label_Prediction)

    
button1 = tk.Button (root, text='Predict # of Cases',command=values, bg='orange') 
canvas1.create_window(270, 150, window=button1)
 
#plot # of Cases 
figure3 = plt.Figure(figsize=(5,4), dpi=100)
ax3 = figure3.add_subplot(111)
ax3.scatter(df['Month'],df['Surgeries'], color = 'r')
scatter3 = FigureCanvasTkAgg(figure3, root) 
scatter3.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
ax3.legend(['# of Cases']) 
ax3.set_xlabel('Month')
ax3.set_title('# of Cases per Month')

#plot Revenue
figure4 = plt.Figure(figsize=(5,4), dpi=100)
ax4 = figure4.add_subplot(111)
ax4.scatter(df['Month'].astype(float),df['Sales'].astype(float), color = 'g')
scatter4 = FigureCanvasTkAgg(figure4, root) 
scatter4.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
ax4.legend(['Sales']) 
ax4.set_xlabel('Month')
ax4.set_title('Sales per Month')

root.mainloop()









