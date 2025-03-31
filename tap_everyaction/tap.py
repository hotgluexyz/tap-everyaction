"""EveryAction tap class."""

from __future__ import annotations
from typing import List

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_everyaction.client import EveryActionStream
from tap_everyaction.streams import ContactsStream

STREAM_TYPES = [
    ContactsStream,
]


class TapEveryAction(Tap):
    """EveryAction tap class."""

    name = "tap-everyaction"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "app_name",
            th.StringType,
            required=True,
            description="App name for authentication",
        ),
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            description="API key for authentication",
        ),
    ).to_dict()

    def discover_streams(self) -> List[EveryActionStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
    
    def sync_all(self) -> None:
        raise NotImplementedError("Sync all is not implemented")


if __name__ == "__main__":
    TapEveryAction.cli()
