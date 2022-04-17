import json
from pathlib import Path

from openapi_schema_pydantic.v3.v3_0_3 import OpenAPI

for i in (Path(__file__).parent.parent / 'swagger3_apis').glob('*.json'):
    with open(i) as f:
        data = json.load(f)
    result = OpenAPI.validate(data)
    data = OpenAPI.parse_obj(data)
    print(data.info.title)
