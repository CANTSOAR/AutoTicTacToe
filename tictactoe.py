spots = [" " for x in range(9)]

def print_grid():

    print(" " + spots[0] + " | " + spots[1] + " | " + spots[2])
    print("-----------")
    print(" " + spots[3] + " | " + spots[4] + " | " + spots[5])
    print("-----------")
    print(" " + spots[6] + " | " + spots[7] + " | " + spots[8])


for x in range(9):

    spot = input("enter x or o and box#:")
    spots[int(spot[-1]) - 1] = spot[0]
    print_grid()