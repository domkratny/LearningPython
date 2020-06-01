## https://www.hackerrank.com/challenges/text-wrap/problem?h_r=next-challenge&h_v=zen
import math

def wrap(string, max_width):
    text = string
    for i in range(0, math.ceil(len(text) / (1.0 * max_width))):
        print(text[i*max_width:i*max_width+max_width])

print("================================")
wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 5)
print("================================")