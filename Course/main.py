'''
Reporting Course Performance to Students
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


course_data = pd.read_csv("course.csv")
#print(course_data)

class students:

    def __init__(self, data):
        self.df = data
    def get_student_grades(self,std_name,std_grade):
        print(std_name)
        print(std_grade)

   # def course_activities(self):


std=students(course_data)
# Iterate through each row in the DataFrame
df = course_data.set_index('Name')
df = df.iloc[:, 2:]
index=0
for i, row in df.iterrows():
    student_name = i
    student_marks = row
    # Get the name and marks for the student
    #name = row["Name"]
    reports = row["Reports"]
    hw = row["HW"]
    midterm = row["Midterm"]
    practical = row["Practical"]
    final = row["Final"]
    total_grade = row["Total Grade"]
    std_grades = [ reports, hw, midterm, practical, final, total_grade]
    if index == 0:
        weight_lis = std_grades
        #print(weight_lis)
    else:
        std.get_student_grades(student_name,std_grades)
    index = index+1

