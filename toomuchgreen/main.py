__author__ = 'root'

import cv2 as cv
import numpy
import math

# Tile size : 16x16
tile_size = 16

channels = {
    'r': 0,
    'g': 1,
    'b': 2
}


def analyze_tile(img, row=0, column=0, tile_size=16):
    '''

    :param numpy.ndarray img:
    :return:
    '''

    # y - height
    # x - width

    start_x = tile_size * column
    start_y = tile_size * row

    end_x = start_x + tile_size
    end_y = start_y + tile_size

    area = img[start_y:end_y, start_x:end_x]

    channel = channels['g']
    counts = {}

    for x in xrange(tile_size):
        row = area[x]
        for y in xrange(tile_size):
            px = row[y][channel]

            if px in counts:
                counts[px] += 1
            else:
                counts[px] = 1

    return counts


def analyze_tiles(img, tile_size):
    width = img.shape[1]
    height = img.shape[0]

    rows = int(math.ceil(height/tile_size))
    tiles_in_row = int(math.ceil(width/tile_size))

    counts = {}
    for i in xrange(rows):
        for j in xrange(tiles_in_row):
            key = '{}_{}'.format(i, j)
            counts[key] = analyze_tile(img, i, j, tile_size)

    return counts


if __name__ == '__main__':
    filename = 'toomuchgreen.png'
    file_obj = cv.imread(filename)

    counts = analyze_tiles(file_obj, tile_size)
    c = 0
    for count in counts:
        if len(count) > 1:
            print '{} -> {}'.format(count, len(count))
            c += 1

    print c/8

    pass