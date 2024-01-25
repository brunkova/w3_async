def right_justify(string_s):
    left_string = ""
    i = 1
    while i < 70 - len(string_s):
        left_string += " "
        i += 1
    print(left_string, string_s)


def print_spam(spam):
    print(spam)


def do_twice(f_function, v_value):
    f_function(v_value)
    f_function(v_value)


def do_four(f_function, v_value):
    do_twice(f_function, v_value)
    do_twice(f_function, v_value)


def draw_grid(row, column):
    corner_row = "+"
    side_row =  "|"
    corner_row_repetition = "----+"
    side_row_repetition = "    |"

    full_corner_row = corner_row + corner_row_repetition * column
    full_side_row = side_row + side_row_repetition * column

    table_row = 0

    while table_row < row:
        print(full_corner_row)
        side_row_printed = 0
        while side_row_printed < 5:
            print(full_side_row)
            side_row_printed += 1
        table_row += 1
    print(full_corner_row)

draw_grid(3,6)