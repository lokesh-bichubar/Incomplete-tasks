X = str(input("Name: "))
Y = int(input("Roll no.: "))

# Marks in subjects
English = int(input("English: "))
Chemistry = int(input("Chemistry: "))
Painting = int(input("Painting: "))
Mathematics = int(input("Mathematics: "))
Physics = int(input("Physics: "))

total = (English + Chemistry + Painting + Mathematics + Physics)


print("Total Marks:", total, "out of 500" " " "and the percentage is", (total/5))
