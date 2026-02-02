from src.fingerprint import Fingerprinter

def test_fingerprint_returns_dict():
    fp = Fingerprinter()
    result = fp.analyze("http://example.com")
    assert isinstance(result, dict)
