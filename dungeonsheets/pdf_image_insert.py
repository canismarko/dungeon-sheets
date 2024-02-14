import io
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas


def insert_image_into_pdf(
    destination_pdf: Path,
    source_image_path: Path,
    page_target_index: int,
    x_center: int,
    y_center: int,
    max_width: int,
    max_height: int,
):
    packet = io.BytesIO()
    pdf_canvas = canvas.Canvas(packet)
    pdf_canvas.drawImage(
        image=source_image_path,
        x=x_center,
        y=y_center,
        width=max_width,
        height=max_height,
        anchor="c",
        anchorAtXY=True,
        preserveAspectRatio=True,
        mask="auto",
    )
    pdf_canvas.showPage()
    pdf_canvas.save()
    packet.seek(0)

    reader = PdfReader(destination_pdf)
    stamp = PdfReader(packet)
    writer = PdfWriter()

    writer.clone_document_from_reader(reader)
    for i, page in enumerate(writer.pages):
        if i == page_target_index:
            page.merge_page(stamp.pages[0])
    writer.write(destination_pdf)
