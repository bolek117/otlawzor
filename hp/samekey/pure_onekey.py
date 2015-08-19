from utils import *

__author__ = 'bolek117'

key_size = 9

if __name__ == '__main__':
    decoded = b64decode()

    # Determine maximum number of characters
    max_count = 0
    for sentence in decoded:
        actual_len = len(sentence)

        if actual_len > max_count:
            max_count = actual_len

    # Make array with characters on given positions modulo key size
    characters_on_positions = [[] for i in xrange(key_size)]
    for sentence in decoded:
        for i in xrange(len(sentence)):
            characters_on_positions[i % key_size].append(sentence[i])

    i = 0
    solution = []
    for package in characters_on_positions:
        expected_score = 0
        possible_keys = []

        while len(possible_keys) == 0:
            possible_keys = brute_key(package, expected_score)
            expected_score += 1

        for key in possible_keys:
            print 'Positions', i, ':', key
            solution.append(key)

        i += 1

    for sentence in decoded:
        print do_xor(sentence, solution).strip('X')
