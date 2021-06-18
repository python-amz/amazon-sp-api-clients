"""
Rename this script to "client_config.py" to run testcases.
"""

import amazon_sp_api_clients

marketplace = amazon_sp_api_clients.MarketPlaces.get_by_index(105)

aws_access_key = 'XXXXXXXXXXXXXXXXXXXX'
aws_secret_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
role_arn = "arn:aws:iam::xxxxxxxxxxxx:role/xxxxxxxxxxx"
client_id = 'amzn1.sp.solution.xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
client_key = 'amzn1.application-oa2-client.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
client_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
refresh_token = "Atzr|xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
                "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
                "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
                "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

client_config = dict(
    role_arn=role_arn,
    endpoint=marketplace.endpoint,
    region=marketplace.region,
    marketplace_id=marketplace.market_place,
    refresh_token=refresh_token,
    aws_access_key=aws_access_key,
    aws_secret_key=aws_secret_key,
    lwa_client_key=client_key,
    lwa_client_secret=client_secret,
)
