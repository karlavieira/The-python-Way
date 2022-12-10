x = "awesome" #Global variable

def myfunc():
  global x #that create a global variable inside a funcion
  x = "fantastic" 

myfunc()

print("Python is " + x)