
#Israel Kinfu
# last update 11/08/2022

def game_rules():
    print('=====================================================\n'
          'Game rules:\n'
          '1 means that player 1 put their token in that space \n'
          '2 means that player 2 put their token in that space \n'
          'Good Luck!\n'
          '=====================================================')


game_rules()


matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
first_row = matrix[0]
second_row = matrix[1]
third_row = matrix[2]


def display_cube():
    print(' --- --- ---')
    print('|', first_row[0], '|', first_row[1], '|', first_row[2], '|')
    print(' --- --- ---')
    print('|', second_row[0], '|', second_row[1], '|', second_row[2], '|')
    print(' --- --- ---')
    print('|', third_row[0], '|', third_row[1], '|', third_row[2], '|')
    print(' --- --- ---')


def prompt_user():
    user_input = int(input("for row 1: enter column b/n 0 - 8, Enter 9 for exit: "))
    return user_input


display_cube()


def prompt_user_again():
    user_input = int(input("wrong input: enter column b/n 0 - 8: "))
    return user_input
    return r


def Place_choice(r):
    # row_a[r]='x'
    return 0


while True:
    r = prompt_user()
    x = str(r)
    if x.isdigit() and (0 <= r <= 8):
        # print('Entered: ', r)
        # first_row[r] = 'x'
        if r == 0:
            first_row[0] = 'x'
        if r == 1:
            first_row[1] = 'x'
        if r == 2:
            first_row[2] = 'x'
        if r == 3:
            second_row[0] = 'x'
        if r == 4:
            second_row[1] = 'x'
        if r == 5:
            second_row[2] = 'x'
        if r == 6:
            third_row[0] = 'x'
        if r == 7:
            third_row[1] = 'x'
        if r == 8:
            third_row[2] = 'x'
        display_cube()
    elif r == 9:
        break
    else:
        prompt_user_again()


####Archive code######
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


        
 

        
