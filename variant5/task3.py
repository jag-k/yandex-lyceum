from PIL.ImageDraw import ImageDraw


class ImageDrawer(ImageDraw):
    def __init__(self, im):
        super().__init__(im)

    def horizontal_trapezium(self, xy, width, height, fill=None, outline=None):
        x, y = xy  # type: int
        top, bottom = width  # type: int
        d = (top - bottom) // 2  # type: int

        if d < 0:
            p = [(x - d, y),
                 (x - d + top, y),
                 (x - d + top - d, y + height),
                 (x - d + top - bottom - d, y + height)]
        else:
            p = [(x, y),
                 (x + top, y),
                 (x - d + top, y + height),
                 (x - d + top - bottom, y + height)]

        self.polygon(p, fill=fill, outline=outline)

    def vertical_trapezium(self, xy, width, height, fill=None, outline=None):
        x, y = xy  # type: int
        left, right = height  # type: int
        d = (left - right) // 2  # type: int

        if d > 0:
            p = [(x, y),
                 (x, y + left),
                 (x + width, y + left - d),
                 (x + width, y + left - d - right)]
        else:
            p = [(x, y - d),
                 (x, y + left - d),
                 (x + width, y + left - d - d),
                 (x + width, y + left - d - right - d)]

        self.polygon(p, fill=fill, outline=outline)
