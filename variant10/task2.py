def sorted2(data, key=(lambda x: -x)):
    n = len(data)
    d = sorted((i for j in data for i in j), key=key)
    return list(map(list, zip(*(d[i * n:i * n + n] for i in range(len(data[0]))))))
