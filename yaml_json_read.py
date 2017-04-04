import yaml
import json
from pprint import pprint as pp

with open("my_file.json") as f:
    jsonfile = json.load(f)

print "This is my json file:"    
pp(jsonfile)

with open("assignment_yaml.yml") as f:
    yamlfile = yaml.load(f)

print "this begins the yaml file"   
pp(yamlfile)
