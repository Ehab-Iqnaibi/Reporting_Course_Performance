'''
Reporting Course Performance to Students
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


course_data = pd.read_csv("course.csv")
#print(course_data)
def course_activities():

class students:

    def __init__(self, data):
        self.df = data.iloc[:, 2:]
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
            course_activities(std_grades)





students(course_data)
