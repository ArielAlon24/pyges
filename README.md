# pyges

Pyges is a highly customizable Python-based static site generator and runtime designed for flexibility.

## Usage

### Site Creation

The pyges module revolves around the `Site` class. To create one first create a `Config` and specify your `src` folder, this is the folder where all of your site will be generated from.

```python
from pyges import Site, Config

config = Config(src="src")

```

Next, create a `Site` instance supplying it the already created `Config`

```python
site = Site(config)
```

### Adding a Page

Apart from the `styles.css` style sheet, `CNAME` file and `Assets` folder that have to be created inside the `src` folder. HTML pages can be created from Markdown files using the `site.add` decorator.

```python
from pyges.nodes import Html

@site.add("index.md")
def index(content: str) -> Html:
    return Html(content)
```

In the above example Pyges will read the `index.md` markdown file transform it to an HTML string and pass it as an an argument - `content` in our case to the decorated function. Then, inside the function body an `Html` tag with the `index.md` HTML content is created.

After building the site using

```python
if __name__ == '__main__':
    site.build()
```

a file named `index.html` will be saved in the out folder (`out` by default) at the same relative path as `index.md` was to `src`.

For example, in case `src/index.md` contained:

```md
# Test

This is index.md
```

After building the site `out/index.html` will contain:

```html
<html>
  <h1>Test</h1>
  <p>The <i>index</i> function will return the following HTML</p>
</html>
```

### Adding a ~~Page~~ Pages

In case there's a folder that consists of pages that should have the same template, instead of adding a creator function for each one the folder name can be supplied to the `site.add` decorator. For example

```python
from pyges.nodes import Html, Article


@site.add("blogs")
def blog(content: str) -> Html:
    return Html(Article(content))
```

### Flexible HTML and Markdown

Pyges has support for (soon) all HTML tags, meaning a creator function (a name for a function decorated with the `site.add` add) can utilize all of those to create a specific page as for it's needs. Not only that, but using simple `yaml` syntax in the start of any Markdown file in conjunction with inheriting from the `Scheme` dataclass for it's validation, creates a creates a robust method to access any page metadata.

In the end, a customizable and rich templating system can be achieved, let's improve the previous example, be adding to each blog the following `yaml` configuration

```yaml
---
name: <name>
date: <date>
---
// blog //
```

This is specified as mentioned using a dataclass the inherits from `Scheme`

```python
import datetime

@dataclass
class Blog(Scheme):
    name: str
    date: datetime.date

```

Now our improved `blog` function can look like this:

```python
@site.add("blogs/", scheme=Blog)
def blog(content: str, name: str, date: datetime.date) -> Html:
    return Html(
        Article(
            [
                Div([H(size=1, value=name), P(str(date))]),
                content,
            ]
        )
    )
```

Notice that all `Blog` scheme properties are passed to the creator function.

Another great feature, is the ability to get all pages created by a specific creator, this is done by the `site.pages` method. Let's say we want to create a page to show all blogs created by `blog`, we can do that in the following manner

```python
@site.add("blogs.md")
def blog(content: str) -> Html:
    return Html(
        [
            P(content)
            Article(
                [
                    Div(b.name)
                    for b in sorted(
                        site.pages(creator=blog),
                        key=lambda x: x.properties["date"],
                    )
                ],
            )
        ]
    )
```

### Debugging

Lastly, when developing a website, instead of building it every time, use the `site.debug` method, this will open a flask runtime, that updates changes automatically as you work!
