#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Multiplication Table 1 to 15

for i in range(1, 15):
    for j in range(1, i + 1):
        print('{:2d}x{:2d}={:3d}\t'.format(j, i, i * j), end='')
    print()
