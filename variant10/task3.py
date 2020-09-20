from PIL.ImageDraw import ImageDraw


class ImageDrawer(ImageDraw):
    def __init__(self, im):
        super().__init__(im)

    def down_parallelogram(self, xy, height, fill=None, outline=None):
        x1, y1, x2, y2 = xy  # type: int
        p = [
            (x1, y1),
            (x1, y1 + height),
            (x2, y2),
            (x2, y2 - height)
        ]

        self.polygon(p, fill=fill, outline=outline)

    def up_parallelogram(self, xy, height, fill=None, outline=None):
        x1, y1, x2, y2 = xy  # type: int
        p = [
            (x1, y2 - height),
            (x1, y2),
            (x2, y1 + height),
            (x2, y1)
        ]

        self.polygon(p, fill=fill, outline=outline)
