import json
import random
import pandas as pd

def main(value):
    index = random.randint(0, 999)
    with open('fakeid/UK_F_ID.json', 'r', encoding="utf-8") as file:
        data = json.load(file)
        df = pd.DataFrame.from_dict(data, orient="index").T
        df["id"] = pd.to_numeric(df["id"])
        value = df.iloc[index].to_dict()
        print("\nGenerated Fake ID:\n")
        #print(value)
        print(f"ID: {value['id']}")
        print(f"First Name: {value['first_name']}")
        print(f"Last Name: {value['last_name']}")
        print(f"Gender: {value['gender']}")
        print(f"dates_of_birth: {value['dates_of_birth']}")
        print(f"gmail: {value['gmail']}")
        print(f"address: {value['address']}")
        print(f"phone_number: {value['phone_number']}")
        print(f"education_level: {value['education_level']}")
        print(f"city: {value['city']}")
        print(f"country: {value['country']}\n")
    return value

if __name__ == "__main__":
    main(value=None)