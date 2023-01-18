'''
Reporting Course Performance to Students
'''
import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt
import numpy as np
import math

#course_data = pd.read_csv("course.csv")
course_data = pd.read_excel('course1.xlsx')
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
    def student_grades(self, pdf):
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
        # insert chart
        pdf.image('weights_of_course_activities.png', x=20, y=120, w=160, h=120, type='PNG')
        return (pdf)
    def std_pdf(self,pdf):
        pdf.add_page()
        pdf.cell(60)
        pdf.set_font('Times', "B", size=16)
        # Course activities that the student miss or did not submit
        pdf.cell(75, 10, "Course activities missed or not submitted ", 0, 2, 'C')
        pdf.cell(90, 10, '', 0, 2, 'C')
        table_head = ['Rubric', 'Grade']
        for h in table_head[:-1]:
            pdf.cell(35, 10, h, 1, 0, 'C')
        pdf.cell(35, 10, table_head[-1], 1, 1, 'C')
        pdf.set_font('Times', size=12)
        if any(math.isnan(grade) for grade in self.std_grade):
             for i in range(6):
                # Check if any of the marks is null
                if math.isnan(self.std_grade[i]):
                    pdf.cell(60)
                    pdf.cell(35, 10, self.rubric[i], 1, 0, 'C')
                    pdf.cell(35, 10, 'miss', 1, 1, 'C')
        else:
             pdf.cell(60)
             pdf.cell(70, 10, 'You delivered all Course activities', 1, 1, 'C')

        # insert Bar chart of student grades in the course activates
        pdf.image('bar_chart_of_' + self.std_name + '_grades.png', x=20, y=100, w=170, h=120, type='PNG')
        # insert Bar chart of student his/her rank within the whole class
        pdf.add_page()
        pdf.cell(60)
        pdf.set_font('Times', "B", size=16)
        pdf.cell(75, 10, "A chart showing the student his/her rank within the whole class ", 0, 1, 'C')
        pdf.image('bar_chart_of_' + self.std_name + '_rank.png', x=20, y=30, w=170, h=120, type='PNG')
        pdf.set_font('Times', "", size=28)
        pdf.set_xy(40, 200)
        pdf.cell(40, 20, 'Good Luck '+self.std_name, 0, 1, 'C')
        if user0 == 1:
            pdf.output('Reporting_Course_Performance_' + self.std_name + ".pdf", 'F')
        elif user0 == 2:
            if index == user:
                pdf.output('Reporting_Course_Performance_' + self.std_name + ".pdf", 'F')

    #A pie chart showing the weights of course activities
    def pie_chart(self):
        fig1, ax1 = plt.subplots()
        l=len(self.rubric_weight)-1
        ax1.pie(self.rubric_weight[0:l], radius=1, labels= self.rubric[0:l], autopct='%1.1f%%', wedgeprops=dict(width=1, edgecolor='white'))
        ax1.set_title('weights of course activities ' )
        plt.savefig('weights_of_course_activities.png')

    # bar chart of the student grades in the course activates
    # as a fraction of the total grade for each activity
    def bar_chart(self):
        x = np.arange(len(self.rubric))
        width1 = 0.3
        width2 = 0.2
        fig2, ax = plt.subplots()
        ax.bar(x , self.rubric_weight, width1, label='Full Grade', color="red")
        ax.bar(x , self.std_grade, width2, label='Your Grade', color="blue")
        ax.set_ylabel('Grades')
        ax.set_title(self.std_name+' Activities')
        ax.set_xticks(x)
        ax.set_xticklabels(self.rubric, rotation='vertical')
        ax.legend()
        fig2.tight_layout()
        plt.savefig('bar_chart_of_'+self.std_name+'_grades.png')
        plt.close()
    def rank_chart(self):
        # Sort the dataframe by Total Grade in descending order
        std_df = course_data.sort_values(by='Total Grade', ascending=False)
        r = np.arange(len(std_df['Name'].iloc[1:]))
        fig3, ax3 = plt.subplots()
        # Create the bar chart
        ax3.bar( std_df['Name'].iloc[1:],std_df['Total Grade'].iloc[1:], color='blue')
        # Get the index of the specified student
        specified_student_name = self.std_name
        student_index = std_df.index[std_df['Name'] == specified_student_name].tolist()[0]
        # Plot the red bar for the specified student
        ax3.bar(std_df.loc[student_index, 'Name'], std_df.loc[student_index, 'Total Grade'], color='red')
        # Add title and labels to the axes
        ax3.set_title('You ranking on the whole class')
        ax3.set_xticks(r)
        ax3.set_xticklabels(std_df['Name'].iloc[1:], rotation='vertical')
        ax3.set_ylabel("Total Grade")
        specified_student_x = list(std_df['Name'].iloc[1:]).index(self.std_name)
        # Add 'You' above the red bar
        ax3.text(specified_student_x, std_df.loc[student_index, 'Total Grade'] + 5, 'You', ha='center')
        #save ranking on the whole class
        plt.savefig('bar_chart_of_' + self.std_name + '_rank.png')
        plt.close()
        # Show the chart
        #plt.show()

    def pdf_cover_page(self):
        # save FPDF() class into variable pdf
        pdf = FPDF(format='letter')
        # add a page pdf
        pdf.add_page()
        pdf.image('logo.png', x=80, y=10, w=65, h=55, type='PNG')
        # set style and size font
        pdf.set_font("Arial", size=24)
        # add tex
        pdf.set_xy(10, 80)
        pdf.cell(60, 10, 'Palestine Polytechnic University',border =  0,ln = 1)
        pdf.set_xy(10,120)
        pdf.set_font('Times', size=20)
        pdf.cell(60, 10, 'Reporting Course Performance',border =  0,ln = 1 )
        pdf.cell(30, 10, txt="Name: "+str(self.std_name),border =  0, ln =0)
        return(pdf)


# Iterate through each row in the DataFrame
df = course_data.set_index('Name')
df = df.iloc[:, 2:]
column = course_data.iloc[:, 3:].columns.tolist()
std = students(column)
index=0
user0=int(input('Do you want to create a pdf file for 1.All student OR 2. A specific student: '))
if user0 == 1:
    pass
elif user0 == 2:
    print(course_data['Name'].iloc[1:])
    user = int(input('Enter the student number for which you want to create a pdf file: '))

for i, row in df.iterrows():
    # Get the name and marks for the student
    student_name = i
    std_grades = row
    if index == 0:
        std.set_weights(std_grades)
    else:
        std.set_name(student_name)
        std.set_grade(std_grades)
        std_pdf = std.pdf_cover_page()
        if index ==1:
            std.pie_chart( )
        std.rank_chart()
        std.bar_chart( )
        std_pdf = std.student_grades(std_pdf)
        std.std_pdf(std_pdf)

    index = index+1

