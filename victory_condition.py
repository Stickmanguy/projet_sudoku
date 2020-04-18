def victory(tableau):
    x=0
    y=0
    for x in range(9):
        for y in range(9):
            if tableau [y][x]==0:
                return False
            else:
                return True