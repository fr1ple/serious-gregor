def mult(a,b):
  return a*b

print(mult(3, 4))

print (mult(b=4, a=3))

def varargs(*args):
  return args

print(varargs(32,23))

print(varargs(32,23,13))

print(varargs(32))
print(varargs(23,4,4,4,4))

def complex(x1,x2,*args,**kwargs):
  print(x1)
  print(x2)
  print(args[0])
  print(kwargs["first"])
  print(kwargs["second"])
  
complex(1,2,3,first=4,second=5)

