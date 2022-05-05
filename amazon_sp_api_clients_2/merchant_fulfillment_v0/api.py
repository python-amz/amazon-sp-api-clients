"""
Selling Partner API for Merchant Fulfillment
=============================================================================================
The Selling Partner API for Merchant Fulfillment helps you build applications that let sellers purchase shipping for non-Prime and Prime orders using Amazon¡¯s Buy Shipping Services.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: v0
"""
from ..utils.base_client import BaseClient


class MerchantFulfillmentV0Client(BaseClient):
    def get_eligible_shipment_services_old(
        self,
    ):
        url = "/mfn/v0/eligibleServices"

    def get_eligible_shipment_services(
        self,
    ):
        url = "/mfn/v0/eligibleShippingServices"

    def get_shipment(
        self,
        # name='shipmentId' param_in='path' description='The Amazon-defined shipment identifier for the shipment.' required=True deprecated=False allowEmptyValue=False style=None explode=False allowReserved=False param_schema=Schema(allOf=None, anyOf=None, oneOf=None, schema_not=None, schema_if=None, then=None, schema_else=None, dependentSchemas=None, prefixItems=None, items=None, contains=None, properties=None, patternProperties=None, additionalProperties=None, propertyNames=None, unevaluatedItems=None, unevaluatedProperties=None, type='string', enum=None, const=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern='[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}', maxItems=None, minItems=None, uniqueItems=None, maxContains=None, minContains=None, maxProperties=None, minProperties=None, required=None, dependentRequired=None, schema_format=None, contentEncoding=None, contentMediaType=None, contentSchema=None, title=None, description=None, default=None, deprecated=None, readOnly=None, writeOnly=None, examples=None, discriminator=None, xml=None, externalDocs=None, example=None) example=None examples=None content=None
    ):
        url = "/mfn/v0/shipments/{shipmentId}"

    def cancel_shipment(
        self,
        # name='shipmentId' param_in='path' description='The Amazon-defined shipment identifier for the shipment to cancel.' required=True deprecated=False allowEmptyValue=False style=None explode=False allowReserved=False param_schema=Schema(allOf=None, anyOf=None, oneOf=None, schema_not=None, schema_if=None, then=None, schema_else=None, dependentSchemas=None, prefixItems=None, items=None, contains=None, properties=None, patternProperties=None, additionalProperties=None, propertyNames=None, unevaluatedItems=None, unevaluatedProperties=None, type='string', enum=None, const=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern='[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}', maxItems=None, minItems=None, uniqueItems=None, maxContains=None, minContains=None, maxProperties=None, minProperties=None, required=None, dependentRequired=None, schema_format=None, contentEncoding=None, contentMediaType=None, contentSchema=None, title=None, description=None, default=None, deprecated=None, readOnly=None, writeOnly=None, examples=None, discriminator=None, xml=None, externalDocs=None, example=None) example=None examples=None content=None
    ):
        url = "/mfn/v0/shipments/{shipmentId}"

    def cancel_shipment_old(
        self,
        # name='shipmentId' param_in='path' description='The Amazon-defined shipment identifier for the shipment to cancel.' required=True deprecated=False allowEmptyValue=False style=None explode=False allowReserved=False param_schema=Schema(allOf=None, anyOf=None, oneOf=None, schema_not=None, schema_if=None, then=None, schema_else=None, dependentSchemas=None, prefixItems=None, items=None, contains=None, properties=None, patternProperties=None, additionalProperties=None, propertyNames=None, unevaluatedItems=None, unevaluatedProperties=None, type='string', enum=None, const=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern='[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}', maxItems=None, minItems=None, uniqueItems=None, maxContains=None, minContains=None, maxProperties=None, minProperties=None, required=None, dependentRequired=None, schema_format=None, contentEncoding=None, contentMediaType=None, contentSchema=None, title=None, description=None, default=None, deprecated=None, readOnly=None, writeOnly=None, examples=None, discriminator=None, xml=None, externalDocs=None, example=None) example=None examples=None content=None
    ):
        url = "/mfn/v0/shipments/{shipmentId}/cancel"

    def create_shipment(
        self,
    ):
        url = "/mfn/v0/shipments"

    def get_additional_seller_inputs_old(
        self,
    ):
        url = "/mfn/v0/sellerInputs"

    def get_additional_seller_inputs(
        self,
    ):
        url = "/mfn/v0/additionalSellerInputs"
