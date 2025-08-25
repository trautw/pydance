import yaml
import json
import sys

def read_yaml(yaml_file: str) -> str:
    with open(yaml_file, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data

def yaml_to_json(yaml_file: str) -> str:
    # YAML-Datei einlesen
    with open(yaml_file, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    # In JSON umwandeln und zurückgeben (mit schöner Formatierung)
    return json.dumps(data, indent=4, ensure_ascii=False)

class Figure_list:
    def __init__(self, figure_name: str, anchor: dict):
        self.figure_name = figure_name
        self.anchor = anchor

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Bitte den Pfad zur YAML-Datei angeben.")
        print("Beispiel: python main.py dance.yaml")
        sys.exit(1)

    yaml_file = sys.argv[1]
    try:
        # json_output = yaml_to_json(yaml_file)
        # print(json_output)

        data = read_yaml(yaml_file)
        print(data['dance']['name'])
        print("Complex Figure:")
        print(data['dance']['complex_figure'])
        print()
        for complex_figure in data['dance']['complex_figure']:
            print(f"== Complex figure: {complex_figure['complex_figure_name']}")
            for figure_list in complex_figure['figure_list']:
                if figure_list['comment']:
                    print(f"Comment: {figure_list['comment']}")
                for list in figure_list['list']:
                    print(f"Figure Name: {list['figure_name']}")
                    flist = Figure_list(list['figure_name'], list['anchor'])
                    print(f"Figure List Object: {flist.figure_name}, Anchor: {flist.anchor}")
                # print(f"Figure List: {figure_list}")
                print()

    except Exception as e:
        print(f"Fehler beim Konvertieren: {e}")
