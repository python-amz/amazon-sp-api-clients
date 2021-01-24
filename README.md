# amazon-sp-api-clients

This is a package generated from amazon selling partner open api models.

This package is for my personal usage, and may not be a good package,
but enough for myself.

## Features

* ready to use;
* provide code to generate clients, in case that amazon update models;
* type hint.

## Note

Because that this repo currently do not need community contribution,
and is mainly for my personal usage,
so I made this repo private.
You can download the client from pypi and use it free.
But if you want to generate a new client lib to support your business,
please contact and pay me and I will provide technical support. 

For technical support, please contact [panhaoyu.china@outlook.com](mailto:panhaoyu.china@outlook.com).


由于这个库目前不打算接受社区的协助，而且主要是用于我的个人使用，
因此我将这个库设置成了私有库。
您可以免费从pypi安装并使用这个库，
但是如果您想生成一个新的客户端以适应您的业务逻辑，
我可以为您提供付费技术支持。

商业合作请联系 [panhaoyu.china@outlook.com](mailto:panhaoyu.china@outlook.com)。

## Usage

For saving time, I just paste part of my test code here as a demo.

For better understanding, all the fields are the same length of actual fields,
and some readable information are kept.

```python
def test_api():
    from datetime import datetime
    import sp_api_clients
    endpoint = "https://sellingpartnerapi-eu.amazon.com"
    marketplace_id = "XXXXXXXXXXXXXX"

    refresh_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
                    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
                    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
                    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    order_pk = '123-1234567-1234567'
    role_arn = "arn:aws:iam::123456789012:role/xxxxxx"
    aws_access_key = 'XXXXXXXXXXXXXXXXXXXX'
    aws_secret_key = "XXXXX/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    client_id = 'amzn1.application-oa2-client.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    client_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    client_config = dict(
        role_arn=role_arn,
        endpoint=endpoint,
        marketplace_id=marketplace_id,
        refresh_token=refresh_token,
        aws_access_key=aws_access_key,
        aws_secret_key=aws_secret_key,
        lwa_client_key=client_id,
        lwa_client_secret=client_secret,
    )
    order_client = sp_api_clients.orders.OrdersClient(**client_config, use_cache=True)

    orders = order_client.getOrders(
        MarketplaceIds=[marketplace_id],
        CreatedAfter=datetime(2000, 1, 1).isoformat()).payload.Orders
    assert len(orders) > 0
    assert orders[0].AmazonOrderId == order_pk

```

## Configuration

The client configuration can be set both at the initiation and as environment variables.

* SP_API_ROLE_ARN
* SP_API_ENDPOINT
* SP_API_MARKETPLACE_ID
* SP_API_REFRESH_TOKEN
* SP_API_AWS_ACCESS_KEY
* SP_API_AWS_SECRET_KEY
* SP_API_LWA_CLIENT_KEY
* SP_API_LWA_CLIENT_SECRET

## Build

The client is generated in the following steps:

1. download amazon open api repository;
1. copy open api 2 json files from the amazon repository to a single directory;
1. convert open api 2 json files to open api 3 json files;
1. convert open api 3 json files to py clients.

The main script of generation is the `test_main` python file.

When convert open api to py clients,
I separated the process into 6 steps,
which are defined in the `swager_client_generator.stages` module.

If my build is not suitable for your demand,
or amazon api model updates but my build do not follow,
you can clone this repo, modify the `api.pyt` template and build it by yourself,
and please push a PR, thanks!

# Acknowledgement

The auth method is partially from
[python-amazon-sp-api](https://github.com/saleweaver/python-amazon-sp-api).

# Note

If this library helps you, please give me a star, thanks!

如果这个库对您有用，请为我点亮Star，谢谢！

商业合作请联系 [panhaoyu.china@outlook.com](mailto:panhaoyu.china@outlook.com)。
