from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from send_email import EmailController as email_controller


def create_pdf(
    amount: str,
    voucher_number: str,
):
    """Create PDF

    Args:
        amount: amount
        voucher: voucher

    """
    packet = io.BytesIO()

    can = canvas.Canvas(packet, pagesize=letter)

    can.setFillColor("#144f5d")  #
    can.setFont("Helvetica-Bold", 35)
    can.drawString(40, 130, amount)

    can.setFillColor("#144f5d")  #
    can.setFont("Helvetica-Bold", 10)
    can.drawString(600, 250, voucher_number)

    can.setFillColor("#144f5d")  #
    can.setFont("Helvetica-Bold", 20)
    can.drawString(300, 120, voucher_number)
    can.save()

    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # getting the existing pdf file
    existing_pdf = PdfFileReader(open("assets/voucher.pdf", "rb"))
    output = PdfFileWriter()

    # add our text to the pdf
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)

    # genertate a new pdf
    outputStream = open("generated-pdf/" + voucher_number + ".pdf", "wb")
    output.write(outputStream)
    outputStream.close()

    # email_controller.send_pop_as_email(transaction_reference)


amount = "$USD50"
voucher_number = "EW5144522885505575112"

# i = 0
# while i < 100:
create_pdf(
    amount=amount,
    voucher_number=voucher_number,
)

# i += 1
