import re
import numpy as np

class Board:
    def __init__(self):
        BOARD_WIDE=1000
        BOARD_TALL=1000

        #First lines, then columns
        self.board = np.zeros((BOARD_TALL,BOARD_WIDE), dtype=int)


    def parse_line(self, line):
        claim = dict()

        sublist = re.split('#|@|,|:|x',line)
        claim.update({'id':sublist[1]})
        claim.update({'ledge':int(sublist[2])})
        claim.update({'tedge':int(sublist[3])})
        claim.update({'wide':int(sublist[4])})
        claim.update({'tall':int(sublist[5])})

        return claim

    def get_input(self, file):
        self.claims = list()
        with open(file, mode='r') as f:
            for line in f:
                self.claims.append(self.parse_line(line.replace('\n', '')))


    def add_claim_to_board(self, claim):
        for row in range(0, claim["tall"]):
            for column in range (0, claim["wide"]):
                self.board[claim["tedge"] + row][claim["ledge"] + column] += 1


    def process_claims(self):
        for claim in self.claims:
            self.add_claim_to_board(claim)


    def repeated_cells(self):
        counter = 0
        for cell in np.nditer(self.board):
            if cell > 1:
                counter += 1
        return counter

    def get_da_claim(self):
        for claim in self.claims:
            count = 0
            for row in range(0, claim["tall"]):
                for column in range (0, claim["wide"]):
                    count += self.board[claim["tedge"] + row][claim["ledge"] + column]
            if (count == claim['wide'] * claim['tall']):
                return claim['id']

    def print_board(self):
        print(self.board)


mb = Board()
mb.get_input('input.txt')
mb.process_claims()
print(mb.repeated_cells())
print(mb.get_da_claim())
mb.print_board()
