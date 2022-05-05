"""
Selling Partner API for Vendor Direct Fulfillment Sandbox Test Data
=============================================================================================
The Selling Partner API for Vendor Direct Fulfillment Sandbox Test Data provides programmatic access to vendor direct fulfillment sandbox test data.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: 2021-10-28
"""
from ..utils.base_client import BaseClient


class VendorDirectFulfillmentSandboxTestData20211028Client(BaseClient):
    def generate_order_scenarios(
        self,
    ):
        url = "/vendor/directFulfillment/sandbox/2021-10-28/orders"

    def get_order_scenarios(
        self,
        # name='transactionId' param_in='path' description='The transaction identifier returned in the response to the generateOrderScenarios operation.' required=True deprecated=False allowEmptyValue=False style=None explode=False allowReserved=False param_schema=Schema(allOf=None, anyOf=None, oneOf=None, schema_not=None, schema_if=None, then=None, schema_else=None, dependentSchemas=None, prefixItems=None, items=None, contains=None, properties=None, patternProperties=None, additionalProperties=None, propertyNames=None, unevaluatedItems=None, unevaluatedProperties=None, type='string', enum=None, const=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxContains=None, minContains=None, maxProperties=None, minProperties=None, required=None, dependentRequired=None, schema_format=None, contentEncoding=None, contentMediaType=None, contentSchema=None, title=None, description=None, default=None, deprecated=None, readOnly=None, writeOnly=None, examples=None, discriminator=None, xml=None, externalDocs=None, example=None) example=None examples=None content=None
    ):
        url = "/vendor/directFulfillment/sandbox/2021-10-28/transactions/{transactionId}"
