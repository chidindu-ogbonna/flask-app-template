from flask import Flask

def test_app(app):
    assert isinstance(app, Flask)
