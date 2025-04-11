# Custom Exceptions

class FormatError(Exception):
    def __init__(self):
        Exception.__init__(self)
        self.msg = "Format Error : "