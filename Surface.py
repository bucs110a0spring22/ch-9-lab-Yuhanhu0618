from Rectangle import Rectangle

class Surface:
  def __init__(self, filename, x, y, h, w):
    '''
    Initilize the rectangle object and saving a filename.
	args: (str, int) Stores the filename in image as a str; take in the rectangle dimensions as int and make a rectangle.
	return: None
    '''
    self.image = filename
    self.rect = Rectangle(x, y, h, w)

  def getRect(self):
    '''
    Returns the rectangle object
	args: None
	return: (int) Returns the rectangle object in self.rect
    '''
    return self.rect