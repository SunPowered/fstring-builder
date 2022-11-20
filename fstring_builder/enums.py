"""fstring_builder.enums"""

from enum import Enum

__all__ = ["Conversion", "Align", "Sign", "Grouping", "Type"]

# https://docs.python.org/3/library/string.html?highlight=string%20format#format-string-syntax


class Conversion(Enum):
    STRING = "s"
    REPR = "r"
    ASCII = "a"


# https://docs.python.org/3/library/string.html?highlight=string%20format#format-specification-mini-language


class Align(Enum):
    # https://docs.python.org/3/library/string.html?highlight=string%20format#grammar-token-format-spec-align
    LEFT = "<"
    RIGHT = ">"
    CENTER = "^"
    NUMERIC = "="


class Sign(Enum):
    # https://docs.python.org/3/library/string.html?highlight=string%20format#grammar-token-format-spec-sign
    PLUS = "+"
    MINUS = "-"
    SPACE = " "


class Grouping(Enum):
    # https://docs.python.org/3/library/string.html?highlight=string%20format#grammar-token-format-spec-grouping_option
    COMMA = ","
    UNDERSCORE = "_"


class Type(Enum):
    # https://docs.python.org/3/library/string.html?highlight=string%20format#grammar-token-format-spec-type
    # String Types
    STRING = "s"

    # Integer Types
    BINARY = "b"
    CHARACTER = "c"
    DECIMAL = "d"
    OCTAL = "o"
    HEX = "x"
    HEX_UPPER = "X"
    NUMBER = "n"

    # Float Types
    SCIENTIFIC = "e"
    SCIENTIFIC_UPPER = "E"
    FIXED_POINT = "f"
    FIXED_POINT_UPPER = "F"
    GENERAL = "g"
    GENERAL_UPPER = "G"
    PERCENTAGE = "%"
