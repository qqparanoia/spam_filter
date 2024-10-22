import os

class Corpus():
    def __init__(self, directory: str):
        self.directry = directory

    def emails(self):
        for file_name in os.listdir(self.directry):
            if file_name.startswith('!'):
                continue

            filepath = os.path.join(self.directry, file_name)

            if os.path.isfile(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    body = f.read()
                yield file_name, body




