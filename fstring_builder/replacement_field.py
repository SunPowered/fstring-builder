"""fstring_builder.fstring_field"""
from typing import Optional


class ReplacementField:
    """
    Format String Replacement Field

    This represents a unit of format in an f-string, ie something defined inside curly parentheses, {}.

    It is a simple container that allows for a state of formatted fields to be stored and modified and eventually built into
    a format-ready string.

    See: https://docs.python.org/3/library/string.html?highlight=string%20format#format-specification-mini-language
    """

    def __init__(
        self,
        name: Optional[str] = None,
        conversion: Optional[str] = None,
        fill: Optional[str] = None,
        align: Optional[str] = None,
        sign: Optional[str] = None,
        z: Optional[bool] = None,
        hashtag: Optional[bool] = None,
        zero: Optional[bool] = None,
        width: Optional[int] = None,
        grouping: Optional[str] = None,
        precision: Optional[int] = None,
        type: Optional[str] = None,
    ):
        """Replacement Field constructor.  Pass in formatting options here, if available"""

        self.name = name
        self.conversion = conversion
        self.fill = fill
        self.align = align
        self.sign = sign
        self.z = z
        self.hashtag = hashtag
        self.zero = zero
        self.width = width
        self.grouping = grouping
        self.precision = precision
        self.type = type

    def build_format_spec(self) -> str:
        """Build the format spec field."""

        return f"{self.fill or ''}{self.align or ''}{self.sign or ''}{'z' if self.z else ''}{'#' if self.hashtag else ''}{'0' if self.zero else ''}{self.width or ''}{self.grouping or ''}{'.{}'.format(self.precision) if self.precision is not None else ''}{self.type or ''}"  # noqa: E501

    def build(self) -> str:
        """Build the format ready string"""

        format_spec = self.build_format_spec()
        format_spec = ":{}".format(format_spec) if format_spec else ""
        conversion = (
            "!{}".format(self.conversion) if self.conversion is not None else ""
        )

        return f"{{{self.name or ''}{conversion}{format_spec}}}"
