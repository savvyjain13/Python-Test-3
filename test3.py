Test_scores = {"Amanya":0, "Savir": 100, "Ava" : 67, "John" : 84, "Fred" : 55}
student_score = 0
max = -13
min = 101
max_student = ""
min_student = ""
for key in Test_scores:
    student_score += Test_scores.get(key)
    if max < Test_scores.get(key):
        max = Test_scores.get(key)
        max_student = key
    if min > Test_scores.get(key):
        min = Test_scores.get(key)
        min_student = key
print(min,max)
print(min_student, max_student)
average = student_score // len(Test_scores)
print(average)
student_name = input("Enter a student to get their score: ")
for key in Test_scores:
    if key == student_name:
        print(Test_scores.get(key))
        break