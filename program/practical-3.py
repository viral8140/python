while True:
  try:
    maths = float(input("Enter maths Marks: ")) 
    if maths<101 and maths>0:
      print("Marks entered successfully ")
      break;
    else:
      print("Marks should be >100 and <0 ")      
  except ValueError:
    print("Provide an integer value ")
    continue
while True:
  try:
    java = float(input("Enter java Marks: ")) 
    if java<101 and java>0:
      print("Marks entered successfully ")
      break;
    else:
      print("Marks should be >100 and <0 ")      
  except ValueError:
    print("Provide an integer value ")
    continue
while True:
  try:
    c = float(input("Enter c Marks: ")) 
    if c<101 and c>0:
      print("Marks entered successfully ")
      break;
    else:
      print("Marks should be >100 and <0 ")      
  except ValueError:
    print("Provide an integer value ")
    continue
while True:
  try:
    python = float(input("Enter python Marks: ")) 
    if python<101 and python>0:
      print("Marks entered successfully")
      break;
    else:
      print("Marks should be >100 and <0")      
  except ValueError:
    print("Provide an integer value")
    continue
percentage=(maths+c+java+python)/4
print("your percentage is:", percentage)
if percentage>90:
    print("your grade is A")
elif percentage>=80:
    print("your grade is B")
elif percentage<=70:
    print("your grade is C")
elif percentage<=50:
    print("your grade is D")
else:
    print("your grade is F")
