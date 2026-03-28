"""Make tests a little nicer."""

import io
import tomllib
from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.util.docutils import docutils_namespace

PROJECT = Path(__file__).parent.parent
DATA_DIR = PROJECT / "tests/data"


def read_toml(name: str) -> dict[str, str]:
    """Read a .toml test data file.

    All values are strings, and are dedented.
    """
    with (DATA_DIR / f"{name}.toml").open("rb") as f:
        data = tomllib.load(f)
    return {k: dedent(v) for k, v in data.items()}


def text_and_id(*, text: str, id: str = ""):
    """Helper to create pytest parameters for tests."""
    assert text, "Test cases must have text content or a file name"
    if "\n" in text:
        assert text.startswith("\n"), "Don't start text with a backslash"
        text = dedent(text[1:])
    else:
        # It's a data file name
        assert not id, "Don't provide filename and id"
        id = text
        text = read_toml(text)["rst"]
    assert id, "Test cases must have an id"
    return text, id


@dataclass
class SphinxResult:
    doctree: nodes.document
    warning: str
    status: str
    html_file: str


def run_sphinx(content: str, buildername: str, extensions: list[str]) -> SphinxResult:
    Path("index.rst").write_text(
        dedent("""\
        .. toctree::
            the_page
            dummy_content
        """)
    )
    Path("dummy_content.rst").write_text(Path(DATA_DIR / "dummy_content.rst").read_text())

    Path("the_page.rst").write_text(content, encoding="utf-8")
    Path("conf.py").write_text(
        dedent(f"""\
            extensions = {extensions!r}
            nitpick_ignore = {{
                ("py:module", "my_thing"),
                ("py:mod", "my_thing"),
            }}
        """),
        encoding="utf-8",
    )

    status = io.StringIO()
    warning = io.StringIO()
    with docutils_namespace():
        app = Sphinx(
            srcdir=".",
            confdir=".",
            outdir="_build",
            doctreedir="_build/.doctrees",
            buildername=buildername,
            freshenv=True,
            status=status,
            warning=warning,
        )

        app.build()
        result = SphinxResult(
            doctree=app.env.get_doctree("the_page"),
            warning=warning.getvalue(),
            status=status.getvalue(),
            html_file="_build/the_page.html",
        )

    # Filter out the expected duplicate object warning from our test data,
    # which sometimes intentionally defines two things with the same name.
    warnings = "".join(
        line
        for line in result.warning.splitlines(keepends=True)
        if "duplicate object description" not in line
    )
    print(f"WARNINGS: {warnings}")
    assert not warnings

    return result
