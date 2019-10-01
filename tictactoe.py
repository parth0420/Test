

X='X'
O='O'
Empty=''
choices= []
playerone = True
winner = False

for i in range(1,10):
    choices.append(i)

def drawBoard() :
        print(f'\n\t{choices[0]} | {choices[1]} | {choices[2]} ')        
        print('\t----------')
        print(f'\n\t{choices[3]} | {choices[4]} | {choices[5]} ')
        print('\t----------')
        print(f'\n\t{choices[6]} | {choices[7]} | {choices[8]} ')
        
def Winner():
    winner=False
    WinCond= ((0,1,2),(3,4,5),(6,7,8),
              (0,3,6),(1,4,7),(2,5,8),
              (0,4,8),(2,4,6))
    for row in WinCond:
        if(choices[row[0]]==choices[row[1]]==choices[row[2]]):
            winner=True
            drawBoard()

    return winner


while not winner:
    
    drawBoard()
    if playerone:
        print('Player ONE Turn ')
    else:
        print('Player TWO Turn ')
    try:   
        choice=int(input('>'))
    except:
        print('Enter Valid Number')
        continue
    try:
        if(choices[choice-1] == X or choices[choice-1] == O or choice > 10 or choice < 1):
            print("Illegal Move,Try Again !")
            continue
    except:
        continue
    else:    
        if playerone:
            choices[choice-1] = X
        else: 
            choices[choice-1] = O

        playerone = not playerone

        winner = Winner()
        # for i in range(1,10):
        #     if i not in choices:
        #         print('TIE')1
        #         break



print(f'Player {playerone+1} WINS !!')

        
    