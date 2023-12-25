stud_scores = input("input your score range:  ").split()
for n in range(0, len(stud_scores)):
  stud_scores[n] = int(stud_scores[n])
print(stud_scores)

highest_score = 0 
for score in stud_scores :
  if score > highest_score :
    highest_score = score
print(f"The highest score in the class is: {highest_score}")

number_of_students = 0
for student in stud_scores:
  number_of_students += 1
print("The total number of students" ,number_of_students)

