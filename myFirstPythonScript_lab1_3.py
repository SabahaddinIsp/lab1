name=input("Enter your name\n")
labScore= int(input("Enter your lab score\n"))
midScore= int(input("Enter your midterm score\n"))
finalScore= int(input("Enter your final score\n"))

totalGrade= labScore*0.25 + midScore*0.35 + finalScore*0.40

print("Name: " + name)
print("Lab: " + str(labScore))
print("Midterm: " + str(midScore))
print("Final: " + str(finalScore))
print("Last score: " + str(totalGrade))