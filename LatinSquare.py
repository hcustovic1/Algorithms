########################################################################
# Title: Latin Square
# Comments: Program for reading the incomplete Latin Square from a
#           CSV file, completing it, and storing it in a new CSV
#           file afterwards.
########################################################################

import os


# Function for loading and parsing latin square from a CSV file
def read_latin_square(file):
    input_matrix = list()

    if not os.path.isfile(file):
        return False

    # Open CSV file for reading
    with open(file, "r") as f:

        # Parse line of the CSV file
        for line in f.readlines():
            # Row values are separated by ; in CSV file
            input_matrix_line = line.split(';')
            input_matrix_numbers = []

            for input_matrix_line_element in input_matrix_line:
                # Empty row elements will be recorded as None in input matrix
                if input_matrix_line_element == "" or input_matrix_line_element == "\n":
                    input_matrix_numbers.append(None)
                else:
                    input_matrix_numbers.append(int(input_matrix_line_element))

            input_matrix.append(input_matrix_numbers)

    return input_matrix


# Checks whether latin square is valid by rows and columns
def check_validity(latin_square):

    # Useful to check whether duplicates exist in matrix columns
    transpose_latin_square = [list(x) for x in zip(*latin_square)]

    latin_square_row_dimensions = list()
    latin_square_column_dimensions = list()

    # Check for duplicates by rows
    for line in latin_square:
        row_count = set([x for x in line if x is not None and line.count(x) > 1])
        latin_square_row_dimensions.append(len(line))

        if len(row_count) > 0:
            return False

    # Check for duplicates by columns
    for transpose_line in transpose_latin_square:
        column_count = set([x for x in transpose_line if x is not None and transpose_line.count(x) > 1])
        latin_square_column_dimensions.append(len(transpose_line))

        if len(column_count) > 0:
            return False

    if len(set(latin_square_row_dimensions)) > 1 or len(set(latin_square_column_dimensions)) > 1 \
            or set(latin_square_column_dimensions) != set(latin_square_row_dimensions):
        return False

    return True


def get_possible_elements(latin_square, row, column):
    possible_elements = set(range(1, len(latin_square) + 1))
    transpose_latin_square = [list(x) for x in zip(*latin_square)]

    return list((possible_elements - set(latin_square[row])) - set(transpose_latin_square[column]))


def find_latin_square_next_blank_spot(latin_square):
    for i in range(len(latin_square)):
        for j in range(len(latin_square)):
            if latin_square[i][j] is None:
                return [i, j]

    return [None, None]


# Function for completing the latin square
def solve_latin_square(latin_square):

    row, column = find_latin_square_next_blank_spot(latin_square)

    # if the latin square is complete, solution matrix should be returned from function
    if row is None and column is None:
        return True

    for next_value in get_possible_elements(latin_square, row, column):

        latin_square[row][column] = next_value

        if solve_latin_square(latin_square):
            return True

        # If the value can not be a part of the solution go one step back in the backtracking algorithm
        latin_square[row][column] = None

    return False


# Function for storing the solution matrix in output CSV file
def store_latin_square(file, latin_square):
    with open(file, "w") as f:
        for line in latin_square:
            f.write(";".join([str(i) for i in line]))
            f.write("\n")


def main():
    latin_square = read_latin_square("input.csv")

    if not latin_square:
        print("[ERROR] Input CSV file not found!")
        exit()

    if check_validity(latin_square):

        solve_latin_square(latin_square)
        store_latin_square("output.csv", latin_square)

        print("The Latin Square you provided is valid! I have computed a solution and stored it in output.csv!")

    else:
        print("The Latin Square you provided is invalid! Please replace input.csv and try again!")


if __name__ == '__main__':
    main()
