'''
Reporting Course Performance to Students
'''
import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt
import numpy as np


course_data = pd.read_csv("course.csv")
#print(course_data)

class students:

    def __init__(self, data):
        self.course_df = data.iloc[:, 3:]
    def get_student_grades(self,std_grade,pdf):
        column = str(self.course_df.columns.tolist())
        print("colums is"+column)
        pdf.add_page()
        pdf.set_font('Times', size=18)
        pdf.cell(40, 10, txt=" Student grades of the course activities", border=0,align='C')
        pdf.set_font('Times', size=14)
        pdf.set_xy(10, 10)
        # Create the header cells
        pdf.cell(40, 10, txt="Reports", border=1)
        pdf.cell(40, 10, txt="HW", border=1)
        pdf.cell(40, 10, txt= column[2], border=1)
        pdf.cell(40, 10, txt="Practical", border=1)
        pdf.cell(40, 10, txt=column[4], border=1)
        pdf.cell(40, 10, txt="Total Grade", border=1)
        # Move the cursor to the next row
        pdf.ln()
        # Create the data cells
        pdf.cell(40, 10, txt=str(std_grade[0]), border=1)
        pdf.cell(40, 10, txt=str(std_grade[1]), border=1)
        pdf.cell(40, 10, txt=str(std_grade[2]), border=1)
        pdf.cell(40, 10, txt=str(std_grade[3]), border=1)
        pdf.cell(40, 10, txt=str(std_grade[4]), border=1)
        pdf.cell(40, 10, txt=str(std_grade[5]), border=1)

    #A pie chart showing the weights of course activities
    def get_pie_chart(self,w):
        labels= self.course_df.columns.tolist()
        course_weight=np.array(w)
        print(labels)
        print(type(labels))
        print(course_weight)
        fig, ax = plt.subplots()

        ax.pie(course_weight[0:5], radius=1, labels= labels[0:5], autopct='%1.1f%%', wedgeprops=dict(width=1, edgecolor='white'))
        ax.set_title('weights of course activities ' )
        plt.show()

    def get_pdf_cover_page(self,name):
        # save FPDF() class into variable pdf
        pdf = FPDF()
        # add a page pdf
        pdf.add_page()
        # set style and size font
        pdf.set_font("Arial", size=24)
        # add text
        pdf.cell(40, 10, 'Palestine Polytechnic University',border =  0,ln = 1)
        pdf.cell(40, 10, 'Reporting Course Performance',border =  0,ln = 1)
        pdf.set_font('Times', size=18)
        pdf.cell(200, 10, txt=str(name),border =  0, ln =0, align='C')
        # save our pdf
        #pdf.output(str(name) + ".pdf")
        return(pdf)


std=students(course_data)
# Iterate through each row in the DataFrame
df = course_data.set_index('Name')
df = df.iloc[:, 2:]
#print(df)
index=0
for i, row in df.iterrows():
    # Get the name and marks for the student
    student_name = i
    student_marks = row
    reports = row["Reports"]
    hw = row["HW"]
    #print(type(hw))
    midterm = row["Midterm"]
    practical = row["Practical"]
    final = row["Final"]
    total_grade = row["Total Grade"]
    std_grades = [reports, hw, midterm, practical, final, total_grade]
    if index == 0:
        weight_lis =std_grades
        #print(weight_lis)
    else:
        std_pdf = std.get_pdf_cover_page(student_name)
        std.get_student_grades(std_grades,std_pdf)
        std.get_pie_chart(weight_lis)


    index = index+1

