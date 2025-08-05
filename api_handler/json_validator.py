from jsonschema import validate, ValidationError
import json
import os

def load_schema(schema_file):
    path = os.path.join("schemas", schema_file)
    with open(path, 'r') as f:
        return json.load(f)

def validate_response(response_json, schema_file):
    schema = load_schema(schema_file)
    try:
        validate(instance=response_json, schema=schema)
        print(f"Schema validation passed: {schema_file}")
        return True
    except ValidationError as e:
        print(f"Schema validation failed: {e.message}")
        return False
