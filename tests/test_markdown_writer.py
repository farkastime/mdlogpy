from mdlogpy.mdwriter import MarkdownWriter


def test_markdown_writer_basic():
    mw = MarkdownWriter()
    mw.title("Main Title")
    mw.h1("Section")
    mw.h2("Subsection")
    mw.h3("Subsubsection")
    mw.bullet("Bullet point")
    mw.blank()
    mw.code("print('hello')", lang="python")
    mw.numbered("First item", 1)
    mw.quote("A quote")
    mw.bold("Bold text")
    mw.italic("Italic text")
    mw.link("Google", "https://google.com")
    mw.image("Alt", "https://img.com/img.png")
    mw.hr()
    mw.table(["A", "B"], [["1", "2"], ["3", "4"]])
    output = mw.render()
    assert "# Main Title" in output
    assert "## Section" in output
    assert "### Subsection" in output
    assert "#### Subsubsection" in output
    assert "- Bullet point" in output
    assert "```python" in output
    assert "print('hello')" in output
    assert "1. First item" in output
    assert "> A quote" in output
    assert "**Bold text**" in output
    assert "*Italic text*" in output
    assert "[Google](https://google.com)" in output
    assert "![Alt](https://img.com/img.png)" in output
    assert "---" in output
    assert "| A | B |" in output
    assert "| 1 | 2 |" in output
    assert "| 3 | 4 |" in output
