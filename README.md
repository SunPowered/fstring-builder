# FString Builder

A simple Python library to enhance the API of the native Python f-string syntax.  

This came about from needing to often refer back to the native [format string syntax](https://docs.python.org/3/library/string.html#format-string-syntax).  
I found that configuring formatting options within the program was tricky and tedious.  

For example, if I wanted a user-defined width for a given line, it was awkward to include it in every instance of 
that field.  Many mistakes were made.

The API so far is what resulted after prototyping out the idea on a couple personal projects.  This ended up working 
really well for the line formatting portions, I think it could be useful to others.  

## Installation

Install via pip: 


```
$ pip install fstring-builder
```

## Interface

The idea is to have a main `FormatString` object that is able to collect and manage items comprising that ultimate 
string.  This object can build a format-ready string from its items.   

Each item is either a simple string-like object that gets concatenated in place, or it is a `ReplacementField`, 
traditionally noted in f-strings with a format spec inside curly braces `{<format_syntax>}`.

The `ReplacementField` accepts all the options from a normal format string.  By default, they are all `None`:

| **Name**     | **Type**               | **Description**                                      |
| ------------ | ---------------------- | ---------------------------------------------------- |
| `name`       | `str`                  | Keyword name variable for the field                  |
| `conversion` | `['s', 'r', 'a']`      | Convert the field to a string, repr, or ascii format |
| `fill`       | `str`                  | Single string character to use as a fill             |
| `align`      | `['<', '>', '^', '=']` | Align text left, right, center, or numeric-padded    |
| `sign`       | `['+', '-', ' ']`      | Sign characters for numeric types                    |
| `z`          | `bool`                 | Coerce floating point numbers to positive 0          |
| `hashtag`    | `bool`                 | Use 'alternate' form for conversion                  |
| `zero`       | `bool`                 | Pad numeric numbers with `0`                         |
| `width`      | `int`                  | Set a character width value for the field            |
| `grouping`   | `[',', '_']`           | Set the numeric grouping characters                  |
| `precision`  | `int`                  | Floating point precision value                       |
| `type`       | `str`                  | Format type characters, i.e. `d`, `n`, or `f`        |

Once your field parameters are set, each field can be built using the `.build()` method.  Alternatively, each `FormatString` can build all its elements using its own `.build()`.

The result of a `.build()` is a *format-ready* string, ie a string that you can call `.format(**kwargs)` on.  The `FormatString` object has a convenience function `.format(**kwargs)` that builds and formats itself with any parameters passed.

## Example

The following example creates a format ready string for a monetary currency.  It could be expanded to provide for a more generic locale-aware currency formatter 

```python
import fstring_builder as fsb

# Simple currency format string
# f`${qty:>12,.2f}`

currency_fmt = fsb.FormatString(
    "$", 
    fsb.ReplacementField(
        name="qty",
        grouping=",",
        align="right",
        width=12,
        precision=2,
        type="float"
    )
)

print(currency_fmt)                     # "${qty:>12,.2f}"
print(currency_fmt.format(qty=312.5))   # "$      312.50"
print(currency_fmt.format(qty=15324))   # "$   15,324.00"

currency_fmt._width = 10
print(currency_fmt.format(qty=15324))   # "$ 15,324.00"
```

### Chainable Methods

The parameters for `ReplacementField` objects can also be set after construction via methods.  They are all chainable, allowing for something like:

```python
import fstring_builder as fsb

currency_fmt = fsb.FormatString("$",
    fsb.ReplacementField(name="qty")
        .align(fsb.Align.RIGHT)
        .grouping(fsb.Grouping.COMMA)
        .width(12)
        .precision(2)
        .type(fsb.Type.Float.NUMERIC)
)

currency_fmt.build()

print(currency_fmt.format(qty=15324))       # "$   15,324.00"
print(currency_fmt.format(qty=-2157.25))    # "$   -2,157.25"
print(currency_fmt.format(qty=0))           # "$        0.00"
```