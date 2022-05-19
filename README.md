# YamlParse
YamlParse is an alternative to the normal yaml parsers as it keeps all symbols and characters.

The reason for creating this is to build universal a GUI yaml editor mainly for <a href="https://github.com/home-assistant/core" target="_blank">homeassistant</a>

## Usage Example

```
from parse import YamlParse

my_yaml = [YAML]  # declare yaml text
Yaml = YamlParse(my_yaml)  # parse the yaml text
yaml_json = Yaml.data  

# change yaml_json as you want
new_parent = {
    'name': "dummy_heading",
    'children': [{
        'name': "child_1: steve",
        'children': [],
        'level': 2
    }],
    'level': 0
}

yaml_json['parents'].append(new_parent)  # add new heading to yaml

Yaml.set_data(yaml_json)  # pass the changes to Yaml

new_yaml = Yaml.dump()  # get the changed yaml text
```

