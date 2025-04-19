import json
import pkg_resources
from jsonschema import validate, ValidationError

def load_schema(schema_path=None):
    if schema_path is None:
        schema_path = pkg_resources.resource_filename(
            __name__, "schema/kivai-command.schema.json"
        )
    with open(schema_path, "r") as file:
        return json.load(file)

def validate_command(command: dict, schema_path=None) -> tuple[bool, str]:
    try:
        schema = load_schema(schema_path)
        validate(instance=command, schema=schema)
        return True, "✅ Command is valid!"
    except ValidationError as e:
        return False, f"❌ Validation failed: {e.message}"

