
score = input("Enter Score: ")

try:
    testscore = float(score)
except:
    Print("Invalid score.  Must be between 0 and 1")
    quit()

if testscore > 1:
    Print("Invalid score.  Must be between 0 and 1")
    quit()
elif testscore < 0:
    Print("Invalid score.  Must be between 0 and 1")
    quit()

if testscore >= 0.9 :
    grade = "A"
elif testscore >= 0.8 :
    grade = "B"
elif testscore >= 0.7 :
    grade = "C"
elif testscore >= 0.6 :
    grade = "D"
else:
    grade = "F"

print(grade)

