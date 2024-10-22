from corpus import Corpus

class BaseFilter:
    def __init__(self):
        self.SPAM = True
        self.OK = False

    def filter_function(self, mail):
        pass

    def filter_list(self, data):
        res = {}
        for item in data:
            res[item] = self.filter_function(item)
        return res

    def train(self, dir):
        """ Vytvoření a nastavení vnitřních datových struktur třídy, aby byly později využitelné metodou test(). """
        with open(dir+"/!truth", 'r') as f:
            pass

    def test(self, dir):
        """Vytvoří v zadaném adresáři soubor !prediction.txt"""
        with open(dir+"/!prediction.txt", 'w') as f:
            corpus = Corpus(dir)
            for filename, body in corpus.emails():
                f.write(f"{filename} {"SPAM" if self.filter_function(body) else "OK"}\n")

