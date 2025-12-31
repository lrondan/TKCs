import json
import random

def main(value):
    index = random.randint(0, 232)
    with open('fakeid/USA_F_ID.json', 'r') as file:
        data = json.load(file)
        fake_id = data[index]
        print("Generated Fake ID:")
        for key, value in fake_id.items():
            print(f"{key}: {value}")
    return value

if __name__ == "__main__":
    main(value=None)