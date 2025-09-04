#numList = [5, 40, 2938, 10, 66, 7, 38, 9999999, 3]
#for i in numList:
    #if i > 50:
        #print(i)
username = "endlessconundrums"
password = "drowssap"
userCorrect = False
passCorrect = False
#while not (userCorrect or passCorrect):
    #print("Username or password incorrect. Please reenter username and password.")
    #userCheck = input("Input username: ")
    #if userCheck == username:
        #userCorrect = True
    #else:
        #userCorrect = False
    #passCheck = input("Input password: ")
    #if passCheck == password:
        #passCorrect = True
    #else:
        #passCorrect = False
numListTwo = [4, 9, 2, 0, 5, 8, 6, 11, 7, 1, 3]
for i in numListTwo:
    if (i % 2 == 1):
        continue
    if i > 10:
        break
    print (i)