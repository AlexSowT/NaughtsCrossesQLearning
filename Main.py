import random
import numpy as np
import pygame, sys
from pygame.locals import *

comp2Win = 0
comp1Wins = 0
numDraw = 0


def draw_grid(field):
    print("----")

    print("[",field[0], ",", field[1], ",",field[2], "]", "\n")
    print("[",field[3], ",", field[4], ",",field[5], "]", "\n")
    print("[",field[6], ",", field[7], ",",field[8], "]", "\n")

    return


def check_win(field):
    winning_lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    for x in winning_lines:
        for i in range(0,2):
            if field[x[0]] == field[x[1]] and field[x[1]] == field[x[2]] and field[x[0]] != 0:
                return True
    return False


def check_draw(field):
    zeroCount = 0
    for i in range(0,8):
            if field[i] == 0:
                zeroCount += 1
    if zeroCount == 0 and check_win(field) == False:
        return True
    return False


def play_game_learning(state, action):
    if state[action] == 0:
        state[action] = 1
    else:
        return state, -20, True

    if check_win(state):
        return state, 5, True

    if check_draw(state):
        return state, -1, True

    playable_moves = []
    for i in range(0, len(state)):
        if state[i] == 0:
            playable_moves.append(i)

    computer_two_move_space = playable_moves[random.randint(0, len(playable_moves)-1)]
    state[computer_two_move_space] = 2

    if check_win(state):
        return state, -20, True
    if check_draw(state):
        return state, -1, True

    return state, 0, False


def play_game(field, move,  bot):

    play = True
    while play:
        state = find_index(field)
        action = np.argmax(bot[state])
        draw_grid(field)
        if field[action] == 0:
            field[action] = 1
        else:
            print("Illegal move")
            return True

        if check_win(field):
            print("Computer one wins")
            draw_grid(field)
            return True
        if check_draw(field):
            print("Its a draw")
            draw_grid(field)
            return True

        draw_grid(field)
        field[move] = 2

        if check_win(field):
            print("You win")
            draw_grid(field)
            return
        if check_draw(field):
            print("Its a draw")
            draw_grid(field)
            return


def generate_list_of_states():
    field = [0, 0, 0,
             0, 0, 0,
             0, 0, 0]

    list_of_states_move_one = []
    list_of_states_move_two = []
    list_of_states_move_three = []
    list_of_states_move_four = []
    list_of_states_move_five = []
    list_of_states_move_six = []
    list_of_states_move_seven = []
    list_of_states_move_eight = []
    list_of_states_move_nine = []

    list_of_states_total = [list_of_states_move_one,
                            list_of_states_move_two,
                            list_of_states_move_three,
                            list_of_states_move_four,
                            list_of_states_move_five,
                            list_of_states_move_six,
                            list_of_states_move_seven,
                            list_of_states_move_eight,
                            list_of_states_move_nine,]

    playable_moves = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    for i in range(0, len(playable_moves)):
        field[i] = 1
        list_of_states_move_one.append(field.copy())
        field[i] = 0

    for one_field in list_of_states_move_one:
        for i in range(0, len(playable_moves)):
            if one_field[i] == 0:
                one_field[i] = 2
                if not check_if_in_list(one_field, list_of_states_move_two):
                    list_of_states_move_two.append(one_field.copy())
                one_field[i] = 0

    for two_field in list_of_states_move_two:
        for i in range(0, len(playable_moves)):
            if two_field[i] == 0:
                two_field[i] = 1
                if not check_if_in_list(two_field, list_of_states_move_three):
                    list_of_states_move_three.append(two_field.copy())
                two_field[i] = 0

    for three_field in list_of_states_move_three:
        for i in range(0, len(playable_moves)):
            if three_field[i] == 0:
                three_field[i] = 2
                if not check_if_in_list(three_field, list_of_states_move_four):
                    list_of_states_move_four.append(three_field.copy())
                three_field[i] = 0

    for four_field in list_of_states_move_four:
        for i in range(0, len(playable_moves)):
            if four_field[i] == 0:
                four_field[i] = 1
                if not check_if_in_list(four_field, list_of_states_move_five):
                    list_of_states_move_five.append(four_field.copy())
                four_field[i] = 0

    for five_field in list_of_states_move_five:
        for i in range(0, len(playable_moves)):
            if five_field[i] == 0:
                five_field[i] = 2
                if not check_if_in_list(five_field, list_of_states_move_six):
                    list_of_states_move_six.append(five_field.copy())
                    five_field[i] = 0

    for six_field in list_of_states_move_six:
        for i in range(0, len(playable_moves)):
            if six_field[i] == 0:
                six_field[i] = 1
                if not check_if_in_list(six_field, list_of_states_move_seven):
                    list_of_states_move_seven.append(six_field.copy())
                    six_field[i] = 0

    for seven_field in list_of_states_move_seven:
        for i in range(0, len(playable_moves)):
            if seven_field[i] == 0:
                seven_field[i] = 2
                if not check_if_in_list(seven_field, list_of_states_move_eight):
                    list_of_states_move_eight.append(seven_field.copy())
                    seven_field[i] = 0

    for eight_field in list_of_states_move_eight:
        for i in range(0, len(playable_moves)):
            if eight_field[i] == 0:
                eight_field[i] = 1
                if not check_if_in_list(eight_field, list_of_states_move_nine):
                    list_of_states_move_nine.append(eight_field.copy())
                    eight_field[i] = 0

    final_list = []
    file = open("possible_moves.txt", "w+")
    for i in list_of_states_total:
        for j in i:
            final_list.append(j)
            file.write(str(j))
            file.write("\n")
    final_list.append(field)
    file.write(str(field))
    file.close()

    return final_list


def learning_time():
    bot_one_q_table = np.zeros((6046, 9))
    explore_rate = 0.3
    lr = 0.2
    gamma = 0.7
    epochs = 500000

    for epoch in range(0, epochs):
        print(epoch)
        field = [0, 0, 0,
                 0, 0, 0,
                 0, 0, 0]
        stop = False
        while not stop:
            state = find_index(field)
            if random.uniform(0,1) < explore_rate:
                #Exploit
                action = np.argmax(bot_one_q_table[state])
                new_field, reward, stop = play_game_learning(field, action)
                new_state = find_index(new_field)
                bot_one_q_table[state, action] = bot_one_q_table[state, action] + lr * (
                reward + gamma * np.max(bot_one_q_table[new_state, :]) - bot_one_q_table[state, action])
            else:
                #Explore
                action = random.randint(0, 8)
                new_field, reward, stop = play_game_learning(field, action)
                new_state = find_index(new_field)
                bot_one_q_table[state, action] = bot_one_q_table[state, action] + lr * (reward + gamma * np.max(bot_one_q_table[new_state, :]) - bot_one_q_table[state, action])
            field = new_field
    file = open("bot_one_q_table.txt", 'w+')
    for i in bot_one_q_table:
        file.write(str(i))
    file.close()
    return bot_one_q_table


def check_if_in_list(field, list):
    return False


def find_index(field):
    for i in range(0, len(list_of_states)):
        if list_of_states[i] == field:
            return i


#
#list_of_states = generate_list_of_states()


def load_moves():
    states = []
    with open("possible_moves.txt") as moves:
        for line in moves:
            temp_list = []
            for num in line:
                if num == str("\n"):
                    pass
                else:
                    temp_list.append(int(num))
            states.append(temp_list)
    return states


def load_bot():
    q_table = np.zeros((6046, 9))
    with open("bot_one_q_table.txt") as file_q_table:
        line_num = 0
        for line in file_q_table:
            numbs = line.split(" ")
            for i in range(0, 9):
                q_table[line_num, i] = float(numbs[i])
            line_num += 1

    return q_table


def main_game(bot):
    pygame.init()
    screen = pygame.display.set_mode((640, 640))
    pygame.display.set_caption("First Pygame Application")
    clock = pygame.time.Clock()

    BLACK = 0, 0, 0
    WHITE = 255, 255, 255

    field = [0, 0, 0,
                 0, 0, 0,
                 0, 0, 0]


    player_turn = True;
    waiting = False
    while True:
        clock.tick(50)
        mouse = pygame.mouse.get_pos()

        if not waiting:
            state = find_index(field)
            action = np.argmax(bot[state])

            if field[action] == 0:
                field[action] = 1
            else:
                print("Illegal move")
                break

            if check_win(field):
                print("Computer one wins")
                draw_grid(field)
                break
            if check_draw(field):
                print("Its a draw")
                draw_grid(field)
                break
        waiting = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                # print event.button
                if mouse[0] > 0 and mouse[0] < 213 and mouse[1] > 0 and mouse[1] < 213:
                    if player_turn:
                        field[0] = 2
                        waiting = False
                if mouse[0] > 213 and mouse[0] < 426 and mouse[1] > 0 and mouse[1] < 213:
                    if player_turn:
                        field[1] = 2
                        waiting = False
                if mouse[0] > 426 and mouse[0] < 640 and mouse[1] > 0 and mouse[1] < 213:
                    if player_turn:
                        field[2] = 2
                        waiting = False
                if mouse[0] > 0 and mouse[0] < 213 and mouse[1] > 213 and mouse[1] < 426:
                    if player_turn:
                        field[3] = 2
                        waiting = False
                if mouse[0] > 213 and mouse[0] < 426 and mouse[1] > 213 and mouse[1] < 426:
                    if player_turn:
                        field[4] = 2
                        waiting = False
                if mouse[0] > 426 and mouse[0] < 640 and mouse[1] > 213 and mouse[1] < 426:
                    if player_turn:
                        field[5] = 2
                        waiting = False
                if mouse[0] > 0 and mouse[0] < 213 and mouse[1] > 426 and mouse[1] < 640:
                    if player_turn:
                        field[6] = 2
                        waiting = False
                if mouse[0] > 213 and mouse[0] < 426 and mouse[1] > 426 and mouse[1] < 640:
                    if player_turn:
                        field[7] = 2
                        waiting = False
                if mouse[0] > 426 and mouse[0] < 640 and mouse[1] > 426 and mouse[1] < 640:
                    if player_turn:
                        field[8] = 2
                        waiting = False


        screen.fill(BLACK)

        if field[0] == 1:
            pygame.draw.circle(screen, WHITE, (106, 106), 60, 3)
        if field[0] == 2:
            pygame.draw.line(screen, WHITE, (40, 40), (176,176), 4)
            pygame.draw.line(screen, WHITE, (176, 40), (40,176), 4)

        if field[1] == 1:
            pygame.draw.circle(screen, WHITE, (319, 105), 60, 3)
        if field[1] == 2:
            pygame.draw.line(screen, WHITE, (253, 40), (389,176), 4)
            pygame.draw.line(screen, WHITE, (389, 40), (253,176), 4)

        if field[2] == 1:
            pygame.draw.circle(screen, WHITE, (532, 105), 60, 3)
        if field[2] == 2:
            pygame.draw.line(screen, WHITE, (466, 40), (602,176), 4)
            pygame.draw.line(screen, WHITE, (602, 40), (466,176), 4)

        if field[3] == 1:
            pygame.draw.circle(screen, WHITE, (106, 319), 60, 3)
        if field[3] == 2:
            pygame.draw.line(screen, WHITE, (40, 253), (176,389), 4)
            pygame.draw.line(screen, WHITE, (176, 253), (40,389), 4)

        if field[4] == 1:
            pygame.draw.circle(screen, WHITE, (319, 319), 60, 3)
        if field[4] == 2:
            pygame.draw.line(screen, WHITE, (253, 253), (389,389), 4)
            pygame.draw.line(screen, WHITE, (389, 253), (253,389), 4)

        if field[5] == 1:
            pygame.draw.circle(screen, WHITE, (532, 319), 60, 3)
        if field[5] == 2:
            pygame.draw.line(screen, WHITE, (466, 253), (602,389), 4)
            pygame.draw.line(screen, WHITE, (602, 253), (466,389), 4)

        if field[6] == 1:
            pygame.draw.circle(screen, WHITE, (106, 532), 60, 3)
        if field[6] == 2:
            pygame.draw.line(screen, WHITE, (40, 466), (176,602), 4)
            pygame.draw.line(screen, WHITE, (176, 466), (40,602), 4)

        if field[7] == 1:
            pygame.draw.circle(screen, WHITE, (319, 532), 60, 3)
        if field[7] == 2:
            pygame.draw.line(screen, WHITE, (253, 466), (389,602), 4)
            pygame.draw.line(screen, WHITE, (389, 466), (253,602), 4)

        if field[8] == 1:
            pygame.draw.circle(screen, WHITE, (532, 532), 60, 3)
        if field[8] == 2:
            pygame.draw.line(screen, WHITE, (466, 466), (602,602), 4)
            pygame.draw.line(screen, WHITE, (602, 466), (466,602), 4)

        pygame.draw.line(screen, WHITE, (213, 0), (213, 640), 5)
        pygame.draw.line(screen, WHITE, (426, 0), (426, 640), 5)

        pygame.draw.line(screen, WHITE, (0, 213), (640, 213), 5)
        pygame.draw.line(screen, WHITE, (0, 426), (640, 426), 5)

        pygame.display.flip()


list_of_states = load_moves()
main_game(load_bot())


