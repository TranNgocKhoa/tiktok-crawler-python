# TikTok Crawler Python

This Python script utilizes the Apify API to fetch and print descriptions of trending TikTok videos, user videos, and hashtag videos.

## Setup

Before running the script, you need to obtain your APIFY key.

### Obtaining APIFY Key

1. Visit the [Apify Console](https://console.apify.com/).
2. Navigate to the **Integrations** tab.
3. Find your API token listed there.
4. Copy the token for use in the script.

### Initialization

Replace `'YOUR-APIFY-KEY'` with your actual APIFY key obtained from the Apify Console.

```python
apify_client = ApifyClient('YOUR-APIFY-KEY')
```

## Usage
The script can be used to fetch data for three different types of inputs: TREND, USER, and HASHTAG.

### Fetching Trend Data
To fetch trend data, define your `trend_data` dictionary with the desired parameters and pass it to the `InputSchema` class.

```python
trend_data = {
    "type": "TREND",
    "url": "",
    "region": "US",
    "limit": 20,
    "publishTime": "ALL_TIME",
    "proxyConfiguration": {
        "useApifyProxy": False
    }
}
trend_input = InputSchema(**trend_data)
```

### Fetching User Data
Similarly, to fetch user data, define your `user_data` dictionary.

```python
user_data = {
    "type": "USER",
    "url": "https://www.tiktok.com/@seuamigopitbull",
    "limit": 20,
    "proxyConfiguration": {
        "useApifyProxy": False
    }
}
user_input = InputSchema(**user_data)

```

### Fetching Hashtag Data
For hashtag data, define your `hashtag_data` dictionary.

```python
hashtag_data = {
    "type": "HASHTAG",
    "url": "https://tiktok.com/tag/fyp",
    "region": "US",
    "limit": 20,
    "proxyConfiguration": {
        "useApifyProxy": False
    }
}
hashtag_input = InputSchema(**hashtag_data)

```

### Running the Script
Run the script using the following command:

```shell
python tiktok_trend_fetcher.py
```

The script will print the descriptions of the videos fetched from the specified TREND, USER, and HASHTAG inputs.

## Note

Ensure that the `input_schema.py` file is present in the same directory as the script and contains the `InputSchema` class definition as per your project’s requirements.