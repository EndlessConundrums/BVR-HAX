import math

def areaFunction(shape, width, height):
    if shape == "rectangle":
        return width * height
    elif shape == "square":
        height = width
        return width * height
    elif shape == "triangle":
        return (width * height) / 2
    elif shape == "circle":
        return (width ** 2) * math.pi

#shapeInput = input("Enter shape: ")
#widthInput = int(input("Enter width: "))
#heightInput = int(input("Enter height: "))
#area = areaFunction(shapeInput, widthInput, heightInput)
#print(area)