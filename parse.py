
class yamlParse:
    def __cleanup(self, yaml_string):
        out_yaml = ""
        for line in yaml_string.split("\n"):
            if not line.isspace():
                out_yaml += line + "\n"
        return out_yaml
            
    def __is_sub_key(self, line):
        if line.startswith(' '):
            level = 0
            for char in line:
                if not char == " ":
                    break
                level += 1
            return True, level
        else:
            return False, 0

    def set_data(self, json_data):
        self.data = json_data

    def __init__(self, yaml_string):
        self.yaml_string = self.__cleanup(yaml_string)
        self.data = {
            "parents": [],
        }
        current_parent = ""
        for line in self.yaml_string.split("\n"):
            if not line.startswith("#"):
                sub_key, level = self.__is_sub_key(line)
                if sub_key:
                    for parent in self.data["parents"]:
                        if parent['name'] == current_parent:
                            parent['children'].append({
                                'name': line.replace("  ", "", int(level)),
                                'children': [],
                                'level': level
                            })
                            break
                        for child in parent['children']:
                            if child['name'] == current_parent:
                                child['children'].append({
                                    'name': line.replace("  ", "", int(level)),
                                    'children': [],
                                    'level': level
                                })
                                break
                else:
                    self.data['parents'].append({"name": line, 'children': [], 'level': level})
                    current_parent = line

    def dump(self):
        outString = ""
        for item in self.data['parents']:
            outString += f"{item['name']}\n"
            for child in item['children']:
                outString += f"{' '*child['level']}{child['name']}\n"
        return outString
