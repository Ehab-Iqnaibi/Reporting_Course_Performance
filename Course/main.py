'''
Reporting Course Performance to Students
'''
import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt
import numpy as np

course_data = pd.read_csv("course.csv")

class students:

    def __init__(self, data):
        self.course_df = data
    def get_student_grades(self,std_grade,pdf):
        column=self.course_df.iloc[:, 3:]
        column = column.columns.tolist()
        pdf.add_page()
        pdf.set_font('Times',"B", size=14)
        pdf.cell(60)
        pdf.cell(75, 10, " Student grades of the course activities", 0, 2, 'C')
        pdf.cell(90, 10, '', 0, 2, 'C')
        # Create the header cells
        table_head=['Rubric','Grade']
        for h in table_head[:-1]:
                pdf.cell(35, 10, h, 1, 0, 'C')
        pdf.cell(35, 10, table_head[-1], 1, 1, 'C')
        pdf.set_font('Times', size=12)
        # Create the data cells
        for i in range(6):
            pdf.cell(60)
            pdf.cell(35, 10, column[i], 1, 0, 'C')
            pdf.cell(35, 10,str(std_grade[i]) , 1, 1, 'C')

        pdf.cell(90, 10, " ", 0, 2, 'C')
        pdf.cell(55, 10, " ", 0, 0, 'C')
        if index >= 1:
            # insert chart
            pdf.image('weights_of_course_activities.png', x=None, y=None, w=0, h=0, type='PNG')

            if index == 1:
                pdf.output('zzzz' + ".pdf",'F')


    #A pie chart showing the weights of course activities
    def get_pie_chart(self,w):
        column = self.course_df.iloc[:, 3:]
        labels= column.columns.tolist()
        course_weight=np.array(w)

        fig, ax = plt.subplots()
        fig.set_size_inches(3,3)

        ax.pie(course_weight[0:5], radius=1, labels= labels[0:5], autopct='%1.1f%%', wedgeprops=dict(width=1, edgecolor='white'))
        ax.set_title('weights of course activities ' )
        #plt.show()
        plt.savefig('weights_of_course_activities.png')

    def get_pdf_cover_page(self,name):
        # save FPDF() class into variable pdf
        pdf = FPDF(format='letter')
        # add a page pdf
        pdf.add_page()
        # set style and size font
        pdf.set_font("Arial", size=24)
        # add tex
        pdf.cell(60, 10, 'Palestine Polytechnic University',border =  0,ln = 1)
        pdf.set_xy(10,80)
        pdf.set_font('Times', size=20)
        pdf.cell(60, 10, 'Reporting Course Performance',border =  0,ln = 1 )
        pdf.cell(30, 10, txt="Name: "+str(name),border =  0, ln =0)
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
        if index ==1:
            std.get_pie_chart(weight_lis)
        std.get_student_grades(std_grades,std_pdf)



    index = index+1

