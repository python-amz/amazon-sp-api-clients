"""
Selling Partner API for Tokens 
=============================================================================================

The Selling Partner API for Tokens provides a secure way to access a customer's PII (Personally Identifiable Information). You can call the Tokens API to get a Restricted Data Token (RDT) for one or more restricted resources that you specify. The RDT authorizes subsequent calls to restricted operations that correspond to the restricted resources that you specified.

For more information, see the [Tokens API Use Case Guide](doc:tokens-api-use-case-guide).
API Version: 2021-03-01
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


@attrs.define
class CreateRestrictedDataTokenRequest:

    restricted_resources: list[dict[str, Any]]
    # {'type': 'array', 'generator': <__mp_main__.Generator object at 0x000002A8850FB160>, 'items': Reference(ref='#/components/schemas/RestrictedResource')}
    target_application: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000002A8850FB160>}

    pass


@attrs.define
class CreateRestrictedDataTokenResponse:

    expires_in: int
    # {'type': 'integer', 'generator': <__mp_main__.Generator object at 0x000002A8850FB160>}
    restricted_data_token: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000002A8850FB160>}

    pass


@attrs.define
class Error:

    code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000002A8850FB160>}
    details: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000002A8850FB160>}
    message: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000002A8850FB160>}

    pass


@attrs.define
class ErrorList:

    errors: list[dict[str, Any]]
    # {'type': 'array', 'generator': <__mp_main__.Generator object at 0x000002A8850FB160>, 'items': Reference(ref='#/components/schemas/Error')}

    pass


@attrs.define
class RestrictedResource:

    data_elements: list[str]
    # {'type': 'array', 'generator': <__mp_main__.Generator object at 0x000002A8850FB160>, 'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None)}
    method: Union[Literal["GET"], Literal["PUT"], Literal["POST"], Literal["DELETE"]]
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000002A8850FB160>, 'enum': ['GET', 'PUT', 'POST', 'DELETE']}
    path: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000002A8850FB160>}

    pass


class Tokens20210301Client(BaseClient):
    def create_restricted_data_token(
        self,
    ):
        """
        Returns a Restricted Data Token (RDT) for one or more restricted resources that you specify. A restricted resource is the HTTP method and path from a restricted operation that returns Personally Identifiable Information (PII), plus a dataElements value that indicates the type of PII requested. See the Tokens API Use Case Guide for a list of restricted operations. Use the RDT returned here as the access token in subsequent calls to the corresponding restricted operations.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 1 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/tokens/2021-03-01/restrictedDataToken"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._create_restricted_data_token_params)
        return response

    _create_restricted_data_token_params = ()  # name, param in
