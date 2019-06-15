pass_grade=["A","B","C","D"]
fall_grade=["F"]

grade=input("put your grade: ")

if grade in pass_grade:
    print("your succed at the exam")
elif grade in fall_grade:
    print("your faild at the exam")
else:
        print("please put a correct grade")
        
            
          #هنا اذا تبي تحط الحرف كابيتال وسمول
          
pass_grade=["A","B","C","D"]
fall_grade=["F"]

grade=input("put your grade: ")

if grade.upper() in pass_grade or grade.lower() in pass_grade:
    print("your succed at the exam")
elif grade.lower() in fall_grade or grade.upper() in fall_grade:
    print("your faild at the exam")
else:
        print("please put a correct grade")
        
            
            