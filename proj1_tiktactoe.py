
#Israel Kinfu
#print 3X3 Matrix
#prompt user and displey it on Matrix
#add player detail - player one and two


def main():
    game_rules()
    display_cube()
    #symbol1,symbol2=player_detail()
    run_the_game()


def game_rules():
    print('=====================================================\n'
          'Game rules:\n'
          "Player 1 and player 2, represented by X and O, take turns \n"
          "marking the spaces in a 3*3 grid. The player who succeeds in placing \n "
          "three of their marks in a horizontal, vertical, or diagonal row wins. \n"

          '1 means that player 1 put their token in that space \n'
          '2 means that player 2 put their token in that space \n'

          'Good Luck!\n'
          '=====================================================')


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


def prompt_user_again():
    user_input = int(input("wrong input: enter column b/n 0 - 8: "))
    return user_input
    return r


def Place_choice(r):
    # row_a[r]='x'
    return 0


def player_detail():
    player_symbol=str(input("player 1 do you want to be X or O ? "))
    if player_symbol == 'x' or player_symbol == 'X':
        player_symbol1 = 'X'
        player_symbol2 = 'O'
        print("player 1 is ",player_symbol1,"\n"
              "player 2 is ",player_symbol2)
    elif player_symbol =='o' or player_symbol =='O':
        player_symbol1 = 'O'
        player_symbol2 = 'X'
        print("player 1 is is",player_symbol1,"\n"
              "player 2 is is",player_symbol2)
    return player_symbol1,player_symbol2

def whoiswinner():
    print()
    print('*****************************')
    print('congragulations player X won')
    print('*****************************')

def iswinner():
    if first_row[0]==first_row[1]==first_row[2] :
        whoiswinner()
    elif second_row[0]==second_row[1]==second_row[2]:
        whoiswinner()

def run_the_game():
    player_symbol1,player_symbol2=player_detail()
    while True:
        r = prompt_user()
        x = str(r)
        if x.isdigit() and (0 <= r <= 8):
            # print('Entered: ', r)
            # first_row[r] = 'x'
            if r == 0:
                first_row[0] = player_symbol1
            if r == 1:
                first_row[1] = player_symbol1
            if r == 2:
                first_row[2] = player_symbol1
            if r == 3:
                second_row[0] = player_symbol1
            if r == 4:
                second_row[1] = player_symbol1
            if r == 5:
                second_row[2] = player_symbol1
            if r == 6:
                third_row[0] = player_symbol2
            if r == 7:
                third_row[1] = player_symbol2
            if r == 8:
                third_row[2] = player_symbol2
            display_cube()
            iswinner()
        elif r == 9:
            break
        else:
            prompt_user_again()

#call the main function
main()




        
 

        
