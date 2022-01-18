# Author: Parshan Pourbakht (301429585)
# Date: December 3, 2020
# Title: Even Colored Game
# Title description: The Even colored game is a game where the objective is to get a even sum for every row and column
#                    where at the end of the game a colored box image get presented to the players based off their sums

import random

from createBoardImages import *
import imageManipulation


def opening_instructions():
    """gives opening instructions to the user"""
    print("\nDear player! Welcome to the \"Even Colorful\" game")
    print("==================================================\n")
    print("With this system you will be able to play as many games as you want!")
    print("The point of this game is that all columns and rows in the board must "
          "add to an even number")
    print("- you will be able to choose to play 'solo' or against the computer ('AI'),\n"
          "- you will be able to choose an initial board,\n"
          "- at the end of each game you will win (or lose) points, and\n"
          "- you will see a colorful representation of the game final board results.\n"
          "Enjoy!\n")


def picking_board(board_option):
    """user picks 1 of 3 boards"""
    board_type = ""
    if int(board_option) == 1:
        board_type = "csvFolder/board1.csv"
    elif int(board_option) == 2:
        board_type = "csvFolder/board2.csv"
    elif int(board_option) == 3:
        board_type = "csvFolder/board3.csv"
    else:
        print("Invalid value, re-enter value")
        picking_board(board_option)
    return board_type


def sum_rows(list_of_values):
    """sums up the rows"""
    list_of_sum = []

    for row in list_of_values:
        sum_rows = 0
        for column_item in row:
            sum_rows += int(column_item)
        list_of_sum.append(sum_rows)
    return list_of_sum


def sum_column(list_of_values):
    """sums up the columns"""
    list_of_sums = []
    for i in range(len(list_of_values)):
        sum = 0
        for j in range(len(list_of_values[0])):
            sum += int(list_of_values[j][i])
        list_of_sums.append(sum)
    return list_of_sums


def max_value(list_of_extended_values):
    """finds max value between the final line and final column"""
    this_max_value = 0
    for value in list_of_extended_values:
        if value >= this_max_value:
            this_max_value = value
    return this_max_value


def change_value(this_list, row, column, value):
    """user changes the value in the list_of_values"""
    this_list[row][column] = value


def print_grid(this_list):
    """prints the grid for the users"""
    columns_number = ""
    for i in range(len(this_list) + 1):
        if i == 0:
            columns_number += "\t\t"
        else:
            columns_number += "Col " + str(i - 1) + "\t"
    print(columns_number)
    for j in range(len(this_list)):
        rows = ""

        rows += "Row " + str(j) + "\t"
        for k in range(len(this_list[0])):
            rows += "\t" + str(this_list[j][k]) + "\t"
            if k == (len(this_list) - 1):
                rows += "\n"
        print(rows)

def ai_position_select(this_list):
    """computer randomly generates their value and select their positions"""
    random_value = random.randint(0, 9)
    random_row = random.randint(0, len(this_list) - 1)
    random_column = random.randint(0, len(this_list[0]) - 1)

    print("\nThe AI picked ", random_row, " as their row")
    print("The AI picked ", random_column, " as their column")
    print("The AI picked ", random_value, " as their value\n")

    change_value(this_list, random_row, random_column, random_value)
    print_grid(this_list)


def calculating_points(list_of_values, number_of_turns):
    """calculates the points of the round and returns the value"""
    if number_of_turns != 0:
        final_line = sum_column(list_of_values)
        final_column = sum_rows(list_of_values)

        print("\nThe \"final line\" with the sum of all columns is: ", final_line)
        print("The \"final column\" with the sum of all rows is: ", final_column, "\n")

        list_of_sums = final_line + final_column
        max_value_from_lines = max_value(list_of_sums)
        point = max_value_from_lines // number_of_turns
        print("\nThe points resulting from this board are: ", point)
        print("Points were calculated as: \n\tthe maximum of all numbers in the final line "
              "and column (", max_value_from_lines, ")\n\tdivided by the number of turns "
                                                    "played (", number_of_turns, ")\n")
    else:
        point = 0
    return point


def check_win(this_list):
    """checks both the final column and final row to see if even or odd values exist"""
    for value in this_list:
        if int(value) % 2 != 0:
            return True
    return False


def check_int_value(value):
    """
    Check the passes value (input values) and see if it can be converted to an integer value if not returns a boolean
    """
    try:
        int(value)
    except ValueError:
        return True
    return False


def check_input_validity(lower_limit, higher_limit, name):
    """
    Checks needed integer inputs to see if they are within range of the given lower and higher limits and returns
    valid option

    Pass in arguments that being the parameters lower_limit, higher_limit, name

    name is the string of the you are trying to find

    """
    string_lower = str(lower_limit)
    string_higher = str(higher_limit)
    option = input("Number of " + name + " ? (" + string_lower + ">= and <= " + string_higher + ")")
    while check_int_value(option):  # First checks to see if its not an integer
        print("input is not a integer")
        print("Invalid " + name + ", please enter an integer value.")
        option = input("number of " + name + " ? (" + string_lower + ">= and <= " + string_higher + ")")

    while int(option) > higher_limit or int(option) < lower_limit:  # Check to see if the integer must be in range
        print("Invalid " + name + ", please enter again.")
        option = input("Number of " + name + " ? (" + string_lower + ">= and <= " + string_higher + ")")
        while check_int_value(option):  # If user enters a non integer value again
            print("input is not a integer")
            print("Invalid " + name + ", please enter an integer value.")
            option = input("Number of " + name + " ? (" + string_lower + ">= and <= " + string_higher + ")")

    return option


def play_game_check(user_input):
    bool_play = False
    while user_input != 'y' and user_input != 'n':
        print("invalid answer, try again")
        user_input = input("Would you like to play? (y/n)").lower()
    if user_input == 'y':
        bool_play = True
    elif user_input == 'n':
        bool_play = False
    return bool_play


def check_validity_string(user_input, first_string_bound, second_string_bound, dialog_string):
    while not check_int_value(user_input):
        print("You entered an integer value")
        print("Invalid value, please re-enter")
        user_input = input(dialog_string)
        while user_input.lower() != first_string_bound and user_input.lower() != second_string_bound:
            print("Invalid value, please re-enter")
            user_input = input(dialog_string)
    while user_input.lower() != first_string_bound and user_input.lower() != second_string_bound:
        print("Invalid value, please re-enter")
        user_input = input(dialog_string)
        while not check_int_value(user_input):
            print("You entered an integer value")
            print("Invalid value, please re-enter")
            user_input = input(dialog_string)

    return user_input.lower()


opening_instructions()  # Displays opening instructions

bool_play = False  # Boolean that determines whether or not a game continues, initializes to False
play_option = input("Would you like to play? (y/n)").lower()

# check_validity makes sure its a valid input
play_option = check_validity_string(play_option, "y", "n", "Would you like to play? (y/n)")

# play_game_check makes sure the user whether the user wants to play based off the passed play_option value
bool_play = play_game_check(play_option)

total_user_points = 0  # Total user points
total_ai_points = 0  # Total ai points
ai_games_won = 0  # Number of ai wins
user_games_won = 0  # Number of user wins

# Loop is governed based of the value of bool_play
while bool_play:
    # game_option is the game type the user wants to play. Either Ai or solo mode.
    game_option = input("What level would you want to play (\'solo\' or \'AI\'): ").lower()

    # check_validity_string checks to see if the inputs are correct
    game_option = check_validity_string(game_option, "solo", "ai",
                                        "What level would you want to play (\'solo\' or \'AI\'): ")

    # check_input_validity is checking the board input of the user. Passing arguments 1, 3, "board"
    board_option = check_input_validity(1, 3, "board")
    board = picking_board(board_option)

    # Open the chosen board file
    board_file = open(board)

    # Read lines and slice the unneeded header/line
    lines_board = board_file.readlines()[1:]
    list_of_values = []

    # Iterate through lines, spliting the values at the commas and appending it to the list list_of_values
    for line in lines_board:
        list_of_values.append(line.strip().split(","))

    turns1 = len(list_of_values) - 1
    turns2 = len(list_of_values) ** 2 - 1

    print("\nTurn options:")
    print("Type 1 for max turns being ", turns1)
    print("Type 2 for max turns being ", turns2)

    turn_option = int(check_input_validity(1, 2, " turn option would you like? "))

    if turn_option == 1:
        max_turns = turns1
    else:
        max_turns = turns2

    print("max turn is ", max_turns)

    print("\nDear user, for this round the max amount of turn you can pick is ", max_turns, "\n")

    # Make sure the entered number of turns is both within range and is not a string with check_input_validity
    number_of_turns = int(check_input_validity(0, max_turns, "turns"))

    # Continues with game is entered turn is not 0, otherwise there would be no winner of this game

    if game_option.lower() == 'ai':  # Ai mode
        print("\nAi Mode:")
        print("\nStarting board:\n======================================================")
        print_grid(list_of_values)  # Print grid first prints the given starting board
        turns = random.randint(0, 1)  # randomizes who starts first between Ai and user
        turns_counter = 1

        # Turns alternate from 0 to 1 (user to ai) until turns_counter equals entered turns
        while turns_counter <= (2 * number_of_turns):
            if turns == 0:
                turns = 1

                print("\nUsers turn: \n======================================================")

                print("Enter -1 to quit entry")
                entered_row = int(check_input_validity(-1, len(list_of_values) - 1, "row"))

                if entered_row == -1:
                    break

                entered_column = int(check_input_validity(-1, len(list_of_values) - 1, "column"))

                if entered_column == -1:
                    break

                value = int(check_input_validity(-1, 9, "value"))

                if value == -1:
                    break

                change_value(list_of_values, entered_row, entered_column, value)
                print_grid(list_of_values)
            else:
                turns = 0
                print("\nAI's turn: \n======================================================")
                ai_position_select(list_of_values)  # Ai selects their position and value in the grid
            turns_counter += 1
        point_this_round = calculating_points(list_of_values, number_of_turns)  # Shows point system this round


    else:  # Solo mode
        print("\nSolo Mode:")
        print("Starting board:\n======================================================")
        print_grid(list_of_values)

        for turn in range(number_of_turns):  # Goes through the number of turns

            print("Enter -1 to quit program")
            entered_row = int(check_input_validity(-1, len(list_of_values) - 1, "row"))

            if entered_row == -1:
                break

            entered_column = int(check_input_validity(-1, len(list_of_values) - 1, "column"))

            if entered_column == -1:
                break

            value = int(check_input_validity(-1, 9, "value"))

            if value == -1:
                break

            change_value(list_of_values, entered_row, entered_column, value)
            print_grid(list_of_values)

        point_this_round = calculating_points(list_of_values, number_of_turns)

    final_column = sum_rows(list_of_values)  # Obtain the list of summed values for the final line
    final_line = sum_column(list_of_values)  # Obtain the list of summed values for the final column
    list_of_both_finals = final_column + final_line  # Combine both lists (final_column and final_row) into one list

    bool_not_win = check_win(list_of_both_finals)  # Check to see who won, passing the combined list as an argument

    if bool_not_win:  # User loses
        print("Sadly you lost this round.")
        total_ai_points += point_this_round  # Adding points of the ai
        total_user_points -= point_this_round  # Subtracting points of the user
        ai_games_won += 1  # Adding 1 to the number of ai games won
        print("You have ", total_user_points, " points and the computer has ", total_ai_points, " points")


    else:  # User wins
        print("nice you won this round!")
        total_user_points += point_this_round  # Adding points of the user
        total_ai_points -= point_this_round  # Subtracting points of the ai
        user_games_won += 1  # Adding 1 to the number of user games won

        print("You have ", total_user_points, " points")

    box_length = int(check_input_validity(40, 60, "box length"))  # User enters desired box length
    colors_file = open("csvFolder/colorcoding.csv")  # Open colors file
    lines_colors = colors_file.readlines()[1:]  # Read lines of the file and slice unneeded header/line
    list_of_colors = []

    # Itterates through the lines in lines_color and splits values and appends them into list_of_colors
    for line in lines_colors:
        list_of_colors += [line.strip().split(",")]

    # shows final line image
    list_image_final_line = show_final_line(list_of_colors, final_line, box_length)
    imageManipulation.showImage(list_image_final_line, "final row")

    input("Here is the final line, press anything to continue: ")

    # shows final column image
    list_image_final_column = show_final_column(list_of_colors, final_column, box_length)
    imageManipulation.showImage(list_image_final_column, "final column")

    input("Here is the final column, press anything to continue: ")

    play_option = input("Would you like to play? (y/n)").lower()
    bool_play = play_game_check(play_option)

if total_ai_points > total_user_points:
    print("Sorry but you lost the game.")
elif total_ai_points < total_user_points:
    print("Nice you won!")
else:
    print("Tie!")

print("\nTOTAL OF ALL GAMES\n======================================================\n")
print("Total points user in all games", total_user_points)
print("Total games the user won: ", user_games_won)
print("Total games ai won: ", ai_games_won)

print("\nBye!!!")
