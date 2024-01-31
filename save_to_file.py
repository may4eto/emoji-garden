from generate_land import generate_land
import os

os.makedirs("outputs", exist_ok=True)

noise_levels = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for nl in noise_levels:
    output = generate_land(200, 200, nl)
    filename = os.path.join("outputs", f"noise-level-{nl}.txt")
    with open(filename, "w") as f:
        f.write(output)