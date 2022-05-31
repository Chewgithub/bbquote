from bbquote.lib import get_quote
def test_my_func():
    assert type(get_quote()) == str
