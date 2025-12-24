name = input("Enter Student name: ")

english = int(input("Enter English Marks: "))
maths = int(input("Enter Maths Marks: "))
science = int(input("Enter Science Marks: "))

total_marks = english + maths + science
percentage = (total_marks / 300) * 100
 
if percentage >=90:
    grade = "A+"
elif percentage >=80:
   grade = "A"
elif percentage >=70:
    grade = "B+"
elif percentage >=60:
    grade = "B"
elif percentage >=50:
    grade = "C+"
elif percentage >=40:
    grade = "D"
elif percentage < 40:
 grade = "Fail"

 print("\n---result---")
 print(f"Student Name {name}")
 print(f"Total Marks {total_marks} /300")
 print(f"percentage{percentage:.2f} %")
 print(f"{grade}")
    