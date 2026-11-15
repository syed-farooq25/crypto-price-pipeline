from api import clean_rows

def test_clean_rows_makes_numbers():
    rows = [{"coin": "bitcoin", "price_usd": "64540.00", "price_inr": "6082574.00", "change_24h_percent": "-4.10"}]

    result= clean_rows(rows)

    assert result[0]["price_usd"] == 64540.0
    assert result[0]["price_inr"] == 6082574.0
    assert result[0]["change_24h_percent"] == -4.1