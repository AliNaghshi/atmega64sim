class Error(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code

class NotAccessedRegion(Error):
    def __init__(self):
        super().__init__("Invalid region of memory", 105)


class UnallowedRegister(Error):
    def __init__(self):
        super().__init__("Please use valid registers", 194)

class InvalidBoundary(Error):
    def __init__(self):
        super().__init__("Invalid range of memory used", 127)

class ZeroDevision(Error):
    def __init__(self):
        super().__init__("Dev by Zero",100)

class LabelNotFound(Error):
    def __init__(self):
        super().__init__("Label nit found", 105)


class InvalidImmideate(Error):
    def __init__(self):
        super().__init__("invalide immidiate", 105)



