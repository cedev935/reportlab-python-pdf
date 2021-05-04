from reportlab.pdfgen import canvas
 
 
def create_pdf():
    """Create pdf"""

    pdf_file = 'generated-pdf/receipt.pdf'
    img_file = 'images/zb-bank.png'
 
    can = canvas.Canvas(pdf_file)
 
    x_start = 30
    y_start = 740
    can.drawImage(img_file, x_start, y_start, width=120, height=60, preserveAspectRatio=True, mask='auto')

    can.setFont("Times-Roman", 13)
    can.drawString(50, 710, "Dear : INTELLI AFRICA SOLUTIONS ")
    can.drawString(50, 680, "Thank you for transacting using the ZB Internet Banking platform.  Please find below a")
    can.drawString(50, 660, "confirmation of the Internet transaction that was done in respect of:")
    
    can.drawString(50, 620, "Beneficiary Name")
    can.drawString(210, 620, ":Schweppes")
    
    can.drawString(50, 590, "Beneficiary Bank Name")
    can.drawString(210, 590, ":Steward Bank")

    can.drawString(50, 560, "Beneficiary Account Number")
    can.drawString(210, 560, ":1003088252")

    can.drawString(50, 530, "Transaction Amount")
    can.drawString(210, 530, ":$ 110898.58")

    can.drawString(50, 500, "Transaction Date")
    can.drawString(210, 500, ":30-04-2021")

    can.drawString(50, 470, "Transaction Type")
    can.drawString(210, 470, ":INTERNET RTGS")

    can.drawString(50, 440, "Transaction Reference")
    can.drawString(210, 440, ":413110430H000274")

    can.drawString(50, 410, "Transaction Purpose")
    can.drawString(210, 410, ":null")


    can.drawString(50, 350, "For & on behalf of ZB Bank")

    can.drawString(50, 310, "For any queries kindly get in touch with our 24 Hour ZB Contact Centre on:")
    can.drawString(50, 290, "+263 8677002005")
    can.drawString(50, 270, "SMS /WhatsApp: +263 772442685")

    can.showPage()
 
    can.save()
 
create_pdf()
