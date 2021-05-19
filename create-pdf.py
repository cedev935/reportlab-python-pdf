from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
# import random
# import string



def create_pdf(
    beneficiary_name: str,
    beneficiary_bank: str,
    beneficiary_account_number: str,
    transaction_amount: str,
    transaction_date: str,
    transaction_type: str,
    transaction_reference: str,
    transaction_purpose: str,
):
    """Create PDF

    Args:
        beneficiary_name: beneficiary_name
        beneficiary_bank: beneficiary_bank
        beneficiary_account_number: beneficiary_account_number
        transaction_amount: transaction_amount
        transaction_date: transaction_date
        transaction_type: transaction_type
        transaction_reference: transaction_reference
        transaction_purpose: transaction_purpose

    """
    packet = io.BytesIO()

    can = canvas.Canvas(packet, pagesize=letter)
    
    # can.setFillColorRGB(255, 255, 255) #
    can.drawString(280, 503, beneficiary_name)
    can.drawString(280, 477, beneficiary_bank)
    can.drawString(280, 453, beneficiary_account_number)
    can.drawString(280, 427, transaction_amount)
    can.drawString(280, 402, transaction_date)
    can.drawString(280, 377, transaction_type)
    can.drawString(280, 355, transaction_reference)
    can.drawString(280, 330, transaction_purpose)
    can.save()

    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # getting the existing pdf file
    existing_pdf = PdfFileReader(open("assets/original.pdf", "rb"))
    output = PdfFileWriter()

    # add our text to the pdf 
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)

    # genertate a new pdf
    outputStream = open("generated-pdf/" + transaction_reference + ".pdf", "wb")
    output.write(outputStream)
    outputStream.close()

beneficiary_name = "Schweppes"
beneficiary_bank = "Steward Bank"
beneficiary_account_number = "1003088252"
transaction_amount = "$ 110898.58"
transaction_date = "30-04-2021"
transaction_type = "INTERNET RTGS"
transaction_reference = "413110430H000274"
transaction_purpose = "null"


# i = 0
# while i < 100:
create_pdf(
    beneficiary_name=beneficiary_name,
    beneficiary_bank=beneficiary_bank,
    beneficiary_account_number=beneficiary_account_number,
    transaction_amount=transaction_amount,
    transaction_date=transaction_date,
    transaction_type=transaction_type,
    transaction_reference=transaction_reference,
    transaction_purpose=transaction_purpose,
)

    # i += 1
