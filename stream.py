class StringStream:
    def __init__(self, text: list[str]) -> None:
        self.text = text
        self.iter = self.__iterator()
    
    def __next__(self):
        return next(self.iter)

    def __iterator(self):
        for line in self.text:
            yield line
        yield None
