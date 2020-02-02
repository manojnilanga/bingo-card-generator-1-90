from PIL import Image, ImageDraw, ImageFont
import random

if __name__ == '__main__':

    variations = [[[[-1, -1, 0, 0, 0, -1, 0, -1, 0], [0, 0, 0, -1, 0, -1, 0, -1, -1], [-1, -1, 0, 0, -1, 0, 0, 0, -1]], [[0, -1, -1, 0, -1, 0, 0, -1, 0], [-1, 0, -1, 0, -1, 0, 0, -1, 0], [0, 0, -1, -1, 0, 0, -1, -1, 0]], [[-1, 0, 0, -1, -1, 0, -1, 0, 0], [0, 0, 0, -1, 0, 0, -1, -1, -1], [-1, 0, 0, -1, 0, -1, -1, 0, 0]], [[0, -1, -1, 0, 0, -1, -1, 0, 0], [0, 0, 0, -1, 0, -1, 0, -1, -1], [-1, -1, 0, 0, -1, 0, -1, 0, 0]], [[0, 0, -1, -1, 0, -1, -1, 0, 0], [-1, 0, 0, 0, -1, -1, 0, 0, -1], [0, 0, -1, 0, -1, 0, 0, -1, -1]], [[-1, -1, -1, -1, 0, 0, 0, 0, 0], [-1, -1, 0, 0, 0, -1, 0, 0, -1], [0, -1, -1, 0, -1, 0, -1, 0, 0]]], [[[-1, -1, -1, -1, 0, 0, 0, 0, 0], [-1, 0, 0, 0, -1, 0, -1, 0, -1], [0, -1, -1, 0, 0, -1, 0, -1, 0]], [[0, 0, -1, -1, -1, 0, 0, -1, 0], [0, 0, -1, 0, -1, 0, 0, -1, -1], [-1, 0, 0, 0, -1, 0, 0, -1, -1]], [[-1, -1, 0, 0, -1, 0, 0, -1, 0], [0, 0, 0, -1, 0, 0, -1, -1, -1], [0, -1, -1, 0, 0, -1, -1, 0, 0]], [[-1, 0, -1, 0, 0, -1, 0, -1, 0], [0, -1, -1, -1, 0, -1, 0, 0, 0], [0, -1, 0, 0, -1, 0, -1, 0, -1]], [[-1, 0, 0, 0, -1, -1, -1, 0, 0], [-1, 0, 0, 0, -1, -1, -1, 0, 0], [0, -1, 0, -1, 0, 0, 0, -1, -1]], [[-1, 0, 0, -1, 0, -1, -1, 0, 0], [-1, 0, 0, -1, 0, -1, -1, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0, -1]]], [[[-1, -1, 0, 0, 0, -1, 0, 0, -1], [-1, 0, 0, -1, 0, 0, -1, -1, 0], [0, -1, -1, 0, -1, 0, 0, 0, -1]], [[-1, 0, 0, 0, -1, -1, 0, -1, 0], [0, -1, 0, -1, 0, 0, 0, -1, -1], [0, 0, -1, 0, -1, 0, -1, 0, -1]], [[-1, 0, -1, -1, 0, -1, 0, 0, 0], [-1, -1, -1, 0, 0, 0, -1, 0, 0], [0, -1, -1, 0, -1, 0, 0, -1, 0]], [[0, -1, 0, 0, -1, -1, -1, 0, 0], [0, 0, -1, 0, -1, 0, -1, -1, 0], [-1, 0, 0, -1, 0, 0, -1, 0, -1]], [[0, -1, -1, 0, 0, 0, 0, -1, -1], [-1, 0, 0, 0, -1, -1, 0, -1, 0], [0, 0, 0, -1, 0, -1, 0, -1, -1]], [[-1, 0, -1, -1, 0, -1, 0, 0, 0], [-1, -1, 0, -1, 0, 0, -1, 0, 0], [0, 0, 0, -1, -1, -1, -1, 0, 0]]], [[[0, 0, 0, -1, -1, -1, 0, -1, 0], [-1, 0, 0, 0, -1, -1, -1, 0, 0], [-1, -1, 0, -1, 0, 0, 0, 0, -1]], [[0, 0, -1, -1, 0, -1, -1, 0, 0], [0, -1, 0, -1, 0, 0, -1, -1, 0], [0, -1, -1, 0, -1, 0, 0, -1, 0]], [[0, -1, 0, 0, 0, -1, 0, -1, -1], [-1, -1, 0, -1, 0, 0, 0, -1, 0], [-1, 0, 0, 0, -1, -1, -1, 0, 0]], [[-1, 0, -1, 0, 0, -1, -1, 0, 0], [-1, 0, 0, 0, -1, 0, -1, -1, 0], [-1, 0, 0, 0, -1, 0, 0, -1, -1]], [[0, 0, -1, -1, -1, 0, -1, 0, 0], [-1, 0, -1, -1, 0, 0, 0, -1, 0], [0, -1, -1, 0, 0, -1, 0, 0, -1]], [[0, -1, 0, -1, 0, 0, -1, 0, -1], [-1, 0, -1, 0, -1, 0, 0, 0, -1], [0, -1, -1, 0, 0, -1, 0, 0, -1]]], [[[-1, 0, 0, 0, -1, 0, -1, 0, -1], [0, -1, -1, 0, -1, 0, 0, -1, 0], [0, -1, 0, 0, 0, 0, -1, -1, -1]], [[0, 0, 0, 0, -1, -1, -1, -1, 0], [-1, -1, 0, -1, 0, -1, 0, 0, 0], [-1, 0, -1, 0, 0, -1, -1, 0, 0]], [[0, -1, -1, 0, -1, 0, -1, 0, 0], [0, 0, -1, 0, 0, -1, -1, 0, -1], [-1, -1, 0, 0, -1, 0, 0, -1, 0]], [[-1, 0, 0, -1, 0, -1, 0, -1, 0], [0, -1, 0, 0, -1, -1, 0, 0, -1], [-1, -1, -1, -1, 0, 0, 0, 0, 0]], [[0, 0, -1, -1, 0, -1, 0, 0, -1], [0, 0, -1, -1, 0, -1, 0, 0, -1], [-1, 0, 0, -1, -1, 0, 0, -1, 0]], [[-1, 0, 0, 0, -1, 0, 0, -1, -1], [-1, -1, 0, -1, 0, 0, -1, 0, 0], [0, 0, -1, -1, 0, 0, -1, -1, 0]]], [[[0, 0, -1, -1, 0, -1, 0, -1, 0], [-1, -1, -1, 0, 0, 0, -1, 0, 0], [0, 0, 0, 0, -1, -1, 0, -1, -1]], [[-1, 0, -1, 0, -1, 0, 0, 0, -1], [0, 0, -1, -1, -1, 0, -1, 0, 0], [-1, -1, 0, 0, 0, -1, -1, 0, 0]], [[0, 0, 0, -1, -1, -1, 0, 0, -1], [0, 0, -1, -1, 0, -1, 0, 0, -1], [-1, -1, 0, 0, 0, 0, -1, 0, -1]], [[0, -1, 0, -1, 0, 0, -1, 0, -1], [0, -1, 0, -1, 0, 0, -1, -1, 0], [0, 0, 0, 0, -1, -1, 0, -1, -1]], [[-1, 0, -1, 0, 0, -1, 0, -1, 0], [-1, -1, 0, -1, 0, 0, 0, -1, 0], [-1, 0, 0, 0, -1, 0, -1, -1, 0]], [[0, 0, -1, -1, -1, 0, 0, -1, 0], [-1, -1, -1, 0, -1, 0, 0, 0, 0], [-1, -1, 0, 0, 0, -1, -1, 0, 0]]], [[[0, -1, 0, 0, -1, 0, -1, -1, 0], [0, 0, 0, -1, -1, 0, -1, 0, -1], [0, 0, -1, 0, -1, 0, -1, 0, -1]], [[-1, 0, -1, -1, 0, 0, 0, 0, -1], [0, 0, -1, -1, -1, 0, 0, -1, 0], [0, -1, -1, -1, 0, 0, -1, 0, 0]], [[-1, 0, 0, -1, -1, -1, 0, 0, 0], [-1, 0, -1, -1, 0, -1, 0, 0, 0], [0, -1, 0, -1, 0, -1, 0, 0, -1]], [[-1, -1, 0, 0, -1, 0, 0, -1, 0], [0, -1, 0, 0, -1, -1, -1, 0, 0], [-1, -1, 0, 0, 0, -1, 0, -1, 0]], [[-1, 0, 0, 0, 0, 0, -1, -1, -1], [-1, -1, 0, 0, -1, -1, 0, 0, 0], [0, 0, -1, 0, 0, -1, 0, -1, -1]], [[-1, 0, -1, 0, 0, 0, -1, -1, 0], [-1, -1, 0, 0, 0, 0, -1, -1, 0], [0, 0, -1, -1, 0, -1, 0, 0, -1]]], [[[-1, 0, 0, -1, 0, 0, 0, -1, -1], [0, 0, -1, 0, -1, -1, 0, 0, -1], [0, -1, 0, 0, -1, -1, 0, 0, -1]], [[-1, 0, -1, 0, -1, 0, 0, -1, 0], [0, 0, -1, -1, -1, 0, -1, 0, 0], [-1, -1, -1, -1, 0, 0, 0, 0, 0]], [[0, -1, 0, 0, -1, 0, -1, -1, 0], [0, -1, 0, -1, 0, 0, -1, -1, 0], [-1, 0, -1, 0, 0, -1, -1, 0, 0]], [[-1, -1, 0, -1, 0, 0, -1, 0, 0], [-1, -1, 0, 0, 0, -1, 0, 0, -1], [-1, 0, 0, 0, 0, -1, -1, -1, 0]], [[-1, -1, 0, 0, 0, -1, 0, -1, 0], [0, 0, 0, -1, 0, 0, -1, -1, -1], [-1, 0, -1, 0, -1, 0, 0, 0, -1]], [[0, 0, -1, -1, -1, 0, 0, -1, 0], [0, -1, 0, -1, 0, -1, -1, 0, 0], [0, 0, -1, 0, -1, -1, 0, 0, -1]]], [[[-1, 0, -1, 0, -1, 0, 0, -1, 0], [0, 0, -1, -1, -1, 0, -1, 0, 0], [-1, -1, -1, -1, 0, 0, 0, 0, 0]], [[0, -1, 0, 0, 0, -1, -1, 0, -1], [-1, -1, 0, 0, 0, 0, -1, -1, 0], [-1, -1, 0, -1, -1, 0, 0, 0, 0]], [[0, -1, 0, -1, 0, 0, -1, 0, -1], [-1, 0, -1, -1, 0, 0, 0, 0, -1], [0, 0, 0, -1, 0, -1, 0, -1, -1]], [[-1, -1, 0, 0, 0, -1, -1, 0, 0], [0, -1, -1, 0, 0, -1, 0, 0, -1], [-1, 0, -1, 0, 0, -1, 0, -1, 0]], [[0, 0, 0, -1, -1, -1, 0, 0, -1], [0, 0, -1, 0, -1, 0, -1, -1, 0], [0, 0, -1, 0, 0, -1, -1, -1, 0]], [[0, 0, 0, 0, -1, -1, -1, 0, -1], [-1, -1, 0, 0, -1, 0, 0, -1, 0], [-1, 0, 0, -1, -1, 0, 0, -1, 0]]], [[[-1, -1, 0, -1, -1, 0, 0, 0, 0], [-1, 0, -1, 0, -1, -1, 0, 0, 0], [0, 0, -1, -1, 0, -1, 0, 0, -1]], [[-1, 0, 0, 0, -1, 0, -1, -1, 0], [-1, -1, -1, 0, 0, 0, -1, 0, 0], [-1, -1, -1, 0, 0, -1, 0, 0, 0]], [[0, 0, 0, -1, 0, 0, -1, -1, -1], [0, 0, -1, 0, -1, -1, 0, -1, 0], [0, 0, 0, 0, -1, -1, -1, 0, -1]], [[0, 0, -1, -1, 0, 0, 0, -1, -1], [0, -1, -1, -1, 0, -1, 0, 0, 0], [-1, -1, 0, -1, 0, 0, -1, 0, 0]], [[0, -1, 0, 0, -1, -1, -1, 0, 0], [-1, -1, 0, -1, 0, 0, -1, 0, 0], [-1, 0, 0, 0, -1, -1, 0, -1, 0]], [[-1, 0, 0, 0, 0, 0, -1, -1, -1], [0, -1, 0, 0, -1, 0, 0, -1, -1], [0, 0, -1, -1, 0, 0, 0, -1, -1]]], [[[-1, 0, 0, 0, 0, -1, -1, -1, 0], [-1, -1, 0, -1, 0, 0, -1, 0, 0], [-1, 0, 0, -1, -1, 0, 0, 0, -1]], [[0, -1, -1, 0, 0, -1, -1, 0, 0], [-1, 0, 0, 0, -1, 0, 0, -1, -1], [0, -1, -1, -1, 0, 0, -1, 0, 0]], [[-1, 0, 0, -1, 0, 0, -1, -1, 0], [0, 0, 0, -1, 0, 0, -1, -1, -1], [-1, 0, -1, 0, -1, -1, 0, 0, 0]], [[0, 0, 0, 0, -1, -1, 0, -1, -1], [0, -1, -1, -1, 0, 0, 0, -1, 0], [-1, -1, 0, 0, -1, -1, 0, 0, 0]], [[-1, 0, -1, 0, -1, 0, 0, 0, -1], [0, -1, 0, -1, 0, 0, -1, 0, -1], [-1, -1, -1, 0, 0, -1, 0, 0, 0]], [[0, -1, -1, 0, 0, -1, 0, -1, 0], [0, 0, 0, 0, -1, -1, -1, -1, 0], [0, 0, -1, -1, -1, 0, 0, 0, -1]]], [[[-1, -1, -1, 0, -1, 0, 0, 0, 0], [0, 0, -1, 0, -1, -1, 0, 0, -1], [-1, 0, 0, -1, 0, -1, 0, 0, -1]], [[-1, 0, 0, 0, 0, 0, -1, -1, -1], [0, 0, -1, 0, 0, 0, -1, -1, -1], [0, -1, 0, -1, -1, 0, -1, 0, 0]], [[-1, -1, 0, 0, 0, 0, -1, -1, 0], [-1, 0, -1, 0, -1, 0, 0, -1, 0], [0, -1, 0, -1, 0, -1, -1, 0, 0]], [[0, -1, -1, 0, -1, -1, 0, 0, 0], [0, 0, 0, 0, -1, -1, 0, -1, -1], [0, -1, -1, -1, 0, 0, 0, -1, 0]], [[-1, 0, 0, 0, 0, -1, -1, 0, -1], [0, -1, 0, -1, 0, 0, -1, -1, 0], [-1, 0, -1, 0, 0, -1, -1, 0, 0]], [[-1, 0, 0, -1, -1, 0, 0, 0, -1], [0, -1, -1, -1, -1, 0, 0, 0, 0], [-1, 0, 0, -1, 0, -1, 0, -1, 0]]], [[[-1, 0, 0, -1, -1, 0, -1, 0, 0], [-1, 0, 0, 0, 0, -1, 0, -1, -1], [-1, -1, -1, 0, 0, 0, 0, 0, -1]], [[0, -1, -1, -1, 0, 0, 0, -1, 0], [0, 0, -1, -1, 0, 0, -1, -1, 0], [0, -1, -1, 0, -1, 0, -1, 0, 0]], [[0, -1, 0, 0, -1, 0, 0, -1, -1], [0, -1, 0, -1, -1, 0, -1, 0, 0], [-1, 0, -1, 0, -1, 0, 0, -1, 0]], [[-1, -1, 0, -1, 0, 0, -1, 0, 0], [0, 0, -1, 0, -1, -1, 0, -1, 0], [-1, -1, 0, 0, 0, -1, 0, -1, 0]], [[-1, 0, 0, 0, 0, -1, -1, 0, -1], [-1, 0, 0, -1, 0, -1, 0, 0, -1], [0, 0, -1, -1, 0, 0, -1, 0, -1]], [[0, 0, -1, 0, -1, -1, -1, 0, 0], [0, -1, 0, 0, 0, -1, 0, -1, -1], [-1, 0, 0, -1, -1, -1, 0, 0, 0]]], [[[-1, -1, 0, 0, 0, -1, 0, -1, 0], [0, -1, 0, -1, -1, -1, 0, 0, 0], [0, -1, 0, -1, 0, -1, -1, 0, 0]], [[0, -1, -1, 0, 0, -1, 0, 0, -1], [0, 0, 0, -1, -1, 0, -1, 0, -1], [0, 0, -1, -1, -1, 0, 0, -1, 0]], [[-1, 0, 0, 0, -1, 0, 0, -1, -1], [0, -1, -1, 0, -1, 0, -1, 0, 0], [0, 0, -1, 0, 0, -1, -1, -1, 0]], [[-1, 0, -1, 0, -1, 0, -1, 0, 0], [-1, 0, -1, -1, 0, 0, 0, 0, -1], [-1, 0, 0, 0, -1, -1, 0, -1, 0]], [[-1, 0, 0, -1, 0, 0, -1, -1, 0], [-1, -1, 0, 0, 0, 0, 0, -1, -1], [-1, -1, 0, -1, 0, 0, 0, -1, 0]], [[0, -1, -1, 0, 0, -1, 0, 0, -1], [-1, 0, -1, -1, 0, 0, -1, 0, 0], [0, 0, 0, 0, -1, -1, -1, 0, -1]]], [[[0, -1, -1, -1, 0, 0, 0, -1, 0], [0, -1, 0, -1, 0, -1, 0, 0, -1], [-1, 0, 0, 0, 0, -1, -1, -1, 0]], [[-1, -1, 0, 0, -1, 0, -1, 0, 0], [-1, -1, -1, 0, 0, 0, -1, 0, 0], [0, -1, 0, 0, -1, 0, -1, -1, 0]], [[0, 0, -1, -1, 0, 0, 0, -1, -1], [0, -1, 0, -1, -1, -1, 0, 0, 0], [0, 0, -1, -1, 0, 0, -1, -1, 0]], [[-1, 0, 0, -1, 0, -1, 0, 0, -1], [-1, 0, -1, 0, -1, 0, 0, -1, 0], [-1, 0, 0, -1, 0, 0, -1, -1, 0]], [[-1, 0, 0, 0, 0, -1, -1, 0, -1], [0, -1, 0, 0, -1, -1, 0, 0, -1], [0, -1, -1, 0, -1, -1, 0, 0, 0]], [[-1, 0, -1, -1, 0, -1, 0, 0, 0], [0, 0, 0, 0, -1, 0, -1, -1, -1], [-1, 0, -1, 0, -1, 0, 0, 0, -1]]], [[[0, -1, -1, 0, 0, -1, -1, 0, 0], [0, 0, 0, -1, -1, 0, 0, -1, -1], [-1, -1, -1, 0, -1, 0, 0, 0, 0]], [[-1, 0, 0, 0, -1, -1, 0, 0, -1], [0, 0, 0, -1, 0, -1, -1, 0, -1], [0, -1, -1, -1, 0, 0, 0, -1, 0]], [[-1, -1, -1, 0, -1, 0, 0, 0, 0], [0, -1, 0, 0, 0, 0, -1, -1, -1], [0, 0, -1, -1, 0, 0, -1, -1, 0]], [[0, -1, 0, 0, -1, -1, 0, -1, 0], [-1, -1, 0, -1, -1, 0, 0, 0, 0], [0, 0, -1, 0, 0, -1, -1, -1, 0]], [[-1, -1, 0, 0, -1, -1, 0, 0, 0], [-1, 0, 0, -1, 0, -1, 0, 0, -1], [-1, 0, 0, -1, 0, 0, 0, -1, -1]], [[0, 0, -1, 0, 0, -1, -1, 0, -1], [-1, 0, 0, 0, -1, 0, -1, -1, 0], [-1, 0, -1, -1, 0, 0, -1, 0, 0]]], [[[-1, 0, -1, 0, 0, 0, -1, -1, 0], [0, 0, -1, -1, 0, 0, 0, -1, -1], [-1, 0, 0, 0, 0, 0, -1, -1, -1]], [[-1, -1, 0, 0, 0, -1, -1, 0, 0], [-1, -1, 0, 0, 0, -1, 0, -1, 0], [0, -1, 0, -1, 0, 0, -1, -1, 0]], [[-1, 0, -1, -1, -1, 0, 0, 0, 0], [0, 0, -1, 0, -1, -1, 0, 0, -1], [0, -1, 0, -1, 0, -1, 0, 0, -1]], [[0, -1, -1, 0, -1, 0, 0, -1, 0], [0, 0, 0, -1, 0, -1, -1, 0, -1], [-1, -1, 0, 0, -1, 0, 0, -1, 0]], [[-1, 0, 0, -1, -1, -1, 0, 0, 0], [0, 0, 0, -1, -1, 0, -1, 0, -1], [0, 0, -1, 0, 0, -1, -1, 0, -1]], [[-1, 0, -1, -1, 0, -1, 0, 0, 0], [0, -1, 0, 0, -1, 0, -1, -1, 0], [-1, -1, -1, 0, -1, 0, 0, 0, 0]]], [[[0, -1, -1, -1, -1, 0, 0, 0, 0], [0, -1, 0, -1, 0, 0, -1, 0, -1], [-1, 0, 0, -1, 0, 0, -1, -1, 0]], [[0, -1, 0, -1, 0, 0, -1, -1, 0], [-1, -1, 0, -1, -1, 0, 0, 0, 0], [0, -1, 0, -1, 0, -1, 0, 0, -1]], [[-1, 0, 0, 0, -1, -1, -1, 0, 0], [-1, 0, -1, 0, -1, 0, 0, -1, 0], [-1, 0, 0, 0, -1, 0, 0, -1, -1]], [[0, 0, -1, 0, -1, -1, 0, 0, -1], [0, 0, -1, 0, 0, 0, -1, -1, -1], [-1, 0, -1, 0, 0, -1, -1, 0, 0]], [[-1, 0, -1, 0, 0, 0, -1, 0, -1], [-1, -1, 0, -1, 0, -1, 0, 0, 0], [-1, -1, 0, 0, -1, -1, 0, 0, 0]], [[0, -1, -1, 0, 0, -1, 0, -1, 0], [0, 0, -1, -1, -1, 0, 0, -1, 0], [0, 0, 0, 0, 0, -1, -1, -1, -1]]], [[[0, -1, 0, 0, 0, 0, -1, -1, -1], [-1, -1, -1, 0, 0, 0, 0, -1, 0], [0, 0, -1, -1, -1, 0, 0, 0, -1]], [[-1, 0, -1, 0, 0, 0, 0, -1, -1], [-1, -1, -1, 0, -1, 0, 0, 0, 0], [0, 0, 0, -1, 0, -1, -1, -1, 0]], [[-1, 0, 0, -1, 0, -1, 0, 0, -1], [-1, -1, -1, 0, -1, 0, 0, 0, 0], [-1, -1, 0, 0, -1, 0, -1, 0, 0]], [[0, 0, 0, -1, 0, -1, 0, -1, -1], [0, 0, 0, -1, -1, -1, -1, 0, 0], [0, -1, -1, -1, 0, 0, -1, 0, 0]], [[-1, 0, -1, 0, 0, 0, 0, -1, -1], [-1, 0, 0, -1, 0, -1, -1, 0, 0], [-1, -1, 0, -1, -1, 0, 0, 0, 0]], [[0, 0, 0, 0, -1, -1, 0, -1, -1], [0, 0, 0, 0, -1, -1, -1, -1, 0], [0, -1, -1, 0, 0, -1, -1, 0, 0]]], [[[0, -1, -1, 0, 0, -1, 0, 0, -1], [-1, 0, 0, -1, -1, -1, 0, 0, 0], [-1, 0, -1, 0, 0, 0, -1, -1, 0]], [[-1, 0, 0, -1, -1, 0, 0, -1, 0], [-1, -1, -1, 0, -1, 0, 0, 0, 0], [0, 0, -1, -1, 0, 0, -1, 0, -1]], [[-1, 0, 0, 0, 0, 0, -1, -1, -1], [0, 0, 0, 0, -1, -1, -1, -1, 0], [0, 0, 0, 0, -1, -1, -1, 0, -1]], [[0, -1, -1, 0, -1, 0, 0, 0, -1], [-1, -1, 0, -1, 0, 0, 0, -1, 0], [-1, 0, -1, 0, 0, 0, -1, -1, 0]], [[0, -1, 0, -1, -1, -1, 0, 0, 0], [-1, -1, 0, -1, 0, 0, 0, -1, 0], [0, 0, 0, -1, 0, -1, -1, 0, -1]], [[-1, -1, 0, 0, 0, 0, -1, -1, 0], [0, -1, -1, 0, -1, -1, 0, 0, 0], [0, 0, -1, -1, 0, -1, 0, 0, -1]]], [[[0, -1, -1, 0, 0, 0, -1, 0, -1], [-1, -1, 0, -1, 0, -1, 0, 0, 0], [0, 0, -1, 0, -1, 0, -1, -1, 0]], [[0, 0, 0, 0, -1, -1, -1, 0, -1], [0, 0, -1, 0, -1, 0, -1, 0, -1], [0, 0, 0, -1, 0, 0, -1, -1, -1]], [[-1, -1, 0, 0, -1, 0, 0, 0, -1], [0, -1, 0, 0, 0, -1, -1, -1, 0], [-1, -1, 0, 0, 0, 0, 0, -1, -1]], [[0, -1, -1, 0, -1, 0, 0, -1, 0], [-1, 0, -1, -1, 0, -1, 0, 0, 0], [0, 0, 0, -1, 0, -1, 0, -1, -1]], [[-1, -1, 0, 0, 0, -1, -1, 0, 0], [-1, 0, 0, -1, 0, 0, -1, -1, 0], [-1, 0, -1, -1, 0, -1, 0, 0, 0]], [[0, 0, -1, -1, -1, -1, 0, 0, 0], [-1, -1, 0, 0, -1, 0, 0, -1, 0], [-1, 0, -1, -1, -1, 0, 0, 0, 0]]], [[[0, 0, 0, -1, -1, -1, -1, 0, 0], [-1, 0, 0, 0, -1, 0, -1, -1, 0], [0, -1, 0, 0, 0, -1, 0, -1, -1]], [[-1, -1, 0, 0, -1, 0, -1, 0, 0], [-1, 0, -1, 0, 0, 0, -1, 0, -1], [0, 0, -1, -1, -1, -1, 0, 0, 0]], [[-1, 0, 0, -1, 0, -1, 0, -1, 0], [0, -1, -1, 0, 0, -1, 0, 0, -1], [0, 0, -1, -1, 0, 0, 0, -1, -1]], [[0, 0, 0, 0, -1, -1, 0, -1, -1], [0, 0, -1, 0, 0, -1, -1, 0, -1], [-1, -1, 0, -1, 0, 0, -1, 0, 0]], [[-1, -1, 0, 0, 0, 0, -1, -1, 0], [0, -1, -1, -1, -1, 0, 0, 0, 0], [-1, -1, -1, -1, 0, 0, 0, 0, 0]], [[0, 0, -1, -1, -1, 0, 0, -1, 0], [-1, 0, 0, 0, -1, -1, -1, 0, 0], [-1, -1, 0, 0, 0, 0, 0, -1, -1]]], [[[0, -1, 0, -1, 0, 0, -1, 0, -1], [0, 0, -1, 0, 0, -1, -1, -1, 0], [0, -1, -1, 0, 0, 0, 0, -1, -1]], [[-1, -1, 0, 0, 0, -1, -1, 0, 0], [-1, 0, 0, 0, -1, 0, -1, -1, 0], [0, -1, -1, -1, -1, 0, 0, 0, 0]], [[-1, 0, 0, -1, 0, 0, 0, -1, -1], [-1, 0, -1, 0, -1, 0, -1, 0, 0], [-1, 0, -1, 0, 0, -1, 0, -1, 0]], [[-1, 0, 0, -1, 0, -1, 0, -1, 0], [-1, 0, 0, 0, 0, -1, -1, -1, 0], [0, -1, 0, -1, -1, -1, 0, 0, 0]], [[0, 0, -1, -1, 0, 0, 0, -1, -1], [0, 0, 0, -1, -1, -1, 0, 0, -1], [0, -1, -1, 0, -1, 0, 0, 0, -1]], [[-1, 0, -1, 0, 0, -1, -1, 0, 0], [0, -1, 0, 0, -1, 0, -1, 0, -1], [-1, -1, 0, -1, -1, 0, 0, 0, 0]]], [[[-1, 0, 0, -1, 0, -1, 0, 0, -1], [-1, 0, -1, 0, 0, 0, -1, 0, -1], [-1, -1, 0, 0, 0, -1, 0, 0, -1]], [[0, 0, 0, -1, -1, -1, 0, -1, 0], [-1, -1, 0, 0, 0, -1, 0, -1, 0], [0, -1, -1, 0, 0, 0, -1, 0, -1]], [[-1, 0, -1, -1, 0, 0, 0, 0, -1], [-1, -1, 0, -1, 0, 0, 0, -1, 0], [0, -1, -1, 0, -1, 0, -1, 0, 0]], [[-1, 0, 0, 0, -1, 0, -1, -1, 0], [-1, -1, 0, 0, 0, 0, -1, -1, 0], [0, 0, -1, -1, 0, 0, -1, -1, 0]], [[0, 0, -1, 0, -1, -1, 0, 0, -1], [0, -1, 0, 0, -1, -1, -1, 0, 0], [0, 0, -1, -1, -1, 0, 0, -1, 0]], [[-1, 0, 0, -1, -1, -1, 0, 0, 0], [0, 0, 0, -1, 0, -1, -1, -1, 0], [0, -1, -1, 0, -1, 0, 0, 0, -1]]], [[[0, -1, -1, 0, -1, 0, -1, 0, 0], [-1, 0, 0, 0, -1, 0, 0, -1, -1], [0, 0, 0, -1, -1, -1, 0, 0, -1]], [[-1, -1, -1, 0, 0, 0, 0, -1, 0], [0, 0, -1, 0, -1, 0, -1, 0, -1], [0, -1, 0, 0, 0, -1, -1, 0, -1]], [[-1, 0, 0, -1, 0, -1, 0, -1, 0], [-1, 0, -1, 0, -1, 0, -1, 0, 0], [-1, 0, -1, -1, 0, -1, 0, 0, 0]], [[0, 0, -1, 0, -1, -1, 0, -1, 0], [0, -1, 0, -1, -1, 0, 0, 0, -1], [-1, -1, 0, 0, 0, 0, -1, 0, -1]], [[-1, 0, -1, -1, 0, 0, 0, -1, 0], [0, -1, 0, -1, 0, -1, -1, 0, 0], [0, 0, -1, 0, -1, 0, -1, -1, 0]], [[-1, 0, 0, -1, 0, 0, 0, -1, -1], [-1, -1, 0, 0, 0, -1, 0, -1, 0], [0, -1, 0, -1, 0, -1, -1, 0, 0]]], [[[0, -1, 0, 0, -1, 0, -1, 0, -1], [-1, -1, -1, 0, 0, -1, 0, 0, 0], [-1, -1, 0, 0, 0, -1, 0, 0, -1]], [[0, -1, -1, -1, 0, 0, 0, 0, -1], [-1, 0, 0, 0, -1, 0, -1, -1, 0], [0, -1, 0, -1, -1, -1, 0, 0, 0]], [[-1, 0, 0, 0, -1, -1, 0, -1, 0], [0, 0, 0, -1, -1, 0, -1, 0, -1], [0, 0, -1, -1, 0, 0, -1, -1, 0]], [[-1, -1, 0, -1, 0, -1, 0, 0, 0], [-1, -1, 0, -1, 0, 0, 0, 0, -1], [0, -1, -1, 0, 0, 0, 0, -1, -1]], [[-1, 0, -1, 0, 0, 0, -1, -1, 0], [0, 0, -1, 0, 0, -1, 0, -1, -1], [-1, 0, -1, 0, -1, 0, 0, -1, 0]], [[0, 0, -1, 0, -1, -1, -1, 0, 0], [0, 0, 0, -1, -1, 0, -1, -1, 0], [-1, 0, 0, -1, 0, -1, -1, 0, 0]]], [[[0, 0, -1, -1, 0, -1, 0, 0, -1], [0, -1, -1, 0, -1, -1, 0, 0, 0], [0, -1, 0, 0, -1, 0, -1, -1, 0]], [[0, -1, 0, -1, 0, 0, -1, 0, -1], [-1, 0, 0, 0, -1, -1, 0, -1, 0], [-1, -1, 0, 0, -1, -1, 0, 0, 0]], [[-1, 0, -1, -1, 0, 0, 0, -1, 0], [0, 0, 0, 0, -1, -1, -1, -1, 0], [-1, 0, -1, 0, 0, -1, -1, 0, 0]], [[-1, 0, -1, 0, -1, 0, 0, 0, -1], [0, -1, 0, 0, 0, -1, 0, -1, -1], [0, -1, 0, -1, -1, 0, -1, 0, 0]], [[-1, 0, 0, -1, 0, 0, -1, -1, 0], [0, -1, -1, -1, -1, 0, 0, 0, 0], [0, 0, 0, -1, 0, -1, 0, -1, -1]], [[-1, -1, -1, 0, 0, 0, -1, 0, 0], [-1, 0, 0, 0, 0, 0, -1, -1, -1], [-1, 0, -1, -1, 0, 0, 0, 0, -1]]], [[[-1, -1, 0, 0, -1, -1, 0, 0, 0], [-1, -1, -1, 0, -1, 0, 0, 0, 0], [0, 0, -1, -1, 0, -1, 0, 0, -1]], [[-1, 0, 0, 0, -1, 0, -1, 0, -1], [0, -1, 0, 0, 0, -1, 0, -1, -1], [0, 0, 0, -1, 0, -1, -1, -1, 0]], [[0, -1, 0, -1, 0, 0, 0, -1, -1], [-1, 0, -1, -1, 0, 0, -1, 0, 0], [0, 0, 0, -1, -1, -1, 0, 0, -1]], [[0, -1, -1, 0, -1, 0, 0, -1, 0], [-1, 0, 0, 0, -1, -1, -1, 0, 0], [0, -1, 0, -1, 0, -1, 0, -1, 0]], [[-1, -1, -1, 0, 0, 0, -1, 0, 0], [-1, 0, -1, 0, 0, 0, -1, 0, -1], [-1, 0, -1, 0, 0, 0, -1, -1, 0]], [[0, -1, 0, -1, 0, 0, 0, -1, -1], [0, 0, 0, -1, -1, 0, -1, -1, 0], [-1, 0, -1, 0, -1, -1, 0, 0, 0]]], [[[-1, 0, 0, 0, -1, 0, 0, -1, -1], [0, 0, -1, 0, -1, -1, 0, 0, -1], [0, 0, 0, 0, -1, -1, -1, -1, 0]], [[-1, -1, 0, 0, 0, 0, -1, -1, 0], [-1, -1, -1, 0, 0, 0, -1, 0, 0], [0, -1, -1, -1, 0, 0, 0, -1, 0]], [[-1, 0, 0, -1, -1, 0, 0, 0, -1], [-1, 0, -1, 0, 0, -1, 0, 0, -1], [0, -1, 0, 0, 0, 0, -1, -1, -1]], [[0, 0, 0, -1, 0, -1, -1, -1, 0], [-1, 0, 0, -1, -1, -1, 0, 0, 0], [0, 0, -1, 0, -1, 0, -1, -1, 0]], [[-1, -1, -1, 0, 0, -1, 0, 0, 0], [0, 0, 0, -1, 0, -1, 0, -1, -1], [-1, -1, 0, 0, 0, -1, 0, 0, -1]], [[-1, -1, 0, -1, 0, 0, -1, 0, 0], [0, -1, -1, -1, -1, 0, 0, 0, 0], [0, 0, -1, -1, -1, 0, -1, 0, 0]]], [[[-1, 0, -1, -1, 0, -1, 0, 0, 0], [-1, -1, 0, 0, 0, 0, -1, 0, -1], [0, -1, 0, -1, -1, -1, 0, 0, 0]], [[0, -1, 0, -1, -1, 0, -1, 0, 0], [-1, 0, 0, 0, -1, -1, 0, -1, 0], [-1, 0, -1, 0, 0, -1, 0, 0, -1]], [[0, -1, -1, 0, -1, 0, 0, 0, -1], [-1, -1, -1, 0, 0, 0, -1, 0, 0], [-1, 0, 0, 0, -1, 0, 0, -1, -1]], [[0, 0, 0, -1, -1, -1, 0, -1, 0], [-1, -1, -1, -1, 0, 0, 0, 0, 0], [-1, 0, -1, 0, 0, 0, 0, -1, -1]], [[0, 0, 0, 0, -1, 0, -1, -1, -1], [0, -1, 0, 0, -1, -1, 0, -1, 0], [0, 0, 0, -1, 0, -1, -1, 0, -1]], [[0, 0, -1, -1, 0, 0, -1, -1, 0], [-1, -1, 0, -1, 0, 0, -1, 0, 0], [0, 0, -1, 0, 0, -1, -1, -1, 0]]]]

    font = ImageFont.truetype("arial.ttf", 18)
    font_company = ImageFont.truetype("arial.ttf", 11)
    pages = 2

    for m in range(0,pages):
        bingopage=[]

        full_image = variations[random.randint(0,len(variations)-1)]

        for i in range(0,9):
            col = []
            if(i==0):
                for n in range(1,10):
                    col.append(n)
            elif(i==8):
                for n in range(80,91):
                    col.append(n)
            else:
                for n in range(i*10,i*10+10):
                    col.append(n)
            random.shuffle(col)
            #print(col)
            for j in range (0,6):
                count=0
                for k in range(0,3):
                    if(full_image[j][k][i]==0):
                        count+=1
                ordered = col[:count]
                col=col[count:]
                ordered.sort()
                for k in range(0,3):
                    if(full_image[j][k][i]==0):
                        full_image[j][k][i]=ordered[0]
                        ordered=ordered[1:]
        
        for i in range (0,6):
            height = 451
            width = 151
            image = Image.new(mode='L', size=(height, width), color=255)

            # Draw some lines
            draw = ImageDraw.Draw(image)
 
            y_start = 0
            y_end = image.height
            step_size = int(image.width / 9)

            for x in range(0, image.width, step_size):
                line = ((x, y_start), (x, y_end))
                draw.line(line, fill=128)

            x_start = 0
            x_end = image.width
            step_size = int(image.height / 3)

            for y in range(0, image.height, step_size):
                line = ((x_start, y), (x_end, y))
                draw.line(line, fill=128)

            del draw

            # ran15 = random.sample(range(1, 90), 15)
            # print(ran15)

            # for j in range(0,3):
            #     ran5=ran15[j*5:j*5+5]
            #     ran5.append(-1)
            #     ran5.append(-1)
            #     ran5.append(-1)
            #     ran5.append(-1)
            #     random.shuffle(ran5)
            #     print(ran5)
            #     for k in range(0,9):
            #         if(ran5[k]==-1):
            #             continue
            #         d =ImageDraw.Draw(image)
            #         d.text((k*50+14,j*50+14),str(ran5[k]),font=font)

            # ran27 = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

            # for i in range(0,3):
            #     spaces = random.sample(range(0, 9), 4)
            #     for j in range(0, 4):
            #         ran27[i][spaces[j]] =-1


            # for i in range(0,9):
            #     count = 0
            #     for j in range(0,3):
            #         if(ran27[j][i]==0):
            #             count = count+1
            #     if(i==0):
            #         col = random.sample(range(1,10), count)
            #     elif(i==8):
            #         col = random.sample(range(80,91), count)
            #     else:
            #         col = random.sample(range(i*10,i*10+10 ), count)
            #     col.sort()
            #     k=0
            #     skip=0
            #     while(k!=len(col)):
            #         if(ran27[k+skip][i]==0):
            #             ran27[k+skip][i]=col[k]
            #             k=k+1
             
            #         else:
            #             skip=skip+1
            ran27 = full_image[i]

            for j in range(0,3):
                ran5=ran27[j]
                
                for k in range(0,9):
                    if(ran5[k]==-1):
                        continue
                    d =ImageDraw.Draw(image)
                    d.text((k*50+14,j*50+14),str(ran5[k]),font=font)

            bingopage.append(image)

        dst = Image.new(mode='L', size=(1050, 650), color=255)
        dst.paste(bingopage[0], (50, 50))
        dst.paste(bingopage[1], (550, 50))
        dst.paste(bingopage[2], (50, 250))
        dst.paste(bingopage[3], (550, 250))
        dst.paste(bingopage[4], (50, 450))
        dst.paste(bingopage[5], (550, 450))

        #writing the name
        text = ""
        named = ImageDraw.Draw(dst)
        named.text((150,220),text,font=font_company)
        named.text((650,220),text,font=font_company)
        named.text((150,420),text,font=font_company)
        named.text((650,420),text,font=font_company)
        named.text((150,620),text,font=font_company)
        named.text((650,620),text,font=font_company)

        dst.save(str(m+1)+'.png')
    
    