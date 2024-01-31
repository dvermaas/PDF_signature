from pyhanko.keys import load_cert_from_pemder
from pyhanko.pdf_utils.reader import PdfFileReader
from pyhanko.sign.validation import validate_pdf_signature
from pyhanko_certvalidator import ValidationContext


def signature_status():
    with open("signed.pdf", "rb") as doc:
        if signatures := PdfFileReader(doc).embedded_signatures:
            root_cert = load_cert_from_pemder("QuoVadis_Root_CA_1_G3.crt")
            validation_context = ValidationContext(trust_roots=[root_cert])
            return validate_pdf_signature(signatures[-1], validation_context)
        return None


print(signature_status().valid)
