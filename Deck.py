from Card import Card
import random


class Deck(object):
    def __init__(self):
        self.stack = list()
        self.num = -1
        self.front = True
        self.name = 'Init Deck'

    def ret_chinese(self):
        return self.stack[self.num].chinese

    def ret_english(self):
        return self.stack[self.num].english

    def ret_pinyin(self):
        return self.stack[self.num].pinyin

    def add_card(self, english, chinese, pinyin):
        self.stack.append(Card(english, chinese, pinyin))

    def next_card(self):
        self.num += 1
        if self.num >= len(self.stack):
            self.num = 0
        curr = self.stack[self.num]
        if self.front:
            return curr.chinese
        else:
            return curr.english, curr.pinyin

    def flip_card(self):
        if self.front:
            self.front = False
            curr = self.stack[self.num]
            return curr.english, curr.pinyin
        else:
            self.front = True
            curr = self.stack[self.num]
            return curr.chinese, ''

    def remove_card(self, chinese):
        for i in self.stack:
            if i.chinese == chinese:
                self.stack.remove(i)
        self.num -= 1

    def shuffle(self):
        random.shuffle(self.stack)
        self.num = -1
        self.front = True

    def rename(self, new_name):
        self.name = new_name
