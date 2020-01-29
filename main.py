#def draw teken board
#def p1 en p2: nummer kiezen 
#def choose nummer: regels om nummers te kiezen
#def check board: steeds controlleren of de speler heeft gekozen of het spel gelijk is. 
#def while not: spel gaat door tot winnen of het gelijkspel
#if input: wanneer de spel beëindigd, gaat spel door of niet

def tic_tac_toe():
    print ('Boter Kaas & Eieren')
    print ('Speler 1 begint met spelen, kiest een nummer tussen 1 en 9.')
    print ()
    board = [[1], [2], [3], [4], [5], [6], [7], [8], [9]]
    end = False
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

#def draw: het teken van het board 
    def draw():
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])
        print()

#def choose number: testen op goede nummer 
#speler mogen niet de nummers kiezen die al gekozen zijn.
    def choose_number():
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nDat mag niet, kies een ander getal")
                        continue
                except ValueError:
                   print("\nDat mag niet, kies een ander getal")
                   continue

#def p1: een nummer kiezen vanuit board 
    def p1():
        n = choose_number()
        if board[n] == "[X]" or board[n] == "[O]":
            print("\nDat mag niet, kies een ander getal")
            p1()
        else:
            board[n] = "[X]"

#def p2: een nummer kiezen vanuit board 
    def p2():
        n = choose_number()
        if board[n] == "[X]" or board[n] == "[O]":
            print("\nDat mag niet, kies een ander getal")
            p2()
        else:
            board[n] = "[O]"

#def check_board: testen op het board 
#of een speler heeft gewonnen of het spel gelijk is 
    def check_board():
        count = 0
        for a in win_commbinations:
            if board[a[0]] == board[a[1]] == board[a[2]] == "[X]":
                print("Speler 1 heeft gewonnen!\n")
                print("Gefeliciteerd!\n")
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "[O]":
                print("Speler 2 heeft gewonnen!\n")
                print("Gefelictieerd!\n")
                return True
        for a in range(9):
            if board[a] == "[X]" or board[a] == "[O]":
                count += 1
            if count == 9:
                print("Het is gelijkspel\n")
                return True

#while not end: om verder te kunnen spelen 
    while not end:
        draw()
        end = check_board()
        if end == True:
            break
        print("Speler 1 mag kiezen")
        p1()
        draw()
        end = check_board()
        if end == True:
            break
        print("Speler 2 mag kiezen")
        p2()

#if input: 
    if input("Nog een keer? (J/N)\n") == "j":
        print()
        tic_tac_toe()

tic_tac_toe() 