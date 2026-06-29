from pydantic import BaseModel


class PdfPage(BaseModel):
    page: int = 0
    text: str
    source: str
