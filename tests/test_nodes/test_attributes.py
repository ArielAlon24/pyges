from ...pyges.nodes import Div, Attribute, DataAttribute


def test_one_attribute() -> None:
    html = Div("Only one attribute", {Attribute.STYLE: "color: red"})
    assert str(html) == '<div style="color: red"> Only one attribute </div>'


def test_class_attribute_and_data_attribute() -> None:
    html = Div(
        "Hello, World!",
        {Attribute.CLASS: "test", DataAttribute("name"): "123"},
    )
    assert str(html) == '<div class="test" data-name="123"> Hello, World! </div>'


def test_two_data_attributes_with_identical_name() -> None:
    html = Div(
        "Hello, World!",
        {DataAttribute("name"): "test", DataAttribute("name"): "123"},
    )
    assert str(html) == '<div data-name="test" data-name="123"> Hello, World! </div>'


def test_id_and_style_attributes() -> None:
    html = Div(
        "Another example",
        {Attribute.ID: "uniqueId", Attribute.STYLE: "color: red;"},
    )
    assert str(html) == '<div id="uniqueId" style="color: red;"> Another example </div>'


def test_combining_class_and_data_attributes() -> None:
    html = Div(
        "Mixed attributes",
        {Attribute.CLASS: "mix", DataAttribute("role"): "presentation"},
    )
    assert (
        str(html)
        == '<div class="mix" data-role="presentation"> Mixed attributes </div>'
    )


def test_empty_attributes() -> None:
    html = Div("Empty attributes", {})
    assert str(html) == "<div> Empty attributes </div>"


def test_multiple_data_attributes() -> None:
    html = Div(
        "Multiple data attributes",
        {DataAttribute("key1"): "value1", DataAttribute("key2"): "value2"},
    )
    assert (
        str(html)
        == '<div data-key1="value1" data-key2="value2"> Multiple data attributes </div>'
    )


def test_special_characters_in_attributes() -> None:
    html = Div(
        "Special chars",
        {Attribute.CLASS: "test&class", DataAttribute("complex-name"): "value&value"},
    )
    assert (
        str(html)
        == '<div class="test&class" data-complex-name="value&value"> Special chars </div>'
    )
