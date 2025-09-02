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