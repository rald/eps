class P:

  def __init__(self,ln,cl):
    self.ln=ln+1
    self.cl=cl+1

  def __str__(self):
    return f"P {{ line: {self.ln}, column: {self.cl} }}"
  
  def __repr__(self):
    return self.__str__()
