class Singleton:
  def __init__(self, clase):
    self.clase = clase
    self.instance = 0
  def __call__(self, *args):
    if self.instance == 0:
      self.instance = self.clase(*args)
    return self.instance