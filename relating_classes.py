class Writer:
    def __init__(self, name):
        self.name = name
        self._tool = None

    @property
    def tool(self):
        return self._tool

    @tool.setter
    def tool(self, tool):
        self._tool = tool

class WritingTool:
    def __init__(self, name):
        self.name = name

    def write(self):
        return 'Writing...'

writer = Writer('Levi')
pen = WritingTool('Bic')
typewriter = WritingTool('Typewriter')
writer.tool = typewriter

print(pen.write())
print(typewriter.write())
