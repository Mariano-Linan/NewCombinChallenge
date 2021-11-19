import datetime
import DatabaseManager

class Transaction:

    def __init__(self):
        self.totalpay = None
        self.cardnumber = None
        self.barcode = None
        self.paydate = None


    def payProcess(self):

        db = DatabaseManager.DatabaseManager()

        selection =int(input("Selecciona un metodo de pago: \n 1. Tarjeta de debito \n 2. Tarjeta de credito \n 3. Efectivo \n"))

        if selection == 1 or selection == 2:
            self.cardnumber = int(input("Por favor ingrese su numero de tarjeta sin espacios: "))
        else:
            self.cardnumber = 0

        self.barcode = int(input("Ingrese codigo de barras de su factura: "))
        self.totalpay = db.amount(self.barcode)
        self.paydate = datetime.date.today()
