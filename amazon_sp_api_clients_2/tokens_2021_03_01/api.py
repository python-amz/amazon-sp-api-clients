"""
Selling Partner API for Tokens 
=============================================================================================
The Selling Partner API for Tokens provides a secure way to access a customer's PII (Personally Identifiable Information). You can call the Tokens API to get a Restricted Data Token (RDT) for one or more restricted resources that you specify. The RDT authorizes subsequent calls to restricted operations that correspond to the restricted resources that you specified.
For more information, see the [Tokens API Use Case Guide](doc:tokens-api-use-case-guide).
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: 2021-03-01
"""
from ..utils.base_client import BaseClient


class Tokens20210301Client(BaseClient):
    def create_restricted_data_token(
        self,
    ):
        url = "/tokens/2021-03-01/restrictedDataToken"
