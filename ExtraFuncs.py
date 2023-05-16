

def select_deck():
    print("Current Decks:")
    for i in range(len(library)):
        print("{}: {}".format((i + 1), library[i].name))
    selection = int(input("Enter corresponding deck number or zero to exit: "))
    while selection < 0 or selection > len(library):
        print("Current Decks:")
        for i in range(len(library)):
            print("{}: {}".format((i + 1), library[i].name))
        selection = int(input("Enter corresponding deck number or zero to exit: "))
    if selection == 0:
        exit(1)
    deck_pick = library[selection - 1]
    return deck_pick


def create_deck():
    end = False
    new_deck = Deck()
    deck_name = input("Enter new deck name: ")
    new_deck.name = deck_name
    print("To stop adding cards, type 0 in the card's first field")
    print()
    while not end:
        chinese = input("Enter character(s) or '0' to end: ")
        if chinese == '0':
            end = True
        else:
            english = input("Enter english definition: ")
            pinyin = input("Enter pinyin: ")
            new_deck.add_card(english, chinese, pinyin)
    library.append(new_deck)