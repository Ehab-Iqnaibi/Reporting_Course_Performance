
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
'''
# for Excel file
#course_data2 = pd.read_excel('course1.xlsx', sheet_name='course1')
#print(course_data2)

course_data = pd.read_csv("course.csv")
print(course_data)
class student:

    def __init__(self, df):
        self.name = data["Name"]
        self.reports = data["Reports"]
        self.hw = data["HW"]
        self.midterm = data["Midterm"]
        self.practical = data["Practical"]
        self.practical = data["Practical"]

#pdf
from fpdf import FPDF
# save FPDF() class into variable pdf
pdf = FPDF()
#add a page pdf
pdf.add_page()
#set style and size font
pdf.set_font("Arial",size=16)
# creat text
pdf.cell(40 ,10,txt="Ehab Iqnaibi",align="C")
#save our pdf
pdf.output("ehab.pdf")

#3 
std_names = df['Name']
#df = df.set_index('Name')
print(df)
print(df.iloc[7].isnull()['HW'] )
print(std_names)
'''

#marks_df = pd.read_excel("Marks\Class1_Marks.xlsx")
df = pd.read_csv("course.csv")
df = df.set_index('Name')

df = df.iloc[:, 2:]

for i, row in df.iterrows():
    student_name = i
    student_marks = row

    # Print the student name and marks
    print(student_name)
    print(student_marks)



