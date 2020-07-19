print("Use the following as a guide A=4, B=3, C=2, D=1, F=0")
math=input("Enter the corresponding number with the letter grade for math: ")
sci=input("Enter the corresponding number with the letter grade for science: ")
ss=input("Enter the corresponding number with the letter grade for history: ")
eng=input("Enter the corresponding number with the letter grade for english: ")
gpa=((float(math) + float(sci) + float(ss) + float(eng)) / 4)
print("Your GPA is " + str(gpa))  






