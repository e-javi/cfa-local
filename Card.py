class Card(object):
    def __init__(self, english, chinese, pinyin):
        self.english = english
        self.chinese = chinese
        self.pinyin = pinyin

    def print_back(self):
        print(self.pinyin)
        print(self.english)

    def print_front(self):
        print(self.chinese)

    def print_info(self):
        print(self.chinese)
        print(self.english)
        print(self.pinyin)
