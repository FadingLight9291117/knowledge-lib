import time

class Indenter():
    def __init__(self):
        self.level = -1

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, ec_val, exc_tb):
        self.level -= 1

    def print(self, txt):
        print("    " * self.level + txt)


def test_indenter():
    with Indenter() as indent:
        indent.print("Hi!")

        with indent:
            indent.print("Hello")

            with indent:
                indent.print("Body")

        indent.print("Bye")

class Timer:
    def __init__(self):
        self.start = None
        self.end = None

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.interval = self.end - self.start
        print(f"execuation time: {self.interval / 1000}s")


with Timer():
    test_indenter()