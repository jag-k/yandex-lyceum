from sys import stdin
r = list(map(int, input().split()))
r[1] += 1
r = range(*r)

for i in stdin:
    numbs = list(filter(lambda n: n in r, map(int, i.split())))
    print(max(numbs, key=lambda x: (numbs.count(x), x)) if numbs else -1)
