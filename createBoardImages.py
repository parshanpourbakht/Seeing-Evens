def show_final_line(list_of_colors, final_line, box_length):
    """
    The function takes in the list of color values, the list of sum values in the final line, and the box length

    Based off these three parameters the function returns a list representing the horizontal colored boxes with
    the black bars in between
    """
    list_image_final_line = []
    for value in final_line:
        for row in list_of_colors:
            if value == int(row[0]):
                row[1] = int(row[1])
                row[2] = int(row[2])
                row[3] = int(row[3])

                # list_image_final_line is a 2D list of RGB values and accumulates the number of pixels for the image
                list_image_final_line += [[row[1:]] * box_length] * box_length + [[[0, 0, 0]] * box_length] * 10

    return list_image_final_line


def show_final_column(list_of_colors, final_column, box_length):
    """
    The function takes in the list of color values, the list of sum values in the final column, and the box length

    Based off these three parameters the function returns a list representing the vertical  colored boxes with
    the black bars in between
    """
    column_list = []
    list_image_final_column = []
    for value in final_column:
        for row in list_of_colors:
            if value == int(row[0]):
                row[1] = int(row[1])
                row[2] = int(row[2])
                row[3] = int(row[3])

                # list_image_final_column is a 2D list of RGB values and accumulates the number of pixels for the image
                column_list += [row[1:]] * box_length + [[0, 0, 0]] * 10
    list_image_final_column += [column_list] * box_length
    return list_image_final_column

