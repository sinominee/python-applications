# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

v_column = int(position[0]) #frst
h_row =  int(position[1]) #second
map[h_row - 1][v_column - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")

# hor = int(position[0]) #2
# ver = int(position[1]) #3
# selected_f = map[ver - 1]
# selected_f[hor-1] = "x"
# print(f"{row1}\n{row2}\n{row3}")