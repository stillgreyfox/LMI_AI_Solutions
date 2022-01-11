class Mask:
    """
    the class for polygon mask annotations
    """
    def __init__(self, im_name, fullpath, category='', x_vals=[], y_vals=[]) -> None:
        """
        Arguments:
            im_name(str): the image file basename
            fullpath(str): the location of the image file
            category(str): the categorical class name of this image
            x_vals(list): the x values [x1, x2, ..., xn] of the polygon
            y_vals(list): the y values [y1, y2, ..., yn] of the polygon
        """
        self.im_name = im_name
        self.fullpath = fullpath
        self.category = category
        self.X = x_vals
        self.Y = y_vals
        