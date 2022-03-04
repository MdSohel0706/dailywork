'''
Example 2: Passing the function as an argument
'''
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def func(myfunc):
    sentence = myfunc("This is a normal SENTENCE")
    print(sentence)

func(shout)
func(whisper)

'''
In the above example, the greet function takes another function as a parameter (shout and whisper in this case). 
The function passed as an argument is then called inside the function greet.
'''


