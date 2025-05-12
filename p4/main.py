import random

moves = ["Rock", "Paper", "Scissors"]

def determine_winner(player, ai):
    if player == ai:
        return "Tie"
    elif (player == "Rock" and ai == "Scissors") or \
         (player == "Paper" and ai == "Rock") or \
         (player == "Scissors" and ai == "Paper"):
        return "Player"
    else:
        return "AI"

player_score = 0
ai_score = 0

continue_playing = True
while continue_playing:
    while True:
        player_move = input("Enter your move (Rock, Paper, Scissors): ").strip().capitalize()
        if player_move in moves:
            break
        else:
            print("Invalid move. Please try again.")
    
    ai_move = random.choice(moves)
    
    result = determine_winner(player_move, ai_move)
    
    if result == "Player":
        player_score += 1
    elif result == "AI":
        ai_score += 1
    
    print(f"Player chose: {player_move}")
    print(f"AI chose: {ai_move}")
    print(f"Result: {result}")
    print(f"Score - Player: {player_score}, AI: {ai_score}")
    
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower().strip()
        if play_again == "yes":
            break
        elif play_again == "no":
            continue_playing = False
            break
        else:
            print("Please enter 'yes' or 'no'.")

print("Final Score")
print(f"Player: {player_score}")
print(f"AI: {ai_score}")