# TODO:
# Make a named tuple out of cards

from random import shuffle

class Player(object):
  def __init__(self, name, cards):
    self.name = str(name)
    self.cards = cards

  def pretty(self, card):
    card_color, card_value = card
    return card_color.capitalize() + " " + str(card_value).capitalize()

  def print_cards(self):
    print self.name + ":"
    self.cards.sort()
    for i, c in enumerate(self.cards):
      print "[" + str(i) + "]", self.pretty(c)
    print

  def remaining_cards(self):
    return len(self.cards)

  def find_card(patterns):
    # for p in patterns:
    return

  def play_card(self):
    """ Let's see what we do next... """
    print Game.played_cards[0]
    card_color, card_value = Game.played_cards[0]
    # React on...
    # Skip
    if card_value == "skip":
      # Next player reacts on card below skip
      Game.played_cards[0] = Game.played_cards[1]
      return

    # Special card
    total_cards_draw = 0
    while card_value == "+4" or card_value == "+2":
      total_cards_draw += card_value[1]

    if total_cards_draw > 0:
      matching_card = self.find_card(["+2", "+4"])
      if matching_card:
        return matching_card
      else:
        self.cards.append(Game.deal(total_cards_draw))

    # Find card with matching color
    matching_card = self.find_card([card_color])
    if matching_card:
      return matching_card
    # Find card with matching value
    matching_card = self.find_card([card_value])
    if matching_card:
      return matching_card
    # Deal special
    matching_card = self.find_card(["+2", "+4"])
    if matching_card:
      return matching_card
    else:
      # Can't do anything but draw a card
      self.cards.append(Game.deal(1))


###################

class Game(object):
  stack = self.stack()
  played_cards = []

  def __init__(self, num_players = 2):
    shuffle(Game.stack)
    self.players = [Player(p, self.deal()) for p in range(num_players)]
    # Deal first card
    Game.played_cards.append(self.deal(1))

  def stack(self):
    # Four different colors
    colors = ["y", "r", "g", "b"]
    # 2 * 10 * 4 = 80 number cards from 0 to 9
    number_cards = 2 * [(c, str(n)) for c in colors for n in range(0,10)]
    # 2 * 3 * 4 = 24 action cards in four colors
    actions = ["+2", "reverse", "skip"]
    action_cards = 2 * [(c, a) for c in colors for a in actions]
    # 2 * 4 = 8 black cards - an empty color string stands for black
    black_cards = 4 * [(" ", "color select"), (" ", "+4")]
    # 4 + 72 + 24 + 8 = 108 cards total
    stack = zero_cards + number_cards + action_cards + black_cards
    return stack
    def deal(self, n = 7):
      """ Get n cards from top of deck """
      hand, Game.stack = Game.stack[:n], Game.stack[n:]
      return hand

  def play(self):
    # Play as long as there are remaining players
    while self.players:
      self.play_round()

  def play_round(self):
    print self.played_cards[0]
    for p in self.players:
      p.print_cards()
      p.play_card()
      if p.remaining_cards() == 0:
        print "FINISHED"
        self.players.remove(p)
      # if self.current_card REVERSE -> reverse(players)

def main():
  game = Uno()
  game.play()

if __name__ == "__main__":
  main()
