# Custom Exceptions

class FormatError(Exception):
    def __init__(self, message):
        Exception.__init__(self,f"Format Error : {message}")
