#!/usr/bin/env python3
import matplotlib.pyplot as plt

def main():
    data = []
    with open('counter.txt') as f:
        data = [int(line.strip()) for line in f]

    n, bins, patches = plt.hist(x=data, bins='auto', color='#4287f5')
    plt.savefig('histogram')

if __name__ == '__main__':
    main()
