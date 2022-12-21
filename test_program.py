import strParser

def test_output(capfd, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    strParser.string_parser()

    out, err = capfd.readouterr()
    assert "Adjusted DSPAM Confidence Score: 0.8725" in out
    
