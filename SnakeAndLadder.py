import random
import time
import sys


class Game:
    def __init__(self, snakes, ladders, players):
        self.snakes = snakes
        self.ladders = ladders
        self.players = players

    def roll_a_dice(self):
        time.sleep(1)
        dice_value = random.randint(1, 6)
        return dice_value

    def check_ladder(self, position):
        if position in self.ladders:
            time.sleep(1)
            print('\nCongrats ! You climbed up a Ladder')
            new_position = self.ladders[position]
            return new_position
        else:
            return position

    def check_snake(self, position):
        if position in self.snakes:
            time.sleep(1)
            print('\nOh No ! You got a Snake Bite')
            new_position = self.snakes[position]
            return new_position
        else:
            return position

    def check_win(self, player, position):
        if position == 100:
            print('\nConratulations', player, '! You won the game !')
            sys.exit(1)

    def move_calculator(self, n, old_position, dice_value):
        new_position = old_position + dice_value

        if new_position > 100:
            print('\nCannot go beyond 100 , Wait for next turn')

        else:
            new_position = self.check_ladder(new_position)
            new_position = self.check_snake(new_position)

            self.players[n][1] = new_position
            time.sleep(1)
            print('\nMoved from', old_position, 'to', new_position)

            return new_position

    def start_game(self):
        print('\nGAME STARTS !')

        while True:
            for n in range(len(self.players)):
                time.sleep(1)
                name = self.players[n][0]
                old_position = self.players[n][1]

                input('\n' + name + "'s turn : Hit Enter to roll a dice ")
                print('\nRolling dice ...')
                dice_value = self.roll_a_dice()
                print('\n' + name, 'rolled a', dice_value)

                new_position = self.move_calculator(n, old_position,  dice_value)

                self.check_win(name, new_position)


if __name__ == "__main__":

    print('<<Snakes and Ladders>>')
    snakes = {}
    for _ in range(int(input('\nEnter number of snakes : '))):
        head_and_tail = list(map(int, input('Enter head and tail positions of snake  : ').split()))
        snakes[head_and_tail[0]] = head_and_tail[1]

    ladders = {}

    for _ in range(int(input('\nEnter number of ladders : '))):
        start_and_end = list(map(int, input('Enter start and end positions of ladder : ').split()))
        ladders[start_and_end[0]] = start_and_end[1]

    players = []

    for _ in range(int(input('\nEnter number of players : '))):
        player_name = input('Enter name of player : ')
        starting_position = 0
        players.append([player_name, starting_position])

    SnakesAndLadder = Game(snakes, ladders, players)
    SnakesAndLadder.start_game()