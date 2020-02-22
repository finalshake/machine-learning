class Students(object):
  def __init__(self, name):
    self.__name = name
  def __call__(self, score = 60):
    print('My name is %s, score is %d.' %(self.__name, score))


s = Students('Mark')
s(90)
