import json

def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)

def generate_animals_html(data):
    """Generate basic HTML list items"""
    output = ""
    for animal in data:
        name = animal.get("name")
        diet = animal.get("characteristics", {}).get("diet")
        locations = animal.get("locations")
        type_ = animal.get("characteristics", {}).get("type")

        output += '<li class="cards__item">\n'
        if name:
            output += f"Name: {name}<br/>\n"
        if diet:
            output += f"Diet: {diet}<br/>\n"
        if locations:
            output += f"Location: {locations[0]}<br/>\n"
        if type_:
            output += f"Type: {type_}<br/>\n"
        output += "</li>\n\n"
    return output

def main():
    data = load_data("animals_data.json")

    with open("animals_template.html", "r") as file:
        template = file.read()

    animals_html = generate_animals_html(data)
    new_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    with open("animals.html", "w") as file:
        file.write(new_html)

if __name__ == "__main__":
    main()
