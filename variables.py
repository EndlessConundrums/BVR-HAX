#rectWidth = int(input())
#rectHeight = int(input())
#rectPerimeter = (rectHeight * 2) + (rectWidth * 2)
#rectArea = rectWidth * rectHeight
#print(rectPerimeter)
#print(rectArea)
# If I were to write
#someString = "blah"
#print(someString * 3)
# It prints "blahblahblah"
score = 95
if (score < 0) or (score > 100):
    print("I think you cheated...")
elif score < 60:
    print("You failed the test.")
elif score < 70:
    print("Your grade is a D.")
elif score < 80:
    print("Your grade is a C.")
elif score < 90:
    print("Your grade is a B.")
else:
    print("Your grade is an A.")
grades = {"Eaton":90, "Morillo":85, "Borkowski":100, "Robinson":95}
#select = input("Class to access: ")
#ction = input("Read or write? ")
#if action == "read":
    #print(grades[select])
#elif action == "write":
    #newGrade = int(input("New grade: "))
    #grades[select] = newGrade
    #print(grades[select])
someList = [1, 2, 3]
listOne = someList
listTwo = someList
listThree = someList
listOne.append([4, 5, 6])
listTwo.append(["A", "B", "C"])
listThree.append([3.1, 3.2, 4.5])
print(someList) # a visual representation of no communication