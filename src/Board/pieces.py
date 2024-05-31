import pygame

class Piece:
    def __init__(self, row:int, column:int, player:int, notation:str, image:pygame.Surface):
        self.row = row
        self.column = column
        self.player = player
        self.notation = notation
        self.moves = []
        self.promoted = False
        self.promotion_declined = False
        self.image = image

    def move(self, row, column):
        self.row = row
        self.column = column

    def get_moves(self, row, column, board):
        raise NotImplementedError
     

class Pawn(Piece):
    def __init__(self, row, column, player, image):
        super().__init__(row, column, player, 'P', image)

    def get_moves(self, row, column, board):
        self.moves = []
        if not self.promoted :
            if 0 <= row + self.player < board.size:
                if not board.get_piece(row + self.player, column) or board.get_piece(row + self.player, column).player != self.player:
                    self.moves.append((row + self.player, column))
        else :
            Gold.get_moves(self, row, column, board)
        return self.moves
            

class Bishop(Piece):
    def __init__(self, row, column, player, image):
        super().__init__(row, column, player, 'B', image)

    def get_moves(self, row, column, board):
        self.moves = []
        for dx in (1, -1):
            for dy in (1, -1):
                for i in range(1, board.size):
                    if 0 <= row + i*dy < board.size and 0 <= column + i*dx < board.size :
                        if not board.get_piece(row+i*dy, column+i*dx):
                            self.moves.append((row+i*dy, column+i*dx))
                        elif board.get_piece(row+i*dy, column+i*dx).player != self.player:
                            self.moves.append((row+i*dy, column+i*dx))
                            break
                        else :
                            break
                    else :
                        break
        if self.promoted:
            for dx, dy in zip((1, -1, 0, 0), (0, 0, 1, -1)):
                if 0 <= row + dy < board.size and 0 <= column + dx < board.size :
                    self.moves.append((row+dy, column+dx))
        return self.moves



class Rook(Piece):
    def __init__(self, row, column, player, image):
        super().__init__(row, column, player, 'R', image)

    def get_moves(self, row, column, board):
        self.moves = []
        for dx, dy  in zip((1, -1, 0, 0), (0, 0, 1, -1)):
            for i in range(1, board.size):
                if 0 <= row + i*dy < board.size and 0 <= column + i*dx < board.size :
                    if not board.get_piece(row+i*dy, column+i*dx):
                        self.moves.append((row+i*dy, column+i*dx))
                    elif board.get_piece(row+i*dy, column+i*dx).player != self.player:
                        self.moves.append((row+i*dy, column+i*dx))
                        break
                    else :
                        break
                else :
                    break
        if self.promoted:
            for dx in (-1, 1):
                for dy in (-1, 1):
                    if 0 <= row + dy < board.size and 0 <= column + dx < board.size :
                        self.moves.append((row+dy, column+dx))
        return self.moves

class Knight(Piece):
    def __init__(self, row, column, player, image):
        super().__init__(row, column, player, 'N', image)

    def get_moves(self, row, column, board):
        self.moves = []
        if not self.promoted :
            for dx in (-1, 1):
                if 0 <= row + self.player * 2 < board.size and  0 <= column + dx < board.size :
                    if not board.get_piece(row+self.player*2, column+dx) or board.get_piece(row+self.player*2, column+dx).player != self.player :
                        self.moves.append((row+self.player*2, column+dx))
        else :
            Gold.get_moves(self, row, column, board)
        return self.moves

class Gold(Piece):
        def __init__(self, row, column, player, image):
            super().__init__(row, column, player, 'G', image)

        def get_moves(self, row, column, board):
            self.moves = []
            for dx, dy in zip((-1, -1, 0, 1, 1, 0), (0, self.player, self.player, self.player, 0, -self.player)):
                if 0 <= row + dy < board.size and 0 <= column + dx < board.size :
                    if not board.get_piece(row+dy, column+dx) or board.get_piece(row+dy, column+dx).player != self.player :
                        self.moves.append((row+dy, column+dx))
            return self.moves


class Silver(Piece):
    def __init__(self, row, column, player, image):
        super().__init__(row, column, player, 'S', image)

    def get_moves(self, row, column, board):
            self.moves = []
            if not self.promoted :
                for dx, dy in zip((-1, -1, 1, 1, 0), (1, -1, 1, -1, self.player)):
                    if 0 <= row + dy < board.size and 0 <= column + dx < board.size :
                        if not board.get_piece(row+dy, column+dx) or board.get_piece(row+dy, column+dx).player != self.player :
                            self.moves.append((row+dy, column+dx))
            else :
                Gold.get_moves(self, row, column, board)
            return self.moves

class Lance(Piece):
    def __init__(self, row, column, player, image):
        super().__init__(row, column, player, 'L', image)

    def get_moves(self, row, column, board):
        self.moves = []
        if not self.promoted :
            for i in range(1, board.size):
                if 0 <= row + i*self.player < board.size :
                    if not board.get_piece(row+i*self.player, column) :
                        self.moves.append((row+i*self.player, column))
                    elif board.get_piece(row+i*self.player, column).player != self.player :
                        self.moves.append((row+i*self.player, column))
                        break
                    else :
                        break
                else :
                    break
        else :
            Gold.get_moves(self, row, column, board)
        return self.moves
            
                                    
class King(Piece):
    def __init__(self, row, column, player, image):
        super().__init__(row, column, player, 'K', image)

    def get_moves(self, row, column, board):
        self.moves = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= row + i < board.size and 0 <= column+j < board.size :
                    if not board.get_piece(row+i, column+j) or board.get_piece(row+i, column+j).player != self.player :
                        self.moves.append((row+i, column+j))
        return self.moves























