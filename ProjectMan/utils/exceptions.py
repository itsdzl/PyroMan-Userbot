class dzerror(Exception):
    def __init__(self, errr: str):
        super().__init__(errr)
