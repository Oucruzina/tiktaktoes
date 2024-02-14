import random
def fun_graph():
    print(f'\n{game_state[0]} # {game_state[1]} # {game_state[2]}\n'
          '# # # # #\n'
          f'{game_state[3]} # {game_state[4]} # {game_state[5]}\n'
          '# # # # #\n'
          f'{game_state[6]} # {game_state[7]} # {game_state[8]}\n')
def detect_win(game_state):
    a = 0
    b = 1
    c = 2
    for i in range(3):
        if game_state[a] + game_state[b] + game_state[c] == 'XXX':
            return 'X wins'
        elif game_state[a] + game_state[b] + game_state[c] == 'OOO':
            return 'O wins'
        a += 3
        b += 3
        c += 3
    a = 0
    b = 3
    c = 6
    for i in range(3):
        if game_state[a] + game_state[b] + game_state[c] == 'XXX':
            return 'X wins'
        elif game_state[a] + game_state[b] + game_state[c] == 'OOO':
            return 'O wins'
        a += 1
        b += 1
        c += 1
    if game_state[0] + game_state[4] + game_state[8] == 'XXX':
        return 'X wins'
    elif game_state[0] + game_state[4] + game_state[8] == 'OOO':
        return 'O wins'
    if game_state[2] + game_state[4] + game_state[6] == 'XXX':
        return 'X wins'
    elif game_state[2] + game_state[4] + game_state[6] == 'OOO':
        return 'O wins'
    return None
def ai_player():
    if ai_diff == 'hard' or ai_diff == 'very hard':
        for i in range (9):
            test_state = []
            test_state += game_state
            if game_state[i] != ai_char and game_state[i] != user_char:
                test_state[i] = ai_char
                if detect_win(test_state) != None:
                    return i
                test_state[i] = user_char
                if detect_win(test_state) != None:
                    return i
    if ai_diff == 'easy' or ai_diff == 'very hard':
        test_list = []
        even_list = []
        odd_list = []
        for i in range(9):
            if game_state[i] != 'X' and game_state[i] != 'O':
                test_list.append(i)
        if test_list.count(4) == 1:
            return 4
        else:
            for i in range(len(test_list)):
                if test_list[i] % 2 == 0:
                    even_list.append(test_list[i])
                else:
                    odd_list.append(test_list[i])
            if len(even_list) != 0:
                return even_list[random.randrange(len(even_list))]
            else:
                return odd_list[random.randrange(len(odd_list))]
    if ai_diff == 'very easy' or ai_diff == 'hard':
        test_list = []
        for i in range(9):
            if game_state[i] != 'X' and game_state[i] != 'O':
                test_list.append(i)
        return test_list[random.randrange(len(test_list))]
game_state = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
game_type = 0
while game_type != '1' and game_type != '2':
    print('Would you like to play by yourself, or with a friend?\n')
    game_type = input('Enter number, 1 or 2:')
    if game_type != '1' and game_type != '2':
        print('That wasnt "1" or "2", idiot.\n')
if game_type == '2':
    print('2 player game:')
    user_in = -1
    moves = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    fun_graph()
    for i in range(9):
        if detect_win(game_state) != None:
            print(detect_win(game_state))
            break
        if i % 2 == 0:
            while moves.count(user_in) == 0:
                user_in = int(input("p1, enter value:"))
                if user_in < 0 or user_in > 8:
                    print("That's not a number 0-8, dummy.\n")
                if moves.count(user_in) == 0:
                    print("That's not an available move, dumb dumb bubble gum\n.")
            game_state[user_in] = 'X'
            fun_graph()
        else:
            while moves.count(user_in) == 0:
                user_in = int(input("p2, enter value:"))
                if user_in < 0 or user_in > 8:
                    print("That's not a number 0-8, dummy.\n")
                if moves.count(user_in) == 0:
                    print("That's not an available move, dumb dumb bubble gum.\n")
            game_state[user_in] = 'O'
            fun_graph()
        moves.remove(user_in)
    else:
        if detect_win(game_state) != None:
            print(detect_win(game_state))
        else:
            print('Tie')
elif game_type == '1':
    moves = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    x = '0'
    ai_diff = 0
    print('\n1 player game:')
    while ai_diff != 'very easy' and ai_diff != 'easy' and ai_diff != 'hard' and ai_diff != 'very hard':
        #asks user for difficulty
        print('Select ai difficulty:')
        print('very easy        easy\nvery hard        hard')
        ai_diff = input()
        if ai_diff != 'very easy' and ai_diff != 'easy' and ai_diff != 'hard' and ai_diff != 'very hard':
            print("That wasn't an option, stupid.\n")
    while x != '1' and x != '2':
        #asks user for move order
        print('Would you like to go first or second?\n')
        x = input('Enter number, 1 or 2:')
        if x == '1':
            user_char = 'X'
            ai_char = 'O'
            evenness = 0
            fun_graph()
        elif x == '2':
            user_char = 'O'
            ai_char = 'X'
            evenness = 1
        else:
            print('That wasnt "1" or "2", idiot.\n')
    for i in range(9):
        #play begins 
        user_in = -1
        if detect_win(game_state) != None:
            #win detection
            print(detect_win(game_state))
            fun_graph()
            break
        if i % 2 == evenness:
            #player turn
            while moves.count(user_in) == 0:
                user_in = int(input("p1, enter value:"))
                if user_in < 0 or user_in > 8:
                    print("That's not a number 0-8, dummy.\n")
                if moves.count(user_in) == 0:
                    print("That's not an available move, dumb dumb bubble gum\n.")
            game_state[user_in] = user_char
            moves.remove(user_in)
        else:
            #ai turn
            x = ai_player()
            game_state[x] = ai_char
            moves.remove(x)
            fun_graph()
    else:
        print('Tie')
        fun_graph()

            



















                
