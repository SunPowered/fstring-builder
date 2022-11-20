"""fstring_builder.fstring"""
from typing import Union

from .replacement_field import ReplacementField


class FormatString:
    """
    Main FormatString builder object.

    This collects strings and `ReplacementField` instances to construct a buildable format string
    """

    def __init__(self, *args: Union[str, ReplacementField]):
        """FString constructor.  Acceps a list of `str` or `ReplacementField` items"""
        self._items: list[Union[str, ReplacementField]] = list(args) or []

    def build(self, join_with: str = "") -> str:
        """
        Returns a format ready string from all stored items.

        Accepts an optional `join_with` argument expecting a string to join all elements
        """
        return join_with.join(
            item.build() if isinstance(item, ReplacementField) else item
            for item in self._items
        )

    def format(self, *args, **kwargs) -> str:
        """Build and format an FormatString"""
        return self.build().format(*args, **kwargs)

    def add(self, item: Union[str, ReplacementField]):
        """Add a new item to the FormatString"""
        self._items.append(item)
