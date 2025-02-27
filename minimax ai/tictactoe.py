import pygame
import sys
from copy import deepcopy
pygame.init()
#! Game variables
# Screen dimensions
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
BOARD_ROWS, BOARD_COLS = 3, 3
SECTION_WIDTH = WIDTH/BOARD_ROWS
# Colors
WHITE = (238, 238, 238)
BLACK = (0, 0, 0)
RED = (241, 84, 18)
BLUE = (52, 179, 241)
LINE_COL= (24, 116, 152)
# Win direction
verticle = [[(x,y) for y in list(range(3))]for x in range(3)]
horizontal = [[(x,y) for x in list(range(3))]for y in range(3)]

# Diagonal win direction
diagonal = list()
for x in list(range(3)):
	for y in list(range(3)):
    	 if abs(x-y) !=1:
         	diagonal.append((x,y))
diagonal=[[diagonal[x] for x in list(range(0,5,2))],[diagonal[x] for x in list(range(1,4))]]
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe AI...')

# Initialize the board
BOARD = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Draw the board lines
def draw_lines():
    screen.fill(WHITE)
    # Horizontal lines
    pygame.draw.line(screen, BLACK, (0, 100), (300, 100), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, 200), (300, 200), LINE_WIDTH)
    # Vertical lines
    pygame.draw.line(screen, BLACK, (100, 0), (100, 300), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (200, 0), (200, 300), LINE_WIDTH)

# Draw X's and O's
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if BOARD[row][col] == 'X':
                pygame.draw.line(screen, BLUE, (col * 100 + 15, row * 100 + 15), (col * 100 + 85, row * 100 + 85), 15)
                pygame.draw.line(screen, BLUE, (col * 100 + 85, row * 100 + 15), (col * 100 + 15, row * 100 + 85), 15)
            elif BOARD[row][col] == 'O':
                pygame.draw.circle(screen, RED, (int(col * 100 + 50), int(row * 100 + 50)), 38, 15)
#display the winning line
def winning_line(row):
    pygame.draw.line(screen, LINE_COL,
                    start_pos=((row[0][1]*(SECTION_WIDTH))+SECTION_WIDTH/2,(row[0][0]*(SECTION_WIDTH))+SECTION_WIDTH/2),
                    end_pos=((row[-1][1]*(SECTION_WIDTH))+SECTION_WIDTH/2,(row[-1][0]*(SECTION_WIDTH))+SECTION_WIDTH/2),width=20)
# Display the win screen
def display_winner(winner,row):
    font = pygame.font.Font(None, 50)
    text = font.render(f'Player {winner} wins!', True,RED if winner == 'O'else BLUE)
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
    # winning_line(row)
    print(((row[0][1]*(SECTION_WIDTH))+SECTION_WIDTH/2,(row[0][0]*(SECTION_WIDTH))+WIDTH/6))
    print(((row[-1][1]*(SECTION_WIDTH))+SECTION_WIDTH/2,(row[-1][0]*(SECTION_WIDTH))+WIDTH/6))
    winning_line(row)
    pygame.display.update()
    pygame.time.delay(500)
    screen.fill(WHITE)
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.delay(900)
    screen.fill(WHITE)
    draw_lines()
# displaying draw
def display_draw(winner,row):
    font = pygame.font.Font(None, 50)
    text = font.render(f'Draw', True,  (66,66,80))
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
    pygame.display.update()
    pygame.time.delay(500)
    screen.fill(WHITE)
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.delay(900)
    screen.fill(WHITE)
    draw_lines()
# Check for a winner
def check_winner(board):
    #verticle check
    for check_item in [verticle,horizontal,diagonal]:
        for row in check_item:
            if board[row[0][0]][row[0][1]] == board[row[1][0]][row[1][1]]== board[row[2][0]][row[2][1]] !=0:
               
                return True,row
    return False,None
           
# Check for Draw
def check_draw(board):
    for i in board:
        if 0 in i:
            return False
    return True
#!-----------------------------------------AI PART------------------------------------------------------
def evaluation(board):
    if check_winner(board)[0]:
        if board[check_winner(board)[1][0][0]][check_winner(board)[1][0][1]] == 'O':
            print('won',end='')
            return 1
        else:
            return -1
    
    return 0
     
    
          
                   
def minmax(board,player,depth):
    if depth == 0 or check_winner(board)[0]:
        print('-',end='')
        return evaluation(board), board
    if player == 'O': #max player
        print('.',end='')
        Obest_score = -100
        best_move = None
        for move in get_moves(board):
            fake_board = try_move(move, player,  deepcopy(board))
            Oscore:int = minmax(fake_board, 'X', depth-1)[0]
            Obest_score = max(Obest_score,Oscore)
            if Oscore == Obest_score:
                best_move = move
        return Obest_score,best_move
    if player == 'X': #min player
        print('.',end='')
        Xworst_score = 100
        worst_move = None
        for move in get_moves(board):
            fake_board = try_move(move, player,  deepcopy(board))
            Xscore:int = minmax(fake_board, 'O', depth-1)[0]
            Xworst_score = min(Xworst_score, Xscore)
            if Xscore == Xworst_score:
                best_move = move
        return Xworst_score,worst_move

def try_move(move,player,board):
    board[move[0]][move[1]] = player
    return board
def get_moves(board):
    moves = []
    for row in list(range(3)):
        for col in list(range(3)):
            if board[row][col] == 0:
                moves.append((row,col))
    return moves
#!------------------------------------------------------------------------------------------------------
draw_lines()
pygame.display.update()
# Main loop
running = True
player = 'X'
while running:
    is_won,which_row = check_winner(BOARD)
    if is_won:
        display_winner('X' if player == 'O' else 'O',which_row)
        BOARD = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
        player = 'X'
    if check_draw(BOARD):
        display_draw('X' if player == 'O' else 'O',which_row)
        BOARD = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
        player = 'X'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and player == 'X':

            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y
            # Determine which
            clicked_row = int(mouseY // 100)
            clicked_col = int(mouseX // 100)
            if BOARD[clicked_row][clicked_col]== 0:
                BOARD[clicked_row][clicked_col] = player
                player = 'O'
        elif player == 'O':
                value,move = minmax(deepcopy(BOARD), player, 6)
                BOARD[move[0]][move[1]] = player
                player = 'X'
                print(f'AI played at {move}, score: {value}')
            

    draw_figures()
    pygame.display.update()

pygame.quit()
sys.exit()