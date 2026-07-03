import fitz
from pathlib import Path

from app.schemas.pdf_schema import PdfPage


def extract_pdf(pdf_path: PdfPage):
    document = fitz.open(pdf_path)

    pages = []

    for idx, page in enumerate(document):

        text = page.get_text()

        if not text.strip():
            continue

        pages.append(PdfPage(page=idx + 1, text=text, source=Path(pdf_path).name))

    document.close()

    return pages
