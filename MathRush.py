import threading
import time
import random
import sys

def generate_random_formula(initial_n=None):

    operations = [
        lambda n: n * n + n,
        lambda n: n * n * n,
        lambda n: n ** 2 + n,
        lambda n: n ** 3 + n,
        lambda n: n ** 2 * n ** 2,
        lambda n: n ** 2 + n ** 2,
        lambda n: n * n - n,
        lambda n: n * n // n
    ]

    selected_op = random.choice(operations)
    if initial_n is None:
        initial_n = random.randint(1, 5)
    puzzles = []
    for n in range(initial_n, initial_n + 5):
        result = selected_op(n)
        puzzles.append(f"{n} + {n} = {result}") 
    expression = puzzles[4]
    parts = expression.split(" = ")
    i = parts[1]
    puzzles[-1] = f"{initial_n + 4} + {initial_n + 4} = ?"
    return puzzles, i
    
 

points = 0
level = 1
initial_n = None
previous_offset = 0  # Track previous difficulty level
input_received = threading.Event()


def get_input():
    global user_input
    user_input = input("Enter value of '?': ")
    input_received.set()

def countdown(seconds):
    for remaining in range(seconds, 0, -1):
        if input_received.is_set():
            break
        sys.stdout.write(f"\r Time left: {remaining:2d} seconds ")
        sys.stdout.flush()
        time.sleep(1)
    print()  # Move to next line after countdown



while True:
    difficulty_offset = (points // 10) * 5
    print(f" current level : {level}")
    if difficulty_offset > previous_offset:
        print(f" Moving to next level! Difficulty increased.")
        level +=1
        print(f" level : {level}")
        previous_offset = difficulty_offset  # Update tracker


    initial_n = random.randint(1 + difficulty_offset, 5 + difficulty_offset)

    puzzles, i = generate_random_formula(initial_n)

    for puzzle in puzzles:
        print(puzzle)

    input_received.clear()
    input_thread = threading.Thread(target=get_input)
    countdown_thread = threading.Thread(target=countdown, args=(30,))

    input_thread.start()
    countdown_thread.start()

    input_thread.join(30)

    if not input_received.is_set():
        print(f"\n Time's up! Game Over. Final Score: {points}")
        break

    if user_input.strip() == i:
        print("correct answer")
        points += 1
        print(f"points: {points}\n")
           
    else:
        print(f"wrong, correct answer is: {i}")
        print(f" Game Over. Final Score: {points}")
        break






