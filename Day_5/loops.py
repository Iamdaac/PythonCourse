# fruits = ["Apple", "Peaches", "Pear"]

# for fruit in fruits: 
#     print(fruit)
#     print(fruit + " pie")

# .sum(a) helps us to add every item on a list

student_score = [180, 124, 165, 173, 189, 169, 146]

# total_exam_score = sum(student_score)

# suma = 0
# for score in student_score: 
#     suma += score
# print(suma)

maxima_exam_score = max(student_score)
print(maxima_exam_score)

max_score = 0
for score in student_score: 
    if score > max_score:
        max_score = score

print(max_score)
    
