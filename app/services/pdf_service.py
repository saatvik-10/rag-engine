import fitz
from app.schemas.pdf_schema import PdfPage


def extract_pdf(pdf_path: PdfPage):
    document = fitz.open(pdf_path)

    pages = []

    for idx, page in enumerate(document):

        text = page.get_text()

        if not text.strip():
            continue

        pages.append(PdfPage(page=idx + 1, text=text, source=pdf_path.split("/")[-1]))

    document.close()

    return pages
