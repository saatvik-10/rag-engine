import fitz
from app.schemas.pdf_schema import PdfPage


def extract_pdf(pdf_path: PdfPage):
    document = fitz.open(pdf_path)

    pages = []

    for idx, page in enumerate(document):

        pages.append(PdfPage(page=idx + 1, text=page.get_text()))

    document.close()

    return pages
