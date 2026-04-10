"""Template rendering utilities for generated dashboards."""

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"
CSS_DIR = STATIC_DIR / "css"
JS_DIR = STATIC_DIR / "js"


def render_dashboard_html(
    placeholders: dict[str, str],
    template_name: str = "template.html",
) -> str:
    """Render dashboard HTML by replacing {{placeholders}} in the template."""
    template_path = TEMPLATES_DIR / template_name
    html = template_path.read_text(encoding="utf-8")

    for key, value in placeholders.items():
        html = html.replace(f"{{{{{key}}}}}", value)

    return html


def write_dashboard_html(html: str, output_path: str | Path) -> Path:
    """Write rendered HTML to disk and return the resolved output path."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")
    return output_path.resolve()
