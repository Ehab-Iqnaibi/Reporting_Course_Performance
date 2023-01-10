'''
Reporting Course Performance to Students
'''
import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt
import numpy as np
import math

course_data = pd.read_csv("course.csv")

class students:

    def __init__(self, Rubric):
        self.rubric = Rubric
        self.rubric_weight=[]
        self.std_name=''
        self.std_grade=[]
    def set_name(self, name):
        self.std_name = name
    def set_grade(self, grades):
        self.std_grade = grades
    def set_weights(self, weights):
        self.rubric_weight = weights
    #def student_grades(self,std_grade,pdf):
    def student_grades(self, pdf):
        #column=self.course_df.iloc[:, 3:]
        #column = column.columns.tolist()
        #print(self.rubric)
        #print(self.std_grade)
        pdf.add_page()
        pdf.set_font('Times',"B", size=16)
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
            pdf.cell(35, 10, self.rubric[i], 1, 0, 'C')
            pdf.cell(35, 10,str(self.std_grade[i]) , 1, 1, 'C')

        pdf.cell(90, 10, " ", 0, 2, 'C')
        pdf.cell(55, 10, " ", 0, 0, 'C')

        # insert chart
        pdf.image('weights_of_course_activities.png', x=None, y=None, w=0, h=0, type='PNG')

        #if index == 1:
             #pdf.output('zzzz' + ".pdf",'F')
        #return (column,std_grade)
        return (pdf)
    def null_rubric(self,pdf):
        pdf.add_page()
        pdf.cell(60)
        pdf.set_font('Times', "B", size=16)
        pdf.cell(75, 10, "Course activities missed or not submitted ", 0, 2, 'C')
        pdf.cell(90, 10, '', 0, 2, 'C')
        table_head = ['Rubric', 'Grade']
        for h in table_head[:-1]:
            pdf.cell(35, 10, h, 1, 0, 'C')
        pdf.cell(35, 10, table_head[-1], 1, 1, 'C')
        pdf.set_font('Times', size=12)
        #pdf.cell(90, 10, "Course activities missed or not submitted ", 0, 2, 'C')
        for i in range(6):
            # Check if any of the marks is null
            if math.isnan(self.std_grade[i]):
                pdf.cell(60)
                pdf.cell(35, 10, self.rubric[i], 1, 0, 'C')
                pdf.cell(35, 10, 'miss', 1, 1, 'C')

        #pdf.cell(90, 10, " ", 0, 2, 'C')
        #pdf.cell(90, 10, " ", 0, 0, 'C')
        pdf.set_xy(10, 120)

        # insert Bar chart
        #pdf.image('bar_chart_of_' + self.std_name + '_grades.png', x=None, y=None, w=0, h=0, type='PNG')
        pdf.image('bar_chart_of_' + self.std_name + '_grades.png', x=20, y=80, w=160, h=90, type='PNG')
        if index == 7:
           pdf.output('zzzzz7' + ".pdf",'F')



    #A pie chart showing the weights of course activities
    def pie_chart(self):
        #column = self.course_df.iloc[:, 3:]
        labels= self.rubric
        #course_weight=np.array(w)

        fig, ax = plt.subplots()
        fig.set_size_inches(3,3)

        ax.pie(self.rubric_weight[0:5], radius=1, labels= labels[0:5], autopct='%1.1f%%', wedgeprops=dict(width=1, edgecolor='white'))
        ax.set_title('weights of course activities ' )
        #plt.show()
        plt.savefig('weights_of_course_activities.png')

    # bar chart of the student grades in the course activates
    # as a fraction of the total grade for each activity
    def bar_chart(self):
        labels = self.rubric
        x = np.arange(len(labels))
        width1 = 0.3
        width2 = 0.2
        fig, ax = plt.subplots()
        #fig.set_size_inches(6,4)

        ax.bar(x , self.rubric_weight, width1, label='Full Grade', color="red")
        ax.bar(x , self.std_grade, width2, label='Your Grade', color="blue")
        ax.set_ylabel('Grades')
        ax.set_title(self.std_name+' Activities')
        ax.set_xticks(x)
        ax.set_xticklabels(labels, rotation='vertical')
        ax.legend()
        fig.tight_layout()
        plt.savefig('bar_chart_of_' + self.std_name + '_grades.png')
        #plt.show()

    def pdf_cover_page(self):
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
        pdf.cell(30, 10, txt="Name: "+str(self.std_name),border =  0, ln =0)
        # save our pdf
        #pdf.output(str(self.std_name) + ".pdf")
        return(pdf)


#std=students(course_data)
# Iterate through each row in the DataFrame
df = course_data.set_index('Name')
df = df.iloc[:, 2:]
#column=course_data.iloc[:, 3:]
column = course_data.iloc[:, 3:].columns.tolist()
std = students(column)
index=0
for i, row in df.iterrows():
    # Get the name and marks for the student
    student_name = i
    student_marks = row
    '''
    reports = row["Reports"]
    hw = row["HW"]
    #print(type(hw))
    midterm = row["Midterm"]
    practical = row["Practical"]
    final = row["Final"]
    total_grade = row["Total Grade"]
    std_grades = [reports, hw, midterm, practical, final, total_grade]
    '''
    std_grades = student_marks

    if index == 0:
        #weight_lis =std_grades
        print(std_grades)
        std.set_weights(std_grades)
    else:
        #print(student_name)
        std.set_name(student_name)
        #print(std_grades)
        std.set_grade(std_grades)
        std_pdf = std.pdf_cover_page()
        if index ==1:
            std.pie_chart( )
        std.bar_chart( )
        std_pdf = std.student_grades(std_pdf)
        std.null_rubric(std_pdf)



    index = index+1

