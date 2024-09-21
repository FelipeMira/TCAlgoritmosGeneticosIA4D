class NoSuchElementException(Exception):
    def __init__(self, message="A população está vazia."):
        self.message = message
        super().__init__(self.message)