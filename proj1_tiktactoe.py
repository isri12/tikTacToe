
#adding comment 


row1=[' ',' ',' ']
row2=[' ',' ',' ']
row3=[' ',' ',' ']

def displayCube():
    print(row1)
    print(row2)
    print(row3)

displayCube()

def prmpt_user():
    r=int(input("for row 1: enter column b/n 0 - 2: "))
    return r

def prmpt_user_again():
    r=int(input("wrong input: enter column b/n 0 - 2: "))
    return r

r=prmpt_user()
# print(type(r))
x=str(r)
# print(type(x))

print(x.isdigit())

if x.isdigit() and (r>=0 and r<=2):
    print('Entered: ',r)
    row1[r]='x'
    displayCube()
else:
    prmpt_user_again()
