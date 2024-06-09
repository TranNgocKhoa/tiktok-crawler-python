from apify_client import ApifyClient

from input_schema import InputSchema

apify_client = ApifyClient('YOUR-APIFY-KEY')


def get_data_from_actor_call(request_input):
    trend_json = request_input.__dict__
    actor_call = apify_client.actor('novi/fast-tiktok-api').call(run_input=trend_json)
    dataset_client = apify_client.dataset(actor_call['defaultDatasetId'])

    return dataset_client.list_items().items


if __name__ == '__main__':
    trend_data = {
        "type": "TREND",
        "region": "US",
        "limit": 20,
        "publishTime": "ALL_TIME",
        # proxyConfiguration should not use proxy for better speed.
        "proxyConfiguration": {
            "useApifyProxy": False
        }
    }
    trend_input = InputSchema(**trend_data)

    # Print each video's description.
    for item in get_data_from_actor_call(trend_input):
        print(item["desc"])

    user_data = {
        "type": "USER",
        "url": "https://www.tiktok.com/@seuamigopitbull",
        "limit": 20,
        # proxyConfiguration should not use proxy for better speed.
        "proxyConfiguration": {
            "useApifyProxy": False
        }
    }
    user_input = InputSchema(**user_data)

    # Print each video's description.
    for item in get_data_from_actor_call(user_input):
        print(item["desc"])

    hashtag_data = {
        "type": "HASHTAG",
        "url": "https://tiktok.com/tag/fyp",
        "region": "US",
        "limit": 20,
        # proxyConfiguration should not use proxy for better speed.
        "proxyConfiguration": {
            "useApifyProxy": False
        }
    }
    hashtag_input = InputSchema(**hashtag_data)

    # Print each video's description.
    for item in get_data_from_actor_call(hashtag_input):
        print(item["desc"])
