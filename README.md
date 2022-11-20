# FString Builder

A simple Python library to extend the API of the native Python f-string formats.  This came about from having to always go back to the fstring format spec each time I needed something.  I also found that configuring formatting options within the program was tricky and tedious.  This led me to quickly spec out my preferred API for regular fstring formatting tasks.

## Interface

My proprosed interface, at its simplest, looks something like this:

```python
import fstring_builder as fsb

# Currency
# -> f`${qty:>12,.2f}`

currency_fmt = fsb.FString(
    "$", 
    fsb.FField(
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

currency_fmt.width = 10
print(currency_fmt.format(qty=15324))   # "$ 15,324.00"
```

An `FField` is a single replacement field of a larger `FString`.  The `FString` object collects string-like pieces and provides a
 format method, similar to strings.  This allows for `*args` and `**kwargs` style assignment in the format call. 


### Additional Interface

I also think its nice to use pre-typed Enum variants for each option.  Calls can be chained:

```python
import fstring_builder as fsb

currency_fmt = fsb.FString("$",
    fsb.FField(name="qty")
        .align(fsb.Align.RIGHT)
        .grouping(fsb.Grouping.COMMA)
        .width(12)
        .precision(2)
        .type(fsb.Type.Float.NUMERIC)
)

# Format strings can be pre-built for fast re-use, or built on-the-fly
print(currency_fmt.is_built)  # False

currency_fmt.build()

print(currency_fmt.is_built)  # True

print(currency_fmt.format(qty=15324))       # "$   15,324.00"
print(currency_fmt.format(qty=-2157.25))    # "$   -2,157.25"
print(currency_fmt.format(qty=0))           # "$        0.00"
```

