import configparser

class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.cfg')
        self.width = self.config.getint('GENERAL', 'width')
        self.height = self.config.getint('GENERAL', 'height')
        self.tile_size = self.width//10
        self.margin = self.tile_size//2
        self.fps = self.config.getint('GENERAL', 'fps')
        self.piece_asset = self.config.get('ASSETS', 'piece')


    def save(self):
        pass