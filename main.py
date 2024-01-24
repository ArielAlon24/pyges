from pyges.nodes import Html, Head, Title, String, Body, H, Span, P, Img

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
                        Span("Inline text", _style="color: red;"),
                        ".",
                    ]
                ),
                Img(src="flower.jpeg", _alt="test"),
            ]
        ),
    ]
)


print(blog)
