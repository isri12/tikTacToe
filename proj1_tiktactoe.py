
#adding comment 
# added some
# last update 11/2/2022

row1=[' ',' ',' ']
row2=[' ',' ',' ']
row3=[' ',' ',' ']

def displayCube():
    print(row1)
    print(row2)
    print(row3)

displayCube()

def prmpt_user():
    r=int(input("for row 1: enter column b/n 0 - 2, Enter 3 for exit: "))

    return r

def prmpt_user_again():
    r=int(input("wrong input: enter column b/n 0 - 2: "))
    return r



# r=prmpt_user()
# # print(type(r))
# x=str(r)
# print(type(x))

#print(x.isdigit())

#x.isdigit() and (r>=0 and r<=2):



# if x.isdigit() and (r>=0 and r<=2):
#     print('Entered: ',r)
#     row1[r]='x'
#     displayCube()
# else:
#     prmpt_user_again()


while True:
    r=prmpt_user()
    x=str(r)
    if x.isdigit() and (r>=0 and r<=2):
        print('Entered: ',r)
        row1[r]='x'
        displayCube()
    if r==3:
        break
        
