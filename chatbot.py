import time
from datetime import datetime
from colorama import Fore, Style, init
from pyfiglet import figlet_format
init(autoreset=True)
def slow_print(text, color=Fore.CYAN):
    for ch in text:
        print(color + ch, end="", flush=True)
        time.sleep(0.02)
    print()
print(Fore.MAGENTA + figlet_format("CHAT BOT"))
print(Fore.YELLOW + "=" * 60)
print(Fore.GREEN + "🤖 Welcome to CodeAlpha Basic Chatbot")
print(Fore.YELLOW + "=" * 60)
name = input(Fore.CYAN + "\nEnter your name: ")
print(Fore.GREEN + f"\nHello {name}! 😊")
print(Fore.BLUE + "Current Date :", datetime.now().strftime("%d-%m-%Y"))
print(Fore.BLUE + "Current Time :", datetime.now().strftime("%I:%M %p"))
print(Fore.YELLOW + "\nYou can ask me these questions:")
print(Fore.WHITE + """
1. hello
2. hi
3. how are you
4. what is your name
5. who created you
6. what can you do
7. tell me a joke
8. tell me about python
9. what is today's date
10. what time is it
11. thank you
12. bye
""")
responses = {
    "hello": "Hello! 👋 Nice to meet you.",
    "hi": "Hi! 😊",
    "how are you": "I am doing great! Thanks for asking. 😄",
    "what is your name": "My name is CodeAlpha Bot. 🤖",
    "who created you": "I was created using Python.",
    "what can you do": "I can answer simple questions and chat with you.",
    "tell me a joke": "Why do programmers love Python? Because it's easy to understand! 😂",
    "tell me about python": "Python is a popular programming language used for AI, Web Development, Data Science and Automation.",
    "what is today's date": datetime.now().strftime("%d-%m-%Y"),
    "what time is it": datetime.now().strftime("%I:%M %p"),
    "thank you": "You're welcome! 😊",
    "bye": "Goodbye! Have a wonderful day! 👋"
}
while True:
    user = input(Fore.GREEN + "\nYou : ").lower()
    if user in responses:
        slow_print("Bot : " + responses[user], Fore.CYAN)
        if user == "bye":
            print(Fore.MAGENTA + "\nThank you for using CodeAlpha Chatbot!")
            break
    else:
        slow_print("Bot : Sorry! I don't understand that question.", Fore.RED)