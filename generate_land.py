import random
from termcolor import colored
from noise import pnoise2

def generate_land(cols=10, rows=10, noise_level=10): 
    data = ["🌳", "🌲", "🍄", "🌻", "🏠", "🍀", "🏠", "🌻", "🍄", "🌲", "🌳"]
    seed = random.randint(0, 100)
    land = ""

    print(f"Generate a landscape which is {cols} by {rows}.")

    for row in range(rows):
        for col in range(cols): 
            n = pnoise2(row / rows, col / cols, base=seed, octaves=5)
            n *= noise_level
            n = round(n)
            n = n % len(data)
            land += data[n]
        land += "\n"

    print("Finished generating landscape")
    return land

def ask_for_number(question): 
    tries = 0
    while tries < 3:
        answer = input(colored(question + "\n", "green"))
        if answer.isnumeric():
            return int(answer)
        elif answer == "quit":
            quit()
        else:
            tries += 1
            print(colored("Ooops, this didn't make sense", "yellow"))

    print(colored("Huh, this isn't fun any more...", "red"))     
    quit()

if __name__ == "__main__":
    rows = ask_for_number("how many rows? ")
    columns = ask_for_number("how many columns? ")
    output = generate_land(columns, rows)
    print(output)