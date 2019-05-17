import barcode
from barcode.writer import ImageWriter

def create(type, num):
    """
    Parametr num should be a string type
    :param type: str
    :param num: str
    :return: None
    """
    EAN = barcode.get_barcode_class(type)
    ean = EAN(u'{}'.format(num), writer=ImageWriter())
    ean.save('created_barcode')

# if __name__=="__main__":
#     create("upc", "482300916524")
