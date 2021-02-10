from poetry_demo1 import __version__
from poetry_demo1 import poetrydemo1


def test_version():
    assert poetrydemo1.poetrydemo1() == "PoetryDemo2"#"PoetryDemo1"
    # assert __version__ == '0.1.0'
