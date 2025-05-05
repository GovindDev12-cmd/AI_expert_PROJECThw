import colorama
from datetime import datetime, timedelta
import random


colorama.init()


time_zones = {
    "new york": -5,
    "london": 0,
    "tokyo": 9,
    "sydney": 10
}


def get_weather(city):
    
   
    conditions = ["sunny", "cloudy", "rainy", "snowy"]
    condition = random.choice(conditions)
    return f"The weather in {city.title()} is {condition}."


def get_time(city):
    
    if city.lower() not in time_zones:
        return f"Sorry, I don't have the time zone for {city.title()}."
    offset = time_zones[city.lower()]
    utc_time = datetime.utcnow()
    city_time = utc_time + timedelta(hours=offset)
    return f"The current time in {city.title()} is {city_time.strftime('%Y-%m-%d %H:%M:%S')}."


def get_news():
    
    headlines = [
        "Breaking: Scientists discover new planet",
        "Stock market hits all-time high",
        "Local team wins championship"
    ]
    return "Here are some news headlines:\n" + "\n".join(headlines)


def chatbot():
    history = []
    
    
    try:
        with open("chatbot_history.txt", "r") as file:
            lines = file.readlines()
            for i in range(0, len(lines), 2):
                if i + 1 < len(lines):
                    user_input = lines[i].strip()
                    response = lines[i + 1].strip()
                    history.append((user_input, response))
    except FileNotFoundError:
        pass

    # Welcome message
    print(colorama.Fore.BLUE + "Chatbot: Hello! I can provide weather, time, and news. Type 'help' for commands." + colorama.Style.RESET_ALL)

    while True:
        user_input = input("You: ").strip().lower()
        
       
        if not user_input:
            continue

        
        response = ""
        if user_input == "exit":
            print(colorama.Fore.BLUE + "Chatbot: Goodbye!" + colorama.Style.RESET_ALL)
            break
        elif user_input == "help":
            response = (
                "Available commands:\n"
                "weather <city>: Get weather for a city\n"
                "time <city>: Get current time in a city\n"
                "news: Get latest news headlines\n"
                "history: Show previous conversations\n"
                "help: Show this help message\n"
                "exit: Exit the chatbot"
            )
            print(colorama.Fore.BLUE + f"Chatbot: {response}" + colorama.Style.RESET_ALL)
        elif user_input.startswith("weather"):
            # TODO: Improve input handling with keyword lists and regular expressions for better matching
            parts = user_input.split()
            if len(parts) < 2:
                response = "Please provide a city for the weather (e.g., 'weather London')."
                print(colorama.Fore.RED + f"Chatbot: {response}" + colorama.Style.RESET_ALL)
            else:
                city = " ".join(parts[1:])
                response = get_weather(city)
                print(colorama.Fore.GREEN + f"Chatbot: {response}" + colorama.Style.RESET_ALL)
        elif user_input.startswith("time"):
            # TODO: Improve input handling with keyword lists and regular expressions for better matching
            parts = user_input.split()
            if len(parts) < 2:
                response = "Please provide a city for the time (e.g., 'time New York')."
                print(colorama.Fore.RED + f"Chatbot: {response}" + colorama.Style.RESET_ALL)
            else:
                city = " ".join(parts[1:])
                response = get_time(city)
                print(colorama.Fore.BLUE + f"Chatbot: {response}" + colorama.Style.RESET_ALL)
        elif user_input == "news":
            response = get_news()
            print(colorama.Fore.YELLOW + f"Chatbot: {response}" + colorama.Style.RESET_ALL)
        elif user_input == "history":
            if not history:
                response = "No previous conversations found."
                print(colorama.Fore.BLUE + f"Chatbot: {response}" + colorama.Style.RESET_ALL)
            else:
                response = "Previous conversations:\n"
                for i, (inp, resp) in enumerate(history, 1):
                    response += f"{i}. You: {inp}\n   Chatbot: {resp}\n"
                print(colorama.Fore.BLUE + f"Chatbot: {response}" + colorama.Style.RESET_ALL)
                continue  # Skip adding the history command to history
        else:
            response = "I don't understand. Type 'help' for commands."
            print(colorama.Fore.RED + f"Chatbot: {response}" + colorama.Style.RESET_ALL)

        # Store the conversation in history (except for history command)
        history.append((user_input, response))

    
    with open("chatbot_history.txt", "w") as file:
        for user_input, response in history:
            file.write(f"{user_input}\n{response}\n")


if __name__ == "__main__":
    chatbot()