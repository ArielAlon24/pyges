from pyges.nodes import Div, P, H, String, Span, Html, Br


def test_string() -> None:
    s1 = String("This is a test")
    s2 = String("")

    assert str(s1) == "This is a test"
    assert str(s2) == ""


def test_html() -> None:
    h = Html(Div([P(String("This is a text")), Br(), P(String("Second line"))]))

    assert (
        str(h)
        == """<!DOCTYPE html>
<html>
    <div>
        <p> This is a text </p>
        <br/>
        <p> Second line </p>
    </div>
</html>"""
    )


def test_simple() -> None:
    simple = Div(
        [
            H(size=1, value=String("This is the Header.")),
            P(String("This is a paragraph inside the Header")),
        ]
    )

    assert (
        str(simple)
        == """<div>
    <h1> This is the Header. </h1>
    <p> This is a paragraph inside the Header </p>
</div>"""
    )


def test_class_and_id() -> None:
    document = Div(_class="classy", _id="idealy", value=String("Text string"))
    assert str(document) == """<div class="classy" id="idealy"> Text string </div>"""


def test_nested_tags() -> None:
    complex_structure = Div(
        [
            H(size=2, value=String("Nested Header")),
            P(
                [
                    String("This is a nested "),
                    Span(String("span element"), _class="span-class"),
                    String("."),
                ]
            ),
        ],
        _class="outer-div",
    )

    assert (
        str(complex_structure)
        == """<div class="outer-div">
    <h2> Nested Header </h2>
    <p>
        This is a nested 
        <span class="span-class"> span element </span>
        .
    </p>
</div>"""
    )


def test_empty_tags() -> None:
    empty_div = Div()
    assert str(empty_div) == "<div></div>"


def test_attributes_on_nested_tags() -> None:
    nested_with_attrs = Div(
        [
            P(String("Paragraph with style"), _style="color: red;"),
        ],
        _class="container",
    )
    assert (
        str(nested_with_attrs)
        == """<div class="container">
    <p style="color: red;"> Paragraph with style </p>
</div>"""
    )


def test_multiple_children() -> None:
    multi_children = Div(
        [
            P(String("First Paragraph")),
            P(String("Second Paragraph")),
        ]
    )
    assert (
        str(multi_children)
        == """<div>
    <p> First Paragraph </p>
    <p> Second Paragraph </p>
</div>"""
    )


def test_special_characters() -> None:
    special_chars = P(String("Special & < > Characters"))
    assert str(special_chars) == "<p> Special &amp; &lt; &gt; Characters </p>"
