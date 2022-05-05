"""
Selling Partner API for Uploads
=============================================================================================

The Uploads API lets you upload files that you can programmatically access using other Selling Partner APIs, such as the A+ Content API and the Messaging API.
API Version: 2020-11-01
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class Uploads20201101Client(BaseClient):
    def create_upload_destination_for_resource(
        self,
        marketplace_ids: list[str],
        content_md5: str,
        resource: str,
        content_type: str = None,
    ):
        """
        Creates an upload destination, returning the information required to upload a file to the destination and to programmatically access the file.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | .1 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            marketplace_ids: A list of marketplace identifiers. This specifies the marketplaces where the upload will be available. Only one marketplace can be specified.
            content_md5: An MD5 hash of the content to be submitted to the upload destination. This value is used to determine if the data has been corrupted or tampered with during transit.
            resource: The resource for the upload destination that you are creating. For example, if you are creating an upload destination for the createLegalDisclosure operation of the Messaging API, the {resource} would be /messaging/v1/orders/{amazonOrderId}/messages/legalDisclosure, and the entire path would be /uploads/2020-11-01/uploadDestinations/messaging/v1/orders/{amazonOrderId}/messages/legalDisclosure.
            content_type: The content type of the file to be uploaded.
        """
        url = "/uploads/2020-11-01/uploadDestinations/{resource}"
        values = (
            marketplace_ids,
            content_md5,
            resource,
            content_type,
        )
        response = self._parse_args_and_request(
            url, "POST", values, self._create_upload_destination_for_resource_params
        )
        return response

    _create_upload_destination_for_resource_params = (  # name, param in
        ("marketplaceIds", "query"),
        ("contentMD5", "query"),
        ("resource", "path"),
        ("contentType", "query"),
    )
