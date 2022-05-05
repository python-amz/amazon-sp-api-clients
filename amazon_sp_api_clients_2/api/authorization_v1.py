"""
Selling Partner API for Authorization
=============================================================================================

The Selling Partner API for Authorization helps developers manage authorizations and check the specific permissions associated with a given authorization.
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs

from ..utils.base_client import BaseClient


@attrs.define
class AuthorizationCode:
    authorization_code: str = attrs.field()

    pass


@attrs.define
class Error:
    code: str = attrs.field()
    details: str = attrs.field()
    message: str = attrs.field()

    pass


@attrs.define
class ErrorList:
    pass


@attrs.define
class GetAuthorizationCodeResponse:
    errors: "ErrorList" = attrs.field()
    payload: "AuthorizationCode" = attrs.field()
    pass


class AuthorizationV1Client(BaseClient):
    def get_authorization_code(
            self,
            selling_partner_id: str,
            developer_id: str,
            mws_auth_token: str,
    ):
        """
        With the getAuthorizationCode operation, you can request a Login With Amazon (LWA) authorization code that will allow you to call a Selling Partner API on behalf of a seller who has already authorized you to call Amazon Marketplace Web Service (Amazon MWS). You specify a developer ID, an MWS auth token, and a seller ID. Taken together, these represent the Amazon MWS authorization that the seller previously granted you. The operation returns an LWA authorization code that can be exchanged for a refresh token and access token representing authorization to call the Selling Partner API on the seller's behalf. By using this API, sellers who have already authorized you for Amazon MWS do not need to re-authorize you for the Selling Partner API.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            selling_partner_id: The seller ID of the seller for whom you are requesting Selling Partner API authorization. This must be the seller ID of the seller who authorized your application on the Marketplace Appstore.
            developer_id: Your developer ID. This must be one of the developer ID values that you provided when you registered your application in Developer Central.
            mws_auth_token: The MWS Auth Token that was generated when the seller authorized your application on the Marketplace Appstore.
        """
        url = "/authorization/v1/authorizationCode"
        values = (
            selling_partner_id,
            developer_id,
            mws_auth_token,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_authorization_code_params)
        return response

    _get_authorization_code_params = (  # name, param in
        ("sellingPartnerId", "query"),
        ("developerId", "query"),
        ("mwsAuthToken", "query"),
    )
