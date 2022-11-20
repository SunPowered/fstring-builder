import pytest

from fstring_builder.fstring import FormatString
from fstring_builder.replacement_field import ReplacementField


@pytest.fixture()
def currency():
    return ReplacementField(
        name="qty", align=">", fill="_", grouping=",", width=15, precision=2, type="f"
    )


def test_format_string(currency):

    expected = "${qty:_>15,.2f}"
    fstr = FormatString("$", currency)

    assert fstr.build() == expected

    val = 13523.5
    assert fstr.format(qty=val) == "$______13,523.50"

    fstr.add("| _column_ ")

    assert fstr.format(qty=val) == "$______13,523.50| _column_ "
