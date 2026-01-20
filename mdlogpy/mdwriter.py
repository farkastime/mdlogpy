class MarkdownWriter:
    def __init__(self):
        self.lines = []

    def title(self, text):
        self.lines.append(f"# {text}\n")

    def h1(self, text):
        self.lines.append(f"## {text}\n")

    def h2(self, text):
        self.lines.append(f"### {text}\n")

    def h3(self, text):
        self.lines.append(f"#### {text}\n")

    def bullet(self, text):
        self.lines.append(f"- {text}")

    def blank(self):
        self.lines.append("")

    def code(self, code, lang=""):
        self.lines.append(f"```{lang}")
        self.lines.extend(code.splitlines())
        self.lines.append("```")

    def numbered(self, text, number):
        self.lines.append(f"{number}. {text}")

    def quote(self, text):
        self.lines.append(f"> {text}")

    def bold(self, text):
        self.lines.append(f"**{text}**")

    def italic(self, text):
        self.lines.append(f"*{text}*")

    def link(self, text, url):
        self.lines.append(f"[{text}]({url})")

    def image(self, alt, url):
        self.lines.append(f"![{alt}]({url})")

    def hr(self):
        self.lines.append("---")

    def table(self, headers, rows):
        header_line = "| " + " | ".join(headers) + " |"
        separator = "| " + " | ".join("---" for _ in headers) + " |"
        self.lines.append(header_line)
        self.lines.append(separator)
        for row in rows:
            self.lines.append("| " + " | ".join(row) + " |")

    def render(self):
        return "\n".join(self.lines)
