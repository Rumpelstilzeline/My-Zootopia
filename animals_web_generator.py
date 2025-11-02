import json

def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)

def generate_animals_text(data):
    """Creates plain text output for HTML insertion"""
    output = ""
    for animal in data:
        name = animal.get("name")
        diet = animal.get("characteristics", {}).get("diet")
        locations = animal.get("locations")
        type_ = animal.get("characteristics", {}).get("type")

        if name:
            output += f"Name: {name}\n"
        if diet:
            output += f"Diet: {diet}\n"
        if locations:
            output += f"Location: {locations[0]}\n"
        if type_:
            output += f"Type: {type_}\n"
        output += "\n"
    return output

def main():
    data = load_data("animals_data.json")

    with open("animals_template.html", "r") as file:
        template = file.read()

    animals_output = generate_animals_text(data)
    new_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_output)

    with open("animals.html", "w") as file:
        file.write(new_html)

if __name__ == "__main__":
    main()

