from src.pieces import *

def notation_to_piece(notation:str):
    return {'P':Pawn, 'K':King, 'R':Rook, 'B':Bishop, 'N':Knight, 'S':Silver, 'G':Gold, 'L':Lance}[notation]

