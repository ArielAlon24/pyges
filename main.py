from pyges.nodes import Html, Head, Title, String, Body, H, Span, P, Img, Attribute

blog = Html(
    [
        Head(Title("Blog")),
        Body(
            [
                H(size=1, value=String("Header")),
                H(size=2, value=String("Sub Heading")),
                P(
                    [
                        "This is a paragraph with some ",
                        Span("Inline text", {Attribute.STYLE: "color: red"}),
                        ".",
                    ]
                ),
                Img(attributes={Attribute.SRC: "flower.jpeg", Attribute.ALT: "test"}),
            ]
        ),
    ]
)


print(blog)
