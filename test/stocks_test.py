


from app.stocks import format_usd


def test_usd_formatting():




    assert format_usd(4.5) == "$4.50"

    assert format_usd(4.555555555) == "$4.56"

    assert format_usd(1234567890) == "$1,234,567,890.00"