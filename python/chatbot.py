# --- Define your functions below! ---
def say_hello():
    print("Hello!")
    username = input("What's your name?\n")
    print("Welcome," + username + "! I'm chatbot.")

def process_input(response):
    if response == "hi" or "Hi":
        output = "Hey"
        print(output)
    else:
        output = "That's cool!"
        print(output)



# --- Put your main program below! ---
def main():
  while True:
      answer = input("(What will you say?)")
      # process_input(answer)



# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    say_hello()
    main()
