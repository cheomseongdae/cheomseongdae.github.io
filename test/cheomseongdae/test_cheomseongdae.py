import cheomseongdae


def test_ping():
    r = cheomseongdae.Cheomseongdae.ping()
    assert r == 'pong'

    r = cheomseongdae.Cheomseongdae.ping(n=3)
    assert r == 'pppong'


def test_cmd_ping():
    r = cheomseongdae.cmd_ping()

