from jinja2 import Environment, FileSystemLoader
import os
import pdfkit
from PyPDF2 import PdfFileWriter, PdfFileReader
import random
import string

def generate_pop(
    account_holder_name: str,
    account_holder_full_name: str,
    account_holder_address: str,
    account_holder_city_country: str,
    account_number: str,
    currency: str,
    account_type: str,
    transactions: list,
):
    """Create POP PDF

    Args:
        account_holder_name: account_holder_name,
        account_holder_full_name: account_holder_full_name,
        account_holder_address: account_holder_address,
        account_holder_city_country: account_holder_city_country,
        account_number: account_number,
        currency: currency,
        account_type: account_type,
        transactions: [
                        {
                            "date": "07 Jun 21",
                            "description": {
                                "narration1":"OPENNING BALANCE",
                                "narration2":"",
                                "narration3":"",
                                "narration4":"",
                                "narration5":"",
                            },
                            "debit": "",
                            "credit": "",
                            "balance": "100,000.19",
                        },

                    ],

    """
    # pass variables to our html template
    env = Environment(loader=FileSystemLoader(os.getcwd()))
    template = env.get_template("templates/base_template.html")
    html = template.render(
        account_holder_name=account_holder_name.upper(),
        account_holder_full_name=account_holder_full_name.upper(),
        account_holder_address=account_holder_address.upper(),
        account_holder_city_country=account_holder_city_country.upper(),
        account_number=account_number.upper(),
        currency=currency.upper(),
        account_type=account_type.upper(),
        transactions=transactions,
    )

    # save the generated html file
    file = open("templates/temp-generated-html/"+account_number+".html", "w")
    file.write(html)
    file.close()


    options = {
        "page-size": "Letter",
        "margin-top": "0.0in",
        "margin-right": "0.0in",
        "margin-bottom": "1.5in",
        "margin-left": "0.0in",
        "encoding": "UTF-8",
        "footer-html": "templates/footer.html",
        # '--header-html': 'header.html',
        "custom-header": [("Accept-Encoding", "gzip")],
        "no-outline": None,
    }

    # convert the html file to a pdf file
    pdfkit.from_file("templates/temp-generated-html/"+account_number+".html", "generated-pdf/"+account_number+".pdf", options=options)

    os.remove("templates/temp-generated-html/"+account_number+".html")


account_holder_name = "Nigel Bongani Zulu"
account_holder_full_name = "Nigel Zulu"
account_holder_address = "71314 Lobengula West"
account_holder_city_country = "Bulawayo, Harare"
account_number = "1003088252"
currency = "ZWL"
account_type = "Saving Account"

transactions = [
    {
        "date": "07 Jun 21",
        "description": {
            "narration1":"OPENNING BALANCE",
            "narration2":"",
            "narration3":"",
            "narration4":"",
            "narration5":"",
        },
        "debit": "",
        "credit": "",
        "balance": "100,000.19",
    },

    {
        "date": "07 Feb 21",
        "description": {
            "narration1":"WHATSAPP BALANCE ENQ",
            "narration2":"200T60187205725",
            "narration3":"WHATSAPP|CHARGES",
            "narration4":"4144601872200|4131847336932",
            "narration5":"263775580596",
        },
        "debit": "22000.00",
        "credit": "",
        "balance": "22035.19",
    },
    {
        "date": "07 Feb 21",
        "description": {
            "narration1":"WHATSAPP BALANCE ENQ",
            "narration2":"200T60187205725",
            "narration3":"WHATSAPP|CHARGES",
            "narration4":"4144601872200|4131847336932",
            "narration5":"263775580596",
        },
        "debit": "",
        "credit": "22000.00",
        "balance": "22035.19",
    },

]

# i = 0
# while i < 2:
#     test_account_number = "".join(
#             random.choice(string.ascii_uppercase + string.digits) for i in range(8)
#         )

generate_pop(
    account_holder_name=account_holder_name,
    account_holder_full_name=account_holder_full_name,
    account_holder_address=account_holder_address,
    account_holder_city_country=account_holder_city_country,
    account_number=test_account_number,
    currency=currency,
    account_type=account_type,
    transactions=transactions,
)

    # i += 1
