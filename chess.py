import pygame as pg
from math import *

pg.init()
win = pg.display.set_mode((600, 600))
pg.display.set_caption('Chess 2')
clock = pg.time.Clock()


wKing_surf = pg.transform.rotozoom(pg.image.load('pieces/king.png').convert_alpha(), 0, 0.75)
wQueen_surf = pg.transform.rotozoom(pg.image.load('pieces/queen.png').convert_alpha(), 0, 0.70)
wRook_surf = pg.transform.rotozoom(pg.image.load('pieces/rook.png').convert_alpha(), 0, 0.70)
wBishop_surf = pg.transform.rotozoom(pg.image.load('pieces/bishop.png').convert_alpha(), 0, 0.70)
wKnight_surf = pg.transform.rotozoom(pg.image.load('pieces/knight.png').convert_alpha(), 0, 0.70)
wPawn_surf = pg.transform.rotozoom(pg.image.load('pieces/pawn.png').convert_alpha(), 0, 0.70)

chessBoard = [
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    6,6.1,6.2,6.3,6.4,6.5,6.6,6.7,
    3,5,4,2,1,4.1,5.1,3.1
]

class Piece:
    def __init__(self, x, y, type, value, sprite):
        self.x = x
        self.y = y
        self.type = type
        self.value = value
        self.sprite = sprite
        self.rect = self.sprite.get_rect(center = (self.x + 75/2, self.y + 75/2))

    def update(self):
        win.blit(self.sprite, self.rect)


def drawBoard(color1, color2):
    for u in range(8):
        for k in range(0, 8, 2):
            if u % 2 == 0:
                pg.draw.rect(win, color1, (75*k, 75*u, 75, 75), width=0)
            else:
                pg.draw.rect(win, color1, (75*(k+1), 75*u, 75, 75), width=0)
    
        for h in range(1, 9, 2):
            if u % 2 == 0:
                pg.draw.rect(win, color2, (75*h, 75*u, 75, 75), width=0)
            else:
                pg.draw.rect(win, color2, (75*(h-1), 75*u, 75, 75), width=0)


    for i in range(1, 8):
        pg.draw.line(win, (0,0,0), (75*i, 0), (75*i, 600), width=3)
    
    for j in range(1, 8):
        pg.draw.line(win, (0,0,0), (0, 75*j), (600, 75*j), width=3)

kings, queens, rooks, bishops, knights, pawns = [],[],[],[],[],[]

selected_piece = None

def drawPieces():

    def boardSearch(value):
        tempL = []
        value = int(value)
        for p in chessBoard:
            if p != 0:
                if  floor(p) == value:
                    tempL.append(int(chessBoard.index(p)))
        return(tempL)

    # KING
    for i in boardSearch(1):
        wKing = Piece((i % 8)*75, (i // 8)*75,'king', 0, wKing_surf)
        kings.append(wKing)
    
    for king in kings:
        king.update()

    # PAWN
    for i in boardSearch(2):
        wQueen = Piece((i % 8)*75, (i // 8)*75,'Queen', 0, wQueen_surf)
        queens.append([wQueen.sprite.get_rect(center = (wQueen.x + 75/2, wQueen.y + 75/2)), (chessBoard[(wQueen.x//75)+(wQueen.y//75)*8])])

    for Queen in queens:
        win.blit(wQueen_surf, Queen[0])
    
    # ROOK
    for i in boardSearch(3):
        wRook = Piece((i % 8)*75, (i // 8)*75,'Rook', 0, wRook_surf)
        rooks.append([wRook.sprite.get_rect(center = (wRook.x + 75/2, wRook.y + 75/2)), (chessBoard[(wRook.x//75)+(wRook.y//75)*8])])

    for rook in rooks:
        win.blit(wRook_surf, rook[0])

    # BISHOP
    for i in boardSearch(4):
        wBishop = Piece((i % 8)*75, (i // 8)*75,'bishop', 0, wBishop_surf)
        bishops.append([wBishop.sprite.get_rect(center = (wBishop.x + 75/2, wBishop.y + 75/2)), (chessBoard[(wBishop.x//75)+(wBishop.y//75)*8])])

    for bishop in bishops:
        win.blit(wBishop_surf, bishop[0])

    # KNIGHT
    for i in boardSearch(5):
        wKnight = Piece((i % 8)*75, (i // 8)*75,'knight', 0, wKnight_surf)
        knights.append([wKnight.sprite.get_rect(center = (wKnight.x + 75/2, wKnight.y + 75/2)), (chessBoard[(wKnight.x//75)+(wKnight.y//75)*8])])

    for knight in knights:
        win.blit(wKnight_surf, knight[0])

    # PAWN
    for i in boardSearch(6):
        wPawn = Piece((i % 8)*75, (i // 8)*75,'pawn', 0, wPawn_surf)
        pawns.append([wPawn.sprite.get_rect(center = (wPawn.x + 75/2, wPawn.y + 75/2)), (chessBoard[(wPawn.x//75)+(wPawn.y//75)*8])])

    for pawn in pawns:
        win.blit(wPawn_surf, pawn[0])


while True:
    win.fill((0,0,0))
    mx, my = pg.mouse.get_pos()
    mx, my = mx//75, my//75
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.MOUSEBUTTONUP and selected_piece == None:
            if chessBoard[mx+my*8] != 0:
                selected_piece = chessBoard[mx+my*8]
                old_piece = selected_piece

        elif event.type == pg.MOUSEBUTTONUP and selected_piece != None:
            print(queens)
            
            if floor(selected_piece) == 6:
                for p in pawns:
                    if p[1] == selected_piece:
                        pawns.pop(pawns.index(p))

            elif floor(selected_piece) == 5:
                for p in knights:
                    if p[1] == selected_piece:
                        knights.pop(knights.index(p))

            elif floor(selected_piece) == 4:
                for p in bishops:
                    if p[1] == selected_piece:
                        bishops.pop(bishops.index(p))

            elif floor(selected_piece) == 3:
                for p in rooks:
                    if p[1] == selected_piece:
                        rooks.pop(rooks.index(p))

            elif floor(selected_piece) == 2:
                for p in queens:
                    if p[1] == selected_piece:
                        queens.pop(queens.index(p))

            chessBoard[chessBoard.index(old_piece)] = 0
            chessBoard[mx+my*8] = selected_piece

            selected_piece = None
            old_piece = None




    drawBoard((240, 147, 43), (246, 229, 141))
    drawPieces()





    pg.display.update()
    clock.tick(60)
