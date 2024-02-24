from ...pyges.nodes import (
    String,
    H,
    P,
    Span,
    Br,
    B,
    I,
    Strong,
    Em,
    Mark,
    Small,
    Del,
    Ins,
    Sub,
    Sup,
    Attribute,
)


def test_string():
    string = String("Hello, World!")
    assert str(string) == "Hello, World!"


def test_header():
    for size in range(1, 7):
        header = H(size=size, value=String(f"Header {size}"))
        assert str(header) == f"<h{size}> Header {size} </h{size}>"


def test_paragraph():
    paragraph = P([String("This is a test paragraph.")])
    assert str(paragraph) == "<p> This is a test paragraph. </p>"


def test_span():
    span = Span("Inline text", {Attribute.STYLE: "color: red"})
    assert str(span) == '<span style="color: red"> Inline text </span>'


def test_br():
    br = Br()
    assert str(br) == "<br>"


def test_bold():
    bold = B(String("Bold text"))
    assert str(bold) == "<b> Bold text </b>"


def test_italic():
    italic = I(String("Italic text"))
    assert str(italic) == "<i> Italic text </i>"


def test_strong():
    strong = Strong(String("Strong text"))
    assert str(strong) == "<strong> Strong text </strong>"


def test_emphasis():
    em = Em(String("Emphasized text"))
    assert str(em) == "<em> Emphasized text </em>"


def test_mark():
    mark = Mark(String("Marked text"))
    assert str(mark) == "<mark> Marked text </mark>"


def test_small():
    small = Small(String("Small text"))
    assert str(small) == "<small> Small text </small>"


def test_delete():
    delete = Del(String("Deleted text"))
    assert str(delete) == "<del> Deleted text </del>"


def test_insert():
    insert = Ins(String("Inserted text"))
    assert str(insert) == "<ins> Inserted text </ins>"


def test_subscript():
    sub = Sub(String("Subscript text"))
    assert str(sub) == "<sub> Subscript text </sub>"


def test_superscript():
    sup = Sup(String("Superscript text"))
    assert str(sup) == "<sup> Superscript text </sup>"


def test_all():
    html = P(
        [
            H(size=1, value="Main Header"),
            H(size=2, value="Sub Heading"),
            P(
                [
                    "Introduction paragraph with ",
                    Span("Inline styled text", {Attribute.STYLE: "color: blue"}),
                    ", followed by a line break.",
                    Br(),
                    B(
                        [
                            "Bold text with an ",
                            I("italic part"),
                            ", and a ",
                            Small("small section"),
                        ]
                    ),
                    Br(),
                    Strong(
                        [
                            "Strong text with a ",
                            Em("emphasized part"),
                            ", and a ",
                            Mark("marked section"),
                        ]
                    ),
                    P(
                        [
                            "Nested paragraph with ",
                            Del("deleted text"),
                            ", ",
                            Ins("inserted text"),
                            ", ",
                            Sub("subscript"),
                            ", and ",
                            Sup("superscript."),
                        ]
                    ),
                ]
            ),
        ]
    )

    expected_html = """<p>
    <h1> Main Header </h1>
    <h2> Sub Heading </h2>
    <p>
        Introduction paragraph with 
        <span style="color: blue"> Inline styled text </span>
        , followed by a line break.
        <br>
        <b>
            Bold text with an 
            <i> italic part </i>
            , and a 
            <small> small section </small>
        </b>
        <br>
        <strong>
            Strong text with a 
            <em> emphasized part </em>
            , and a 
            <mark> marked section </mark>
        </strong>
        <p>
            Nested paragraph with 
            <del> deleted text </del>
            , 
            <ins> inserted text </ins>
            , 
            <sub> subscript </sub>
            , and 
            <sup> superscript. </sup>
        </p>
    </p>
</p>"""

    assert str(html) == expected_html
