"""fstring_builder.fstring_field"""
from typing import Optional, Union, TypeVar

from .enums import Conversion, Sign, Align, Grouping, Type

TField = TypeVar("TField", bound="ReplacementField")


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
        conversion: Optional[Union[str, Conversion]] = None,
        fill: Optional[str] = None,
        align: Optional[Union[str, Align]] = None,
        sign: Optional[Union[str, Sign]] = None,
        z: bool = False,
        hashtag: bool = False,
        zero: bool = False,
        width: Optional[int] = None,
        grouping: Optional[Union[str, Grouping]] = None,
        precision: Optional[int] = None,
        type: Optional[Union[str, Type]] = None,
    ):
        """Replacement Field constructor.  Pass in formatting options here, if available"""

        self._name: Optional[str] = name
        self._conversion: Optional[Conversion] = (
            Conversion(conversion) if conversion else None
        )
        self._fill: Optional[str] = fill
        self._align: Optional[Align] = Align(align) if align else None
        self._sign: Optional[Sign] = Sign(sign) if sign else None
        self._z: bool = z
        self._hashtag: bool = hashtag
        self._zero: bool = zero
        self._width: Optional[int] = width
        self._grouping: Optional[Grouping] = Grouping(grouping) if grouping else None
        self._precision: Optional[int] = precision
        self._type: Optional[Type] = Type(type) if type else None

    def name(self: TField, name: str) -> TField:
        """Chainable function to set the field `name`"""
        self._name = name
        return self

    def conversion(self: TField, conversion: Union[str, Conversion]) -> TField:
        """Chainable function to set the field `conversion`"""

        self._conversion = Conversion(conversion)
        return self

    def fill(self: TField, fill: str) -> TField:
        """Chainable function to set the field `fill`"""
        self._fill = fill
        return self

    def align(self: TField, align: Union[str, Align]) -> TField:
        """Chainable function to set the field `align`"""
        self._align = Align(align)
        return self

    def sign(self: TField, sign: Union[str, Sign]) -> TField:
        """Chainable function to set the field `sign`"""
        self._sign = Sign(sign)
        return self

    def z(self: TField, z: bool = True) -> TField:
        """Chainable function to set the field `z`"""
        self._z = z
        return self

    def hashtag(self: TField, hashtag: bool = True) -> TField:
        """Chainable function to set the field `hashtag`"""
        self._hashtag = hashtag
        return self

    def zero(self: TField, zero: bool = True) -> TField:
        """Chainable function to set the field `zero`"""
        self._zero = zero
        return self

    def width(self: TField, width: int) -> TField:
        """Chainable function to set the field `width`"""
        self._width = width
        return self

    def grouping(self: TField, grouping: Union[str, Grouping]) -> TField:
        """Chainable function to set the field `grouping`"""
        self._grouping = Grouping(grouping)
        return self

    def precision(self: TField, precision: int) -> TField:
        """Chainable function to set the field `precision`"""
        self._precision = precision
        return self

    def type(self: TField, type: Union[str, Type]) -> TField:
        """Chainable function to set the field `type`"""
        self._type = Type(type)
        return self

    def build_format_spec(self) -> str:
        """Build the format spec field."""

        return f"{self._fill or ''}{self._align.value if self._align else ''}{self._sign.value if self._sign else ''}{'z' if self._z else ''}{'#' if self._hashtag else ''}{'0' if self._zero else ''}{self._width or ''}{self._grouping.value if self._grouping else ''}{'.{}'.format(self._precision) if self._precision is not None else ''}{self._type.value if self._type else ''}"  # noqa: E501

    def build(self) -> str:
        """Build the format ready string"""

        format_spec = self.build_format_spec()
        format_spec = ":{}".format(format_spec) if format_spec else ""
        conversion = (
            "!{}".format(self._conversion.value) if self._conversion is not None else ""
        )

        return f"{{{self._name or ''}{conversion}{format_spec}}}"
