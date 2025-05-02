from textblob import TextBlob
from colorama import init, Fore
import time
import re

# Initialize colorama
init()

# Global Variables
conversation_history = []
sentiment_counters = {'positive': 0, 'neutral': 0, 'negative': 0}

def show_processing_animation():
    print("Analyzing", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
    print()

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        sentiment = 'positive'
    elif polarity < -0.1:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'

    return sentiment, polarity

def execute_command(command):
    command = command.lower()
    if command == 'summary':
        print("\nSentiment Summary:")
        for k, v in sentiment_counters.items():
            print(f"  {k.capitalize()}: {v}")
    elif command == 'reset':
        conversation_history.clear()
        for key in sentiment_counters:
            sentiment_counters[key] = 0
        print(Fore.YELLOW + "Conversation and sentiment data reset." + Fore.RESET)
    elif command == 'history':
        print("\nConversation History:")
        for entry in conversation_history:
            print(f"{entry['text']} => {entry['sentiment']} (Polarity: {entry['polarity']:.2f})")
    elif command == 'help':
        print("\nAvailable Commands: summary, reset, history, help, exit")
    else:
        print("Unknown command. Type 'help' for available commands.")

def get_valid_name():
    while True:
        name = input("Enter your name: ")
        if name.isalpha():
            return name
        else:
            print("Name must only contain alphabetic characters. Please try again.")

def save_summary_to_file(username):
    filename = f"{username}_sentiment_analysis.txt"
    with open(filename, 'w') as file:
        file.write(f"Sentiment Analysis Summary for {username}\n\n")
        for entry in conversation_history:
            file.write(f"{entry['text']} => {entry['sentiment']} (Polarity: {entry['polarity']:.2f})\n")
        file.write("\nFinal Summary:\n")
        for k, v in sentiment_counters.items():
            file.write(f"{k.capitalize()}: {v}\n")
    print(f"\nSummary saved to '{filename}'")

def main():
    username = get_valid_name()
    print(f"\nHello, {username}! Type any sentence and I'll analyze its sentiment.")
    print("Type 'help' to see available commands. Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'exit':
            break
        elif user_input.lower() in ['summary', 'reset', 'history', 'help']:
            execute_command(user_input)
        else:
            show_processing_animation()
            sentiment, polarity = analyze_sentiment(user_input)
            color = Fore.GREEN if sentiment == 'positive' else Fore.RED if sentiment == 'negative' else Fore.YELLOW
            print(color + f"Sentiment: {sentiment.capitalize()} (Polarity: {polarity:.2f})" + Fore.RESET)
            
            sentiment_counters[sentiment] += 1
            conversation_history.append({'text': user_input, 'sentiment': sentiment, 'polarity': polarity})

    print("\nChat ended. Generating final summary...")
    execute_command('summary')
    save_summary_to_file(username)

if __name__ == "__main__":
    main()
