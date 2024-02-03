from pyges.nodes import Markdown, Scheme
import datetime
import pytest


def test_no_yaml() -> None:
    content = """# Heading 1
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
"""

    m = Markdown(content)

    assert (
        str(m)
        == """<h1>Heading 1</h1>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,</p>"""
    )
    assert repr(m) == content


def test_with_yaml() -> None:
    class Something(Scheme):
        pi: float
        is_this_a_test: bool
        function_name: str

    content = """---
pi: 3.14
is_this_a_test: True
function_name: "test_with_yaml"
---
# Heading 1
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
"""

    m = Markdown(content, scheme=Something)
    assert m.properties == {
        "pi": 3.14,
        "is_this_a_test": True,
        "function_name": "test_with_yaml",
    }
    assert (
        str(m)
        == """<h1>Heading 1</h1>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,</p>"""
    )
    assert (
        repr(m)
        == """
# Heading 1
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
"""
    )


def test_with_yaml_template_correct() -> None:
    class Template(Scheme):
        name: str
        date: datetime.date
        age: int

    content = """---
name: "pyges"
date: 2000-01-01
age: 1
---
# h1
    """
    m = Markdown(content, scheme=Template)

    assert m.properties == {
        "name": "pyges",
        "date": datetime.date(2000, 1, 1),
        "age": 1,
    }


def test_with_yaml_template_incorrect() -> None:
    class Template(Scheme):
        name: str
        date: datetime.date
        age: int

    content = """---
name: 1
date: 2020-01-01
age: "pyges"
---
# h1
"""
    with pytest.raises(TypeError):
        Markdown(content, scheme=Template)
