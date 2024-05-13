class Piece:
    def __init__(self, row:int, column:int, color:str):
        self.row = row
        self.column = column
        self.color = color
        self.moves = []

    def move(self, row, column):
        self.row = row
        self.column = column

