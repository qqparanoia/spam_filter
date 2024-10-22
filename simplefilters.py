from basefilter import BaseFilter
import random

class NaiveFilter(BaseFilter):
    def __init__(self):
        super().__init__()

    def filter_function(self, element):
        return self.OK

class ParanoidFilter(BaseFilter):
    def __init__(self):
        super().__init__()

    def filter_function(self, element):
        return self.SPAM

class RandomFilter(BaseFilter):
    def __init__(self):
        super().__init__()

    def filter_function(self, element):
        return random.choice([self.SPAM, self.OK])

if __name__ == '__main__':
    pass
