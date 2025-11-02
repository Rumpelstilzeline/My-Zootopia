import json

def load_data(file_path):
    """Load JSON data from a file."""
    with open(file_path, "r") as handle:
        return json.load(handle)

def serialize_animal(animal):
    """Serialize a single animal into HTML card."""
    name = animal.get("name", "Unknown")
    characteristics = animal.get("characteristics", {})
    
    # Fallbacks if a field is missing
    diet = characteristics.get("diet") or characteristics.get("main_prey") or "Unknown"
    type_ = characteristics.get("type") or characteristics.get("group") or "Unknown"
    locations = ", ".join(animal.get("locations", ["Unknown"]))
    slogan = characteristics.get("slogan", "")

    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{name}</div>\n'
    output += '  <p class="card__text">\n'
    output += f'      <strong>Diet:</strong> {diet}<br/>\n'
    output += f'      <strong>Type:</strong> {type_}<br/>\n'
    output += f'      <strong>Location:</strong> {locations}<br/>\n'
    if slogan:
        output += f'      <em>{slogan}</em>\n'
    output += '  </p>\n'
    output += '</li>\n\n'
    return output

def main():
    # Load JSON data
    data = load_data("animals_data.json")

    # Read HTML template
    with open("animals_template.html", "r") as file:
        template = file.read()

    # Generate HTML for all animals
    animals_html = ""
    for animal in data:
        animals_html += serialize_animal(animal)

    # Insert animals HTML into template
    new_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    # Write final HTML
    with open("animals.html", "w") as file:
        file.write(new_html)

    print("animals.html generated successfully!")

if __name__ == "__main__":
    main()
