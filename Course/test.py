
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
# *******************************
    def course_activities(self,std_grade):
        print(std_grade)

    def student_grades(self):
        # Iterate through each row in the DataFrame
        for index, row in self.df.iterrows():
            print(index)
            print(row)

            # Get the name and marks for the student
            name = row["Name"]
            reports = row["Reports"]
            hw = row["HW"]
            midterm = row["Midterm"]
            practical = row["Practical"]
            final = row["Final"]
            total_grade = row["Total Grade"]
            std_grades=[name,reports,hw,midterm,practical,final,total_grade]
            if index==0:
                weight_lis=std_grades
            else:
            self.course_activities(std_grades)
'''

#marks_df = pd.read_excel("Marks\Class1_Marks.xlsx")
df = pd.read_csv("course.csv")
df = df.set_index('Name')

df = df.iloc[:, 2:]

for i, row in df.iterrows():
    student_name = i
    student_marks = row

    # Check if any of the marks is null
    if student_marks.isnull().any():
        # Print the name of the student and the name of the column that is null
        print(f"{student_name}: {student_marks.name[student_marks.isnull()]} is null")

    # Print the student name and marks
    print(student_name)
    print(student_marks)
    print(student_marks.loc["Total Grade"])
    print(student_marks.iloc[2])






