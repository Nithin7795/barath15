import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "win"
    else:
        return "lose"

def print_scores(scores):
    print(f"\nScores:\nPlayer: {scores['player']}\nComputer: {scores['computer']}\nTies: {scores['ties']}")

def main():
    print("Welcome to Rock-Paper-Scissors with Score Tracking!")

    scores = {'player': 0, 'computer': 0, 'ties': 0}
    
    while True:
        while True:
            player_choice = input("\nEnter your choice (rock, paper, or scissors): ").strip().lower()
            
            if player_choice not in ['rock', 'paper', 'scissors']:
                print("Invalid choice, please choose rock, paper, or scissors.")
                continue
            
            computer_choice = get_computer_choice()
            print(f"Computer chose: {computer_choice}")
            
            result = determine_winner(player_choice, computer_choice)
            
            if result == "win":
                print("You win!")
                scores['player'] += 1
            elif result == "lose":
                print("You lose!")
                scores['computer'] += 1
            else:
                print("It's a tie!")
                scores['ties'] += 1
            
            print_scores(scores)
            
            play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
            if play_again != 'yes':
                break
        
        play_again_game = input("\nDo you want to play a new game? (yes/no): ").strip().lower()
        if play_again_game != 'yes':
            print("Thanks for playing!")
            break
        else:
            # Reset scores for a new game
            scores = {'player': 0, 'computer': 0, 'ties': 0}

if __name__ == "__main__":
    main()
