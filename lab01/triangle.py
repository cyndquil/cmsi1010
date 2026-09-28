def print_triangle(character, lines):
    for count in range(1, lines + 1):
        print(character * count)

print_triangle(character="@", lines=2)
print_triangle(character="&", lines=13)
print_triangle(character="o", lines=5)


def print_square(n):

    # 1. For each row in the square print a line of n characters
    # 2. for each column in the square print a character
    # the square should be n characters wide and n characters tall
    for row in range(n):
        for column in range(n):
            print("*", end="")
        print()  # Move to the next line after printing each row  
    
print_square(8)
