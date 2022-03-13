# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("hello world")
mystring = 'hello'
myintger = 16
mystring
print(mystring)
print(myintger)

numberofapples = 5

if numberofapples<1:
 print('You have no apples')
elif numberofapples == 1:
 print('You have one apple')
elif numberofapples < 4:
 print('You have a few apples')
else:
 print('You have many apples!')
 
student_names = ['Doaa', 'Ibrahim', 'Mohamed', 'Ahmed']
print(student_names[1])
print(student_names[-1])
print(student_names[0:2])
print(student_names[1:3])
print(student_names[:2])
student_names.append('Fatma')
print(student_names)
student_names.insert(2, 'Zeinab')
print(student_names)
del student_names[4]
print(student_names)
student_names.append('Esraa')
student_names.append('Esraa')
print(student_names)
#loops
for student_name in student_names:
    print('Hello ' + student_name + '!')
    
# Nested loops 
studentpairs = []
for student_name0 in student_names:
    for student_name1 in student_names:
        studentpairs.append(
            (student_name0, student_name1)
        )

print(studentpairs)    
    
 #Dictionaries
foreignlanguages = {
    'Alice': 'Spanish',
    'Bob': 'French',
    'Carol': 'Italian',
    'Dave': 'Italian',
}
foreignlanguages['Carol']
#foreignlanguages['Zeke']
'Zeke' in foreignlanguages
for key in foreignlanguages:
    value = foreignlanguages[key]
    print(key, 'is taking', value)
    
#Mutable   
foreignlanguages['Esther'] = 'French'
print(foreignlanguages)
del foreignlanguages['Bob']
print(foreignlanguages)
foreignlanguages['Esther'] = 'Italian'
print(foreignlanguages)

#Looping over dictionaries
for key in foreignlanguages:
    value = foreignlanguages[key]
    print(key, 'is taking', value)

for key, value in foreignlanguages.items():
    print(key, 'is taking', value)
    
#Dictionaries as records
studentgrade = ('Doaa', 'Arabic', 'A')
studentname, subject, grade = studentgrade
print(studentname, 'got a grade of', grade, 'in', subject)  

record = {
    'name': 'Doaa',
    'subject': 'Arabic',
    'grade': 'A',
}
print(record['name'],'got a grade of', record['grade'],'in', record['subject'])  

#List of tuples
studentgrades = [
    ('Doaa', 'Arabic', 'A'),
    ('Doaa', 'French', 'C'),
    ('Ali', 'Arabic', 'B+'),
    ('Ali', 'French', 'A-'),
]
print(studentgrades[1])  

studentgraderecords = []
for studentname, subject, grade in studentgrades:
    record = {
        'name': student_name,
        'subject': subject,
        'grade': grade,
    }
    studentgraderecords.append(record)
print(studentgraderecords)

studentcoursegrades = {}
for studentname, subject, grade in studentgrades:
    studentcoursegrades[studentname, subject] = grade
    
print(studentcoursegrades)

x=int(input("enter number :"))
def num (y):
    return y*y

print(num(x))

#max number
def myMax(list1):
    max1 = list1[0]
    for x in list1:
        if x > max1 :
             max1 = x
    return max1
  
list1 = []
num = int(input("Enter number of elements in list: "))
for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    list1.append(ele)

print("max number is:", myMax(list1))
          
list3=[item ** 3 for item in range(1,6)]
print(list3)

          
          



  
    
    
    