"""REST client handling, including EveryActionStream base class."""

from singer_sdk.streams import RESTStream

class EveryActionStream(RESTStream):
    """EveryAction stream class."""

    @property
    def url_base(self) -> str:
        return "https://api.securevan.com/v4"