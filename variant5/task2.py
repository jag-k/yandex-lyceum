def sorted2(data, key=(lambda x: -x)):
    return sorted((sorted(i, key=key) for i in data), key=lambda x: key(x[-1]))
