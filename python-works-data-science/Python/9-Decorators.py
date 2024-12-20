##Intoduction to Decorators

def greet(func): 
    # storing the function in a variable 
    greeting = func("""Hi, I am created by a function passed as an argument.""") 
    print (greeting) 

@greet
def shout(text): 
    return text.upper() 
  
@greet 
def whisper(text): # passing this func as parameter in decorator func
    return text.lower() 