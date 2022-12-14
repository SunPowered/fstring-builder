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


def test_format_string_own_types():
    """Make sure FormatString can accept other FormatStrings"""

    fstr1 = FormatString(
        "Item:", ReplacementField(name="item", type="d", width=13, zero=True)
    )

    fstr2 = FormatString("---", fstr1, "---")

    assert fstr2.format(item=42).startswith("---")


def test_format_string_concatenation():
    """Test the + operator with FormatStrings"""

    fstr1 = FormatString(
        "**", ReplacementField(name="first_name", fill="-", align=">", width=10)
    )
    fstr2 = FormatString(
        ReplacementField(name="last_name", align="<", width=15, fill="-"), "**"
    )

    fconcat = fstr1 + " " + fstr2

    assert isinstance(fconcat, FormatString)
    assert (
        fconcat.format(first_name="Fred", last_name="Rogers")
        == "**------Fred Rogers---------**"
    )
