"""chatbot"""

"""
    Steps:
    1. input/listen
    2. process
    3. output/talkback
"""
greet_words = ['hi', 'hello', 'yo']
bye_words = ['bye', 'tata', 'hasta la vista']
bad_words = ['dog', 'bitch', 'fuck']

def listen():
    return input("Say something: ")

def decide(command):
    command = command.lower()
    broken_words = command.split(" ")
    # print(broken_words)

    for word in broken_words:
        if word in greet_words:
            talkback("Hi man")
            break

        elif word in bye_words:
            talkback("Bye Bye")
            break
        
        elif word in bad_words:
            talkback("Behave yourself")
            break

def talkback(response):
    print(response)

while True:
    command = listen()
    decide(command)