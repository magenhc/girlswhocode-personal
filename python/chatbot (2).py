# --- Define your functions below! ---
def intro():
    print("Hello!")
    answer = input("What's your name?\n")
    print("Welcome," + answer + "! I'm chatbot.")

def process_input(response):
    output = "Hey"
    if response == "hi" or "Hi":
        print(output)
    else:
        print("That's cool.")



# --- Put your main program below! ---
def main():
  while True:
      answer = input("(What will you say?)")
      process_input(answer)



# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    intro()
    main()
