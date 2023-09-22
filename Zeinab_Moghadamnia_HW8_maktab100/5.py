class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        '''increase space'''
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        '''decrease space'''
        self.level -= 1

    def print(self, text):
        indentation = "    " * self.level
        print(f"{indentation}{text}")

with Indenter() as indent:
    indent.print("Hi")
    with indent:
        indent.print("Talk is Cheap!")
        with indent:
            indent.print("Show me the Code...")
    indent.print("Torvalds")
