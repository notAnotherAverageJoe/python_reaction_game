import time
import random

num_rounds = 5
min_delay_sec = 1
max_delay_sec = 5


def main():
    print("Welcome to Reaction Speed Game!")
    input("Press enter to start.....")

    score = 0 
    
    for round_num in range(1, num_rounds +1):
        print(f"Round {round_num}: Get ready...")
        delay_sec = random.uniform(min_delay_sec , max_delay_sec)
        time.sleep(delay_sec)

        print("Press Enter NOW!!!!!!!")
        start_time = time.time()
        input()


        reaction_time_sec = time.time() - start_time
        reaction_time_ms = reaction_time_sec * 1000
        print(f"Your reaction time: {reaction_time_ms: .2f} ms")

        #update score based on reaciton time
        if reaction_time_ms < 200:
            score +=3
        elif reaction_time_ms < 500:
            score +=2
        elif reaction_time_ms < 1000:
            score +=1
        
        print(f"Your score: {score}")

    print(f"Game OVER! Your final score is: {score}")

if __name__ == "__main__":
    main()