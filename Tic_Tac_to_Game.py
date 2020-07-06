from IPython.display import clear_output

def print_board(board):

    ''' This function will display the board after each input '''

    clear_output()
    print(board[0] + '    |    ' + board[1] + '    |   ' + board[2])
    print('------------------')
    print(board[3] + '    |    ' + board[4] + '    |   ' + board[5])
    print('------------------')
    print(board[6] + '    |    ' + board[7] + '    |   ' + board[8])

def validate_input(master_list):

    ''' This function will validate user input every time user will enter a number '''
    choice = 'Wrong'
    while True:
        try:
            choice = input ('Enter Number between 1 to 9 : ')

            if (choice.isdigit() == False):

                print('You have not entered a digit. please re-enter the Input between 1 to 9')
                raise

            elif(choice.isdigit() == True and (int(choice) == 0) or (int(choice) > 9)):

                print('please re-enter the Input between 1 to 9 only')
                raise

            elif not( master_list[int(choice)-1] == '' ):

                print('This slot is already selected earlier , please choose a empty slot')
                raise
        except:
            continue
        else:
            break

    return int(choice)

def validate_victory(input_list,input_pattern):

    ''' This function will validate victory check after each input from user '''
    if ( ( input_list[0] == input_list[1] and input_list[1] == input_list[2] and input_list[2] == input_pattern)
    or
    ( input_list[3] == input_list[4] and input_list[4] == input_list[5] and input_list[5] == input_pattern)
    or
    ( input_list[6] == input_list[7] and input_list[7] == input_list[8] and input_list[8] == input_pattern)
    or
    ( input_list[0] == input_list[3] and input_list[3] == input_list[6] and input_list[6] == input_pattern)
    or
    ( input_list[1] == input_list[4] and input_list[4] == input_list[7] and input_list[7] == input_pattern)
    or
    ( input_list[2] == input_list[5] and input_list[5] == input_list[8] and input_list[8] == input_pattern)
    or
    (input_list[0] == input_list[4] and input_list[4] == input_list[8] and input_list[8] == input_pattern)
    or
    (input_list[2] == input_list[4] and input_list[4] == input_list[6] and input_list[6] == input_pattern)
    ):
        return 1
    else:
        return 0

def take_input():

    ''' This function will validate Initial Input from user to select X or O and assign
     input pattern accordingly'''

    input_1 =''
    input_2 = ''
    while True:
        try:
         input_1 = input("please enter value between X & O : ").upper()
         if not(input_1 == 'X' or input_1 == 'O' ):
            raise
        except:
         print ( 'please enter value between X & O only')
         continue
        else:
         print ('Thanks for your Input')
         if (input_1 =='X'):
             input_2 ='O'
         else:
             input_2 = 'X'

         break

    print('Player 1 is assigned {} and Player 2 is assigned {}  as input pattern'.format(input_1,input_2))

    return input_1,input_2



lst=['','','','','','','','','']
Input_1 = input("You want to Play the game : Yes or No : ")
loop_count = 1

if (Input_1.upper() == 'YES') :

    Input_pattern_player1,Input_pattern_player2 = take_input()

    while (loop_count < 10 ) :

        print_board(lst)
        if (loop_count%2 == 0 ):
            print ('Player 2 --> Please make your selection for the spot')
            user_input = validate_input(lst)
            lst[user_input-1] = Input_pattern_player2
            victory_flag = validate_victory(lst, Input_pattern_player2)
            if  victory_flag == 1 :
                print (' Congratulations , Player 2 won the Game')
                print_board(lst)
                break
        else:
            print('Player 1 --> Please make your selection for the spot')
            user_input=validate_input(lst)
            lst[user_input-1] = Input_pattern_player1
            victory_flag = validate_victory(lst, Input_pattern_player1)
            if victory_flag == 1 :
                print(' Congratulations , Player 1 won the Game')
                print_board(lst)
                break
        loop_count = loop_count + 1

    else:
        print('Thank you for playing. No Result !!!')
else:
        print('Thank you for playing')