"""
Selling Partner API for Product Fees
=============================================================================================
The Selling Partner API for Product Fees lets you programmatically retrieve estimated fees for a product. You can then account for those fees in your pricing.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: v0
"""
from ..utils.base_client import BaseClient


class ProductFeesV0Client(BaseClient):
    def get_my_fees_estimate_for_sku(
        self,
        # name='SellerSKU' param_in='path' description="Used to identify an item in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit." required=True deprecated=False allowEmptyValue=False style=None explode=False allowReserved=False param_schema=Schema(allOf=None, anyOf=None, oneOf=None, schema_not=None, schema_if=None, then=None, schema_else=None, dependentSchemas=None, prefixItems=None, items=None, contains=None, properties=None, patternProperties=None, additionalProperties=None, propertyNames=None, unevaluatedItems=None, unevaluatedProperties=None, type='string', enum=None, const=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxContains=None, minContains=None, maxProperties=None, minProperties=None, required=None, dependentRequired=None, schema_format=None, contentEncoding=None, contentMediaType=None, contentSchema=None, title=None, description=None, default=None, deprecated=None, readOnly=None, writeOnly=None, examples=None, discriminator=None, xml=None, externalDocs=None, example=None) example=None examples=None content=None
    ):
        url = "/products/fees/v0/listings/{SellerSKU}/feesEstimate"

    def get_my_fees_estimate_for_asin(
        self,
        # name='Asin' param_in='path' description='The Amazon Standard Identification Number (ASIN) of the item.' required=True deprecated=False allowEmptyValue=False style=None explode=False allowReserved=False param_schema=Schema(allOf=None, anyOf=None, oneOf=None, schema_not=None, schema_if=None, then=None, schema_else=None, dependentSchemas=None, prefixItems=None, items=None, contains=None, properties=None, patternProperties=None, additionalProperties=None, propertyNames=None, unevaluatedItems=None, unevaluatedProperties=None, type='string', enum=None, const=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxContains=None, minContains=None, maxProperties=None, minProperties=None, required=None, dependentRequired=None, schema_format=None, contentEncoding=None, contentMediaType=None, contentSchema=None, title=None, description=None, default=None, deprecated=None, readOnly=None, writeOnly=None, examples=None, discriminator=None, xml=None, externalDocs=None, example=None) example=None examples=None content=None
    ):
        url = "/products/fees/v0/items/{Asin}/feesEstimate"
