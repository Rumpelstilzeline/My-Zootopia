import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')

# Zugrif auf 'name'
for animal in animals_data:
  print("Name:", animal["name"])
  characteristics = animal.get("characteristics", {})
  print("Diet:", characteristics.get("diet", "N/A"))
  print("Locations:")
  for location in animal["locations"]:
    print("   -", location)
  print()


animals_data = load_data('animals_data.json')
