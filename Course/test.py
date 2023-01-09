
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


#marks_df = pd.read_excel("Marks\Class1_Marks.xlsx")
df = pd.read_csv("course.csv")
df = df.set_index('Name')

df = df.iloc[:, 2:]

for i, row in df.iterrows():
    student_name = i
    student_marks = row

    # Check if any of the marks is null
  #  if student_marks.isnull().any():
        # Print the name of the student and the name of the column that is null
       # print(f"{student_name}: {student_marks.name[student_marks.isnull()]} is null")

    # Print the student name and marks
    print(student_name)
    print(student_marks)
    print(student_marks.loc["Total Grade"])
    print(student_marks.iloc[2])

    print(df.columns)
    column=df.columns.tolist()
    print(column[2])

# A pie chart
import matplotlib.pyplot as plt
import numpy as np
labels = ['Eng', 'IT', 'CAS', 'Sci', 'Med', 'CAP']
student_count = np.array( [[280, 170], [250, 270],
[210, 290], [130, 150], [145, 165], [500, 350]] )
aggregated_student_count = student_count.sum(axis=1)
print(aggregated_student_count)
flattened_student_count = student_count.flatten()
fig, ax = plt.subplots()
ax.pie(aggregated_student_count, radius=1, labels= labels)
ax.set_title('University Student Distribution per College')
plt.show()

# Open the image and get its width and height
img = Image.open('logo.png')
img_width, img_height = img.size

# Get the width and height of the page
page_width, page_height = pdf.w, pdf.h

# Calculate the x and y coordinates needed to center the image
x = (page_width - img_width) / 2
y = (page_height - img_height) / 2

# Add the image to the PDF document
pdf.image('logo.png', x=x, y=y, w=10, h=0.5, type='PNG')
 '''
#pdf
#from PIL import Image
from fpdf import FPDF
ll=['a','b']
gg=list(range(4))
# save FPDF() class into variable pdf
pdf = FPDF(format='letter')
#add a page pdf
pdf.add_page()

#set style and size font
pdf.set_font("Arial",size=24)


pdf.cell(60)
pdf.cell(75 ,10," ",0,2,'C')
pdf.cell(75, 10, 'Palestine Polytechnic University',  0, 6,'C')
pdf.cell(75, 10, 'Reporting Course Performance',border =  0,ln = 1)
#pdf.cell(90,10,'',0,4,'C')
pdf.set_font('Times', size=16)
pdf.cell(70, 10, txt='Name: Ehab Iqnaibi',border =  0, ln =1, align='C')
#pdf.cell(20 ,0,txt="Ehab Iqnaibi",border=0,ln=2,align="C")


pdf.add_page()
pdf.cell(60)
pdf.cell(75,10,'Ehab Iqnaibi',0,2,'C')
pdf.cell(90,10,'',0,2,'C')
for l in ll:
    pdf.cell(35, 10, l, 1, 0, 'C')
#pdf.cell(35, 10, "llllll", 1, 1, 'C')
pdf.set_font("Arial",'B',size=11)
for g in gg:
    pdf.cell(60)
    pdf.cell(35, 10, str(g), 1, 0, 'C')
    pdf.cell(35, 10, str(g**2), 1, 1, 'C')
pdf.cell(90, 10, "gggggggggg", 0, 2, 'C')
pdf.cell(55, 10, "image", 0, 0, 'C')
#save our pdf
pdf.output("test4.pdf")


'''
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
        
        pdf.cell(35,10,'')
        pdf.cell(75, 10, " Student grades of the course activities", 0, 2, 'C')
        pdf.set_font('Times', size=12)
        pdf.cell(20, 10, '', 0, 0, 'C')
        # Create the header cells
        table_head=['Rubric','Grade']
        for h in table_head:
            if h=='Rubric':
                pdf.cell(35, 10, h, 1, 0, 'C')
            else:
                pdf.cell(35, 10, h, 1, 1, 'C')

        # Create the data cells
        for i in range(6):
            #pdf.cell(60)
            pdf.cell(55, 10, '', 0, 0, 'C')
            pdf.cell(35, 10, column[i], 1, 0, 'C')
            pdf.cell(35, 10,str(std_grade[i]) , 1, 1, 'C')
        '''