# 3. Areas of Rectangles
# The area of a rectangle is the rectangle’s length times its width. 
# Write a program that asks for the length and width of two rectangles. 
# The program should tell the user which rectangle has the greater area, or if the areas are the same.

x = 0 
while x < 1:
    length_1 = float(input("Length for rectangle 1:  "))
    length_2 = float(input("Length for rectangle 2:  "))
    width_1 = float(input("Width for rectangle 1:  "))
    width_2 = float(input("Width for rectangle 2:  "))
    Area_1 = length_1*width_1
    Area_2 = length_2*width_2
    if Area_1 > Area_2:
        print("rectangle 1 has the greater area")
    elif Area_1 < Area_2:
        print("rectangle 2 has the greater area")
    elif Area_1 == Area_2:
        print("rectangle 1 and rectangle 2 have the same area")
    else:
        print("error! please retry it")