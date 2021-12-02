class person:
    name = viral
    age = 20.0
    gender = male
    city = surat



class student(person):
    id = 1
    semester = 6
    division = a
    sub1marks = 99
    sub2marks = 100
    sub3marks = 97
    def result():
        per = (sub1marks+sub2marks+sub3marks)/4



class employee(person):
    id = 1
    designation = manager
    salery = 10000
   def  gross_salery():
       if salery == 10000:
           hra = (salery*10)/100
           da = (salery*5)/100
           pf = 200
           total = salery+hra+da+pf
           print("employee inforamtion is:)
           print()
           print()
           print()
           print()
           
       else:
           hra = (salery*15)/100
           da = (salery*7)/100
           pf = (salery*10)/100 
           total = salery+hra+da+pf

    


