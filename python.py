import random

def generate_password():
    return random.sample(range(1, 7), 4)

def get_feedback(password, guess):
    """Provide feedback on the guess compared to the password."""
    correct_position = sum(p == g for p, g in zip(password, guess))
    correct_number = sum(min(password.count(x), guess.count(x)) for x in set(guess)) - correct_position
    return correct_position, correct_number

def filter_combinations(combinations, guess, feedback):
    """Filter the possible combinations based on the feedback."""
    return [combo for combo in combinations if get_feedback(combo, guess) == feedback]

def play_game():
    all_combinations = [list(combo) for combo in generate_all_combinations()]
    attempts = 8

    print("Welcome to the Mastermind game!")
    print("The computer will guess a 4-digit password with unique numbers from 1 to 6.")
    print(f"You have {attempts} attempts to provide feedback. Good luck!\n")

    for attempt in range(1, attempts + 1):
        guess = random.choice(all_combinations)
        print(f"Attempt {attempt}: Computer's guess: {''.join(map(str, guess))}")

        while True:
            try:
                feedback = input("Enter feedback (x y): ").split()
                x, y = int(feedback[0]), int(feedback[1])
                if x < 0 or y < 0 or x + y > 4:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter two non-negative integers separated by a space, where their sum does not exceed 4.")

        if x == 4:
            print(f"Computer cracked the password {''.join(map(str, guess))} in {attempt} attempts!")
            return

        all_combinations = filter_combinations(all_combinations, guess, (x, y))

        

    print("Computer failed to crack the password within 8 attempts.")
def generate_all_combinations():
    combinations = []
    for i in range(1, 7):
        for j in range(1, 7):
            if j == i:
                continue
            for k in range(1, 7):
                if k == i or k == j:
                    continue
                for l in range(1, 7):
                    if l == i or l == j or l == k:
                        continue
                    combinations.append((i, j, k, l))
    return combinations
play_game()