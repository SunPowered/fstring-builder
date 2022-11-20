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

        self._name = name
        self._conversion = conversion
        self._fill = fill
        self._align = align
        self._sign = sign
        self._z = z
        self._hashtag = hashtag
        self._zero = zero
        self._width = width
        self._grouping = grouping
        self._precision = precision
        self._type = type

    def name(self, name: str) -> "ReplacementField":
        """Chainable function to set the field `name`"""
        self._name = name
        return self

    def conversion(self, conversion: str) -> "ReplacementField":
        """Chainable function to set the field `conversion`"""
        self._conversion = conversion
        return self

    def fill(self, fill: str) -> "ReplacementField":
        """Chainable function to set the field `fill`"""
        self._fill = fill
        return self

    def align(self, align: str) -> "ReplacementField":
        """Chainable function to set the field `align`"""
        self._align = align
        return self

    def sign(self, sign: str) -> "ReplacementField":
        """Chainable function to set the field `sign`"""
        self._sign = sign
        return self

    def z(self, z: bool) -> "ReplacementField":
        """Chainable function to set the field `z`"""
        self._z = z
        return self

    def hashtag(self, hashtag: bool) -> "ReplacementField":
        """Chainable function to set the field `hashtag`"""
        self._hashtag = hashtag
        return self

    def zero(self, zero: bool) -> "ReplacementField":
        """Chainable function to set the field `zero`"""
        self._zero = zero
        return self

    def width(self, width: int) -> "ReplacementField":
        """Chainable function to set the field `width`"""
        self._width = width
        return self

    def grouping(self, grouping: str) -> "ReplacementField":
        """Chainable function to set the field `grouping`"""
        self._grouping = grouping
        return self

    def precision(self, precision: int) -> "ReplacementField":
        """Chainable function to set the field `precision`"""
        self._precision = precision
        return self

    def type(self, type: str) -> "ReplacementField":
        """Chainable function to set the field `type`"""
        self._type = type
        return self

    def build_format_spec(self) -> str:
        """Build the format spec field."""

        return f"{self._fill or ''}{self._align or ''}{self._sign or ''}{'z' if self._z else ''}{'#' if self._hashtag else ''}{'0' if self._zero else ''}{self._width or ''}{self._grouping or ''}{'.{}'.format(self._precision) if self._precision is not None else ''}{self._type or ''}"  # noqa: E501

    def build(self) -> str:
        """Build the format ready string"""

        format_spec = self.build_format_spec()
        format_spec = ":{}".format(format_spec) if format_spec else ""
        conversion = (
            "!{}".format(self._conversion) if self._conversion is not None else ""
        )

        return f"{{{self._name or ''}{conversion}{format_spec}}}"
