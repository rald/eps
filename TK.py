class TK:

  def __init__(self,pos,typ,val):
    self.pos=pos
    self.typ=typ
    self.val=val

  def __str__(self):
    return f"TK {{ pos: {self.pos}, typ: {self.typ}, val: '{self.val}' }}"

  def __repr__(self):
    return self.__str__()


