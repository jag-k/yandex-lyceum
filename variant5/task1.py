from sys import stdin
x = int(input())

for i in stdin:
    numbs = list(filter(lambda n: not n % x, map(int, i.split())))
    print(max(numbs, key=lambda x: (numbs.count(x), -x)) if numbs else -1)
