from pyges import Site
from pyges.config import Config
from pyges.nodes import *
import datetime
from pyges.markdown import Scheme
from typing import List
from dataclasses import dataclass


config = Config(src="src", out="out")


site = Site(config)


class Blog(Scheme):
    name: str
    date: datetime.date
    tags: List[str]


def navbar() -> Nav:
    return Nav(
        [
            Div(
                A("Ariel Alon", attributes={Attribute.HREF: "/"}),
                attributes={Attribute.CLASS: "left-nav"},
            ),
            Div(
                [
                    A("Blogs", attributes={Attribute.HREF: "blogs"}),
                    A("About", attributes={Attribute.HREF: "about"}),
                    A(
                        "Github",
                        {Attribute.HREF: "https://github.com"},
                    ),
                ],
                attributes={Attribute.CLASS: "right-nav"},
            ),
        ],
        attributes={Attribute.CLASS: "navbar"},
    )


def head() -> Head:
    return Head(
        [
            Title("Blog"),
            Link(
                attributes={
                    Attribute.REL: "stylesheet",
                    Attribute.TYPE: "text/css",
                    Attribute.HREF: "styles.css",
                }
            ),
        ]
    )


@site.add("blogs/", scheme=Blog)
def blog(content: str, name: str, date: datetime.date, tags: List[str]) -> Html:
    return Html(
        [
            head(),
            Body(
                [
                    navbar(),
                    Article([H(size=1, value=name), "{content: Markdown}"]),
                ]
            ),
        ]
    )


@site.add("index.md")
def index() -> Html:
    return Html(
        [
            head(),
            Body(
                [
                    navbar(),
                    Article(
                        [H(size=1, value="{post.header: str}"), "{content: Markdown}"]
                    ),
                ]
            ),
        ]
    )


@site.add("about.md")
def about() -> Html:
    return Html(
        [
            head(),
            Body(
                [
                    navbar(),
                    Article(
                        [H(size=1, value="{post.header: str}"), "{content: Markdown}"]
                    ),
                ]
            ),
        ]
    )


if __name__ == "__main__":
    site.generate()
