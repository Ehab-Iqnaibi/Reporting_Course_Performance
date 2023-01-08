'''
Reporting Course Performance to Students
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# for Excel file
course_data2 = pd.read_excel('course1.xlsx', sheet_name='course1')
#print(course_data2)
course_data = pd.read_csv("course.csv")
print(course_data)
class student:

    def __init__(self, data):
        self.name = data["Name"]
        self.status = data["Name"]
        self.speed = data["Name"]
        self.fuel = data["Name"]
        self.direction = data["Name"]


student(course_data)