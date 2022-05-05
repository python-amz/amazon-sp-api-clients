"""
Selling Partner API for Shipment Invoicing
=============================================================================================
The Selling Partner API for Shipment Invoicing helps you programmatically retrieve shipment invoice information in the Brazil marketplace for a selling partner¡¯s Fulfillment by Amazon (FBA) orders.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: v0
"""
from ..utils.base_client import BaseClient


class ShipmentInvoicingV0Client(BaseClient):
    def get_shipment_details(
        self,
        # name='shipmentId' param_in='path' description='The identifier for the shipment. Get this value from the FBAOutboundShipmentStatus notification. For information about subscribing to notifications, see the [Notifications API Use Case Guide](doc:notifications-api-v1-use-case-guide).' required=True deprecated=False allowEmptyValue=False style=None explode=False allowReserved=False param_schema=Schema(allOf=None, anyOf=None, oneOf=None, schema_not=None, schema_if=None, then=None, schema_else=None, dependentSchemas=None, prefixItems=None, items=None, contains=None, properties=None, patternProperties=None, additionalProperties=None, propertyNames=None, unevaluatedItems=None, unevaluatedProperties=None, type='string', enum=None, const=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxContains=None, minContains=None, maxProperties=None, minProperties=None, required=None, dependentRequired=None, schema_format=None, contentEncoding=None, contentMediaType=None, contentSchema=None, title=None, description=None, default=None, deprecated=None, readOnly=None, writeOnly=None, examples=None, discriminator=None, xml=None, externalDocs=None, example=None) example=None examples=None content=None
    ):
        url = "/fba/outbound/brazil/v0/shipments/{shipmentId}"

    def submit_invoice(
        self,
        # name='shipmentId' param_in='path' description='The identifier for the shipment.' required=True deprecated=False allowEmptyValue=False style=None explode=False allowReserved=False param_schema=Schema(allOf=None, anyOf=None, oneOf=None, schema_not=None, schema_if=None, then=None, schema_else=None, dependentSchemas=None, prefixItems=None, items=None, contains=None, properties=None, patternProperties=None, additionalProperties=None, propertyNames=None, unevaluatedItems=None, unevaluatedProperties=None, type='string', enum=None, const=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxContains=None, minContains=None, maxProperties=None, minProperties=None, required=None, dependentRequired=None, schema_format=None, contentEncoding=None, contentMediaType=None, contentSchema=None, title=None, description=None, default=None, deprecated=None, readOnly=None, writeOnly=None, examples=None, discriminator=None, xml=None, externalDocs=None, example=None) example=None examples=None content=None
    ):
        url = "/fba/outbound/brazil/v0/shipments/{shipmentId}/invoice"

    def get_invoice_status(
        self,
        # name='shipmentId' param_in='path' description='The shipment identifier for the shipment.' required=True deprecated=False allowEmptyValue=False style=None explode=False allowReserved=False param_schema=Schema(allOf=None, anyOf=None, oneOf=None, schema_not=None, schema_if=None, then=None, schema_else=None, dependentSchemas=None, prefixItems=None, items=None, contains=None, properties=None, patternProperties=None, additionalProperties=None, propertyNames=None, unevaluatedItems=None, unevaluatedProperties=None, type='string', enum=None, const=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxContains=None, minContains=None, maxProperties=None, minProperties=None, required=None, dependentRequired=None, schema_format=None, contentEncoding=None, contentMediaType=None, contentSchema=None, title=None, description=None, default=None, deprecated=None, readOnly=None, writeOnly=None, examples=None, discriminator=None, xml=None, externalDocs=None, example=None) example=None examples=None content=None
    ):
        url = "/fba/outbound/brazil/v0/shipments/{shipmentId}/invoice/status"
