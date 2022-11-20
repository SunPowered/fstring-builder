import pytest
from fstring_builder.replacement_field import ReplacementField
from fstring_builder.enums import *


def test_replacement_field_constructor():
    """Pass valid arguments to the constructor and check the result"""
    expected = "{qty:>10,.2f}"
    rfield = ReplacementField(
        name="qty", align=">", width=10, grouping=",", precision=2, type="f"
    )

    assert rfield.build() == expected


def test_replacement_field_bad_params():
    """Not all parameters are allowed at the same time, expect a formatting `ValueError` on build"""

    # Fill but no align
    rfield = ReplacementField(name="value", fill="*", type="d")

    fstr = rfield.build()
    with pytest.raises(ValueError):

        fstr.format(value=313)


def test_field_enhanced_api():
    """Use the chaining methods to alter a replacement field"""

    # Want to support parameter passing by init arguments and chainable methods
    expected = "{:>20,.2f}"
    rfield = ReplacementField(type="f", precision=2)

    rfield.width(20).align(">").grouping(",")

    fstr = rfield.build()
    assert fstr == expected

    assert len(fstr.format(14312)) == 20


def test_fields_from_enums():
    """Assign Enum values to the set methods and ensure it builds"""
    expected = "{:>015,}"
    rfield = (
        ReplacementField()
        .align(Align.RIGHT)
        .zero(True)
        .width(15)
        .grouping(Grouping.COMMA)
    )

    assert rfield.build() == expected


def test_fields_for_coverage():
    """Some extra fields to test to ensure full coverage"""
    rfield = ReplacementField(conversion="s", z=True, hashtag=True, sign="-", zero=True)

    expected = "{!s:-z#0}"
    assert rfield.build() == expected
