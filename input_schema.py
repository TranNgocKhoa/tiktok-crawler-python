from typing import Optional, Dict


class InputSchema:
    """
    Represents a Trend object.

    Attributes:
        type (str): The type of the trend.
        url (str): The URL associated with the trend.
        region (str): The region where the trend is popular.
        keyword (str): The keyword for the trend.
        urls (list): A list of URLs related to the trend.
        limit (int): The limit on the number of results.
        isUnlimited (bool): Flag to indicate if the results are unlimited.
        publishTime (str): The time period for the trend's publication.
        proxyConfiguration (dict): The configuration for the proxy.
    """

    def __init__(self,
                 type,
                 url: Optional[str] = None,
                 region: Optional[str] = None,
                 keyword: Optional[str] = None,
                 urls: Optional[str] = None,
                 limit: Optional[str] = 20,
                 isUnlimited: Optional[bool] = False,
                 publishTime: Optional[str] = "ALL_TIME",
                 proxyConfiguration = {
                     "useApifyProxy": False
                 }):
        """
        Constructs all the necessary attributes for the Trend object.

        Parameters:
            type (str): The type of the trend.
            url (str): The URL associated with the trend.
            region (str): The region where the trend is popular.
            keyword (str): The keyword for the trend.
            urls (list): A list of URLs related to the trend.
            limit (int): The limit on the number of results.
            isUnlimited (bool): Flag to indicate if the results are unlimited.
            publishTime (str): The time period for the trend's publication.
            proxyConfiguration (dict): The configuration for the proxy.
        """
        self.type = type
        self.url = url
        self.region = region
        self.keyword = keyword
        self.urls = urls
        self.limit = limit
        self.isUnlimited = isUnlimited
        self.publishTime = publishTime
        self.proxyConfiguration = proxyConfiguration

# Example usage:
# trend_data = {
#     "type": "TREND",
#     "url": "",
#     "region": "US",
#     "keyword": "viral",
#     "urls": [
#         "https://www.tiktok.com/@seuamigopitbull/video/7137451371405561093"
#     ],
#     "limit": 20,
#     "isUnlimited": False,
#     "publishTime": "ALL_TIME",
#     "proxyConfiguration": {
#         "useApifyProxy": False
#     }
# }
#
# trend_object = InputSchema(**trend_data)
