import copy

from Deck import Deck
import csv
import codecs

from PyQt5.QtWidgets import *
from PyQt5 import uic


class GUI(QMainWindow):

    def __init__(self):
        super(GUI, self).__init__()
        uic.loadUi("flashAppv1.ui", self)
        self.show()

        # Init vars
        self.currDeck = copy.deepcopy(library[0])
        self.init_check = True
        self.last_selected = copy.deepcopy(self.currDeck)
        self.flipped = False

        #  Init deck list widget
        for i in library:
            self.deckListWidget.addItem(i.name)

        # Set first card to be displayed
        self.topLabel.setText(self.currDeck.next_card())
        self.bottomLabel.setText('')

        # Widget connect statements for when clicked
        self.deckListWidget.itemClicked.connect(self.selectedDeck)
        self.shuffleButton.clicked.connect(self.shuffled)
        self.restartDeckButton.clicked.connect(self.restart)
        self.nextCardButton.clicked.connect(self.nextCard)
        self.flipButton.clicked.connect(self.flip)
        self.prevCardButton.clicked.connect(self.prevCard)
        self.gotItButton.clicked.connect(self.gotIt)
        self.defFirstBox.toggled.connect(self.reverse)

    def selectedDeck(self, item):
        self.init_check = False
        for i in library:
            if i.name == item.text():
                self.currDeck = copy.deepcopy(i)
                self.currDeck.num = -1
                self.last_selected = copy.deepcopy(self.currDeck)
                self.nextCard()

    def shuffled(self):
        self.currDeck.shuffle()
        self.nextCard()

    def restart(self):
        if self.init_check:
            self.currDeck = copy.deepcopy(library[0])
        else:
            self.currDeck = copy.deepcopy(self.last_selected)
        self.nextCard()

    def nextCard(self):
        if self.flipped:
            self.currDeck.front = False
        else:
            self.currDeck.front = True
        if self.currDeck.front:
            self.topLabel.setText(self.currDeck.next_card())
            self.bottomLabel.setText('')
        else:
            eng, pin = self.currDeck.next_card()
            self.topLabel.setText(eng)
            self.bottomLabel.setText(pin)

    def prevCard(self):
        self.currDeck.num -= 2
        if self.currDeck.num < -1:
            self.currDeck.num = -1
        self.nextCard()

    def flip(self):
        eng, pin = self.currDeck.flip_card()
        self.topLabel.setText(eng)
        self.bottomLabel.setText(pin)

    def reverse(self):
        self.flipped = not self.flipped
        self.currDeck = copy.deepcopy(self.last_selected)
        self.nextCard()

    def gotIt(self):
        if len(self.currDeck.stack) > 1:
            self.currDeck.remove_card(self.currDeck.stack[self.currDeck.num].chinese)
            self.nextCard()
        else:
            self.topLabel.setText("Click Restart")
            self.bottomLabel.setText("or Select New Deck")


library = list()  # list of decks

currentDeck = Deck()
currentDeck.add_card('good', '好', 'hǎo')
currentDeck.add_card('movement; action', '动作', 'dòng zuò')
currentDeck.add_card('public square/plaza', '广场', 'guǎng chuǎng')
currentDeck.add_card('aspect', '方面', 'fāng miàn')
currentDeck.add_card('museum', '博物馆', 'bó wù guǎn')
currentDeck.rename("Test Deck")
library.append(currentDeck)


def read_csv(path, deck_name):  # CSVs must be in correct format: chinese, english, pinyin
    with codecs.open(path, 'r', "utf-8") as csvfile:
        line_reader = csv.reader(csvfile)
        new_deck = Deck()
        new_deck.name = deck_name

        for row in line_reader:
            chinese = row[0]
            english = row[1]
            pinyin = row[2]
            new_deck.add_card(english, chinese, pinyin)
        library.append(new_deck)


def main():
    read_csv('deck3.csv', "CSV Loaded Deck")
    app = QApplication([])
    window = GUI()
    app.exec()


if __name__ == '__main__':
    main()
