grade_sum=0.0
grade_count=0
while True:
    grade=input("Letter grade:")
    if grade=="":
        break
    elif grade=="A":
        point=4.0
    elif grade=="A-":
        point=3.7
    elif grade=="B+":
        point=3.3
    elif grade=="B":
        point=3.0
    elif grade=="B-":
        point=2.7
    elif grade=="C+":
        point=2.3
    elif grade=="C":
        point=2.0
    elif grade=="C-":
        point=1.7
    elif grade=="D+":
        point=1.3
    elif grade=="D":
        point=1.0
    elif grade=="D-":
        point=0.7
    elif grade=="F":
        point=0.0
    else:
        print("Error")
    grade_sum+=point
    grade_count+=1
gpa=round(grade_sum/grade_count,2)
print("Average:",gpa)
