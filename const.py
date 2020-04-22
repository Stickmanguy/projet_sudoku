class Const:
   def __init__(self):
       Const.__items = {}
   def __getattr__(self, attr):
       try:
           return Const.__items[attr]
       except:
           return self.__dict__[attr]
   def __setattr__(self, attr, value):
       if attr in Const._items:  # En python 2.1, écrire if attr in Const.__items.keys()
           raise "Cannot reassign constant %s" % attr
       else:
           Const.__items[attr] = value
   def __str__(self):
       return '\n'.join(['%s: %s' % (str(k), str(v)) for k,v in Const.__items.items()])