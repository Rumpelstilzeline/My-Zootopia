import json

with open("animals_template.html", "r") as file:
  html_content = file.read()


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')

output = ''   # Empty string for animal data

for animal in animals_data:
  output += f"Name: {animal["name"]}\n"

  characteristics = animal.get("characteristics", {})
  diet_info = characteristics.get("diet", "N/A")
  output += f"Diet: {diet_info}\n"


  output += "Locations:\n"
  for location in animal["locations"]:
    output += f"   - {location}\n"

  if "type" in characteristics:
    output += f"Type:, {characteristics["type"]}\n"


# Inside the html_content, the old string is replaced by the ouput genereated here
html_output = html_content.replace("__REPLACE_ANIMALS_INFO__", output)


with open("animals.html", "w") as output_file:
  output_file.write(html_output)