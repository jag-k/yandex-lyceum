def map2(data, key=(lambda x: x * 2)):
    return [map2(i, key) if type(i) is list else key(i) for i in data]
