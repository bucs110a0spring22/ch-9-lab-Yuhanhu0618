class Rectangle:
  def __init__(self, x=0, y=0, h=0, w=0):
    '''
    Initilize the rectangle object
	args: (int) Take in the dimensions of the rectangle with the default of 0 in case it's less than 0.
	return: None
    '''
    if x<0:
      x = 0
    if y<0:
      y = 0
    if h<0:
      h = 0
    if w<0:
      w = 0
    self.x = x
    self.y = y
    self.height = h
    self.width = w

  def __str__(self):
    '''
    Returns the dimensions of the rectangel
	args: None
	return: (str) Returns the dimensions of the rectangle in str form.
    '''
    return "Top left x = " + str(self.x) + "top left y = " + str(self.y) + "height = " + str(self.height) + "width" + str(self.width)
