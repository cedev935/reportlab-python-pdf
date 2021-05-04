from reportlab.pdfgen import canvas


def create_pdf(
    client_name: str,
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
        client_name: client_name
        beneficiary_name: beneficiary_name
        beneficiary_bank: beneficiary_bank
        beneficiary_account_number: beneficiary_account_number
        transaction_amount: transaction_amount
        transaction_date: transaction_date
        transaction_type: transaction_type
        transaction_reference: transaction_reference
        transaction_purpose: transaction_purpose

    """

    pdf_file = "generated-pdf/" + transaction_reference + ".pdf"
    img_file = "images/zb-bank.png"

    can = canvas.Canvas(pdf_file)

    x_start = 30
    y_start = 740
    can.drawImage(
        img_file,
        x_start,
        y_start,
        width=120,
        height=60,
        preserveAspectRatio=True,
        mask="auto",
    )

    can.setFont("Times-Roman", 13)
    can.drawString(50, 710, "Dear : " + client_name)
    can.drawString(
        50,
        680,
        "Thank you for transacting using the ZB Internet Banking platform.  Please find below a",
    )
    can.drawString(
        50, 660, "confirmation of the Internet transaction that was done in respect of:"
    )

    can.drawString(50, 620, "Beneficiary Name")
    can.drawString(210, 620, ": " + beneficiary_name)

    can.drawString(50, 590, "Beneficiary Bank Name")
    can.drawString(210, 590, ": " + beneficiary_bank)

    can.drawString(50, 560, "Beneficiary Account Number")
    can.drawString(210, 560, ": " + beneficiary_account_number)

    can.drawString(50, 530, "Transaction Amount")
    can.drawString(210, 530, ": " + transaction_amount)

    can.drawString(50, 500, "Transaction Date")
    can.drawString(210, 500, ": " + transaction_date)

    can.drawString(50, 470, "Transaction Type")
    can.drawString(210, 470, ": " + transaction_type)

    can.drawString(50, 440, "Transaction Reference")
    can.drawString(210, 440, ": " + transaction_reference)

    can.drawString(50, 410, "Transaction Purpose")
    can.drawString(210, 410, ": " + transaction_purpose)

    can.drawString(50, 350, "For & on behalf of ZB Bank")

    can.drawString(
        50,
        310,
        "For any queries kindly get in touch with our 24 Hour ZB Contact Centre on:",
    )
    can.drawString(50, 290, "+263 8677002005")
    can.drawString(50, 270, "SMS /WhatsApp: +263 772442685")

    can.showPage()

    can.save()


client_name = "INTELLI AFRICA SOLUTIONS"
beneficiary_name = "Schweppes"
beneficiary_bank = "Steward Bank"
beneficiary_account_number = "1003088252"
transaction_amount = "$ 110898.58"
transaction_date = "30-04-2021"
transaction_type = "INTERNET RTGS"
transaction_reference = "413110430H000274"
transaction_purpose = "null"


create_pdf(
    client_name=client_name,
    beneficiary_name=beneficiary_name,
    beneficiary_bank=beneficiary_bank,
    beneficiary_account_number=beneficiary_account_number,
    transaction_amount=transaction_amount,
    transaction_date=transaction_date,
    transaction_type=transaction_type,
    transaction_reference=transaction_reference,
    transaction_purpose=transaction_purpose,
)
