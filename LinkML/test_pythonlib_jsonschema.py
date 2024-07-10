import json
import jsonschema
from jsonschema import validate

# Load the schema from a file
with open('draft-2019-09-schema.json', 'r') as schema_file:
    schema = json.load(schema_file)

with open('data_valid_sample.json', 'r') as data_file:
    data = json.load(data_file)

with open('overall_schema.json', 'r') as myschema_file:
    myschema = json.load(myschema_file)

# Validate the data
try:
    validate(instance=data, schema=myschema)
    print("Data is valid!")
except jsonschema.exceptions.ValidationError as err:
    print("Data is invalid:", err.message)