from sys import stdin
x = int(input())

for i in stdin:
    numbs = list(filter(lambda n: not n % x, map(int, i.split())))
    print(max(numbs) - min(numbs) if numbs else -1)
