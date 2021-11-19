# Challenge for NewCombin

import Tax
import DatabaseManager
import Transaction
import ServiceFilter

def createBill():

    db = DatabaseManager.DatabaseManager()
    bill = Tax.Tax()
    bill.inputService()
    db.saveService(bill.servicetype, bill.description, bill.expirationdate, bill.amount, bill.paymentStatus, bill.barcode)

def payBill():
    db = DatabaseManager.DatabaseManager()
    transaction = Transaction.Transaction()
    transaction.payProcess()
    selectionAux = int(input("El importe a pagar es ${} : \n 1. OK \n 2. Cancelar \n ".format(transaction.totalpay)))
    if selectionAux == 1:
        db.payService(transaction.barcode, transaction.cardnumber, transaction.totalpay, transaction.paydate)

def filter():
    selection2 = int(input("Selecciona una opción para ver las facturas impagas: \n 1. Filtrar por dias pasados \n 2. Filtrar por tipo de servicio \n"))
    filter = ServiceFilter.ServiceFilter()
    if selection2 == 1:
        filter.consultbydays(int(input("Introduce la cantidad de dias a filtrar :")))
    if selection2 == 2:
        filter.consultbytype(input("Introduce el tipo de servicio a filtrar :"))

if __name__ == '__main__':
    selection = 1
    while selection == 1 or selection == 2 or selection == 3:
        selection = int(input("Selecciona una opción: \n 1. Agregar una factura \n 2. Pagar una factura \n 3. Filtrar servicios \n 4. Terminar \n"))
        if selection == 1:
            createBill()
        if selection == 2:
            payBill()
        if selection == 3:
            filter()

