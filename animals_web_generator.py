import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

def print_animal_info(data):
    """Prints name, diet, first location, and type if present"""
    for animal in data:
        name = animal.get("name")
        diet = animal.get("characteristics", {}).get("diet")
        locations = animal.get("locations")
        type_ = animal.get("characteristics", {}).get("type")

        if name:
            print(f"Name: {name}")
        if diet:
            print(f"Diet: {diet}")
        if locations:
            print(f"Location: {locations[0]}")
        if type_:
            print(f"Type: {type_}")
        print()  # Blank line between animals

def main():
    animals_data = load_data("animals_data.json")
    print_animal_info(animals_data)

if __name__ == "__main__":
    main()
