class Students(object):
  @property
  def score(self):
    return self.__score

  @score.setter
  def score(self, value):
    if not isinstance(value, int):
      raise valueerror('score must be an integer!')
    if value < 0 or value > 100:
      raise valueerror('score must between 0 ~ 100!')
    self.__score = value
#这样就可以直接用=了
s = Students()
s.score = 100
print(s.score)
