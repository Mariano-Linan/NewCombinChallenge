import uuid
import datetime

class Tax:

    def __init__(self):
        self.servicetype = None
        self.description = None
        self.expirationdate = None
        self.amount = None
        self.paymentStatus = None
        self.barcode = None

    def getDate(self):
        year = int(input('Ingrese año de expiración: '))
        month = int(input('Ingrese mes de expiración: '))
        day = int(input('Ingrese día de expiración: '))
        expirationdate = datetime.date(year, month, day)
        return expirationdate

    def inputService(self):
        self.servicetype = input("Por favor ingrese el tipo de servicio que desea agregar: ")
        self.description = input("Descripción del servicio: ")
        self.expirationdate = self.getDate()
        self.amount = float(input("Ingresa monto del servicio: "))
        self.paymentStatus = "impago"
        self.barcode = uuid.uuid4().int
        print("Servicio creado con codigo de barra: ", self.barcode)

