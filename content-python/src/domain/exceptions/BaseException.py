class BaseNotFoundException(Exception):
    def __init__(self, param: str, message: str):
        self.param = param
        self.message = message
