# This class hadle all releated to database management

import sqlite3
import datetime


class DatabaseManager:

    # Constructor handle the creation of the database tables
    def __init__(self):
        conn = sqlite3.connect('services.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS payables (
                    servicetype TEXT,
                    description TEXT,
                    expirationdate TEXT,
                    amount REAL,
                    paymentstatus TEXT,
                    barcode REAL
                    )""")
        c.execute("""CREATE TABLE IF NOT EXISTS transactions (
                            barcode REAL,
                            cardnumber INTEGER,
                            totalpay REAL,
                            paydate TEXT
                            )""")
        conn.commit()
        conn.close()

    # Save the new tax information to the data base
    def saveService(self, servicetype, description, expirationdate: datetime.date, amount, paymentstatus, barcode):
        conn = sqlite3.connect('services.db')
        c = conn.cursor()
        try:
            s = '%d-%02d-%02d' % (expirationdate.year, expirationdate.month, expirationdate.day)
            entities = (servicetype, description, s, amount, paymentstatus, float(barcode))
            c.execute(
                '''INSERT INTO payables(servicetype, description, expirationdate, amount, paymentstatus, barcode) VALUES(?, ?, ?, ?, ?, ?)''',
                entities)
            conn.commit()
            conn.close()

        except sqlite3.Error as error:
            print("Problema de conexión con la base de datos. ", error)

        finally:
            if conn:
                conn.close()

    # Confirmation of the payment so its saved to the database and change the payment status
    def payService(self, barcode, cardnumber, totalpay, paydate):
        conn = sqlite3.connect('services.db')
        c = conn.cursor()
        try:
            s = '%d-%02d-%02d' % (paydate.year, paydate.month, paydate.day)
            t = float('.'.join(str(elem) for elem in totalpay))
            entities = (float(barcode), cardnumber, t, s)
            c.execute('''INSERT INTO transactions(barcode, cardnumber, totalpay, paydate) VALUES(?, ?, ?, ?)''',
                      entities)
            c.execute('''UPDATE payables SET paymentstatus = 'pagado' WHERE barcode = {}'''.format(barcode))
            conn.commit()
            conn.close()

        except sqlite3.Error as error:
            print("Problema de conexión con la base de datos. ", error)

        finally:
            if conn:
                conn.close()

    # Return the amout to pay for the selected tax
    def amount(self, barcode):
        conn = sqlite3.connect('services.db')
        c = conn.cursor()
        try:
            c.execute('''SELECT amount FROM payables WHERE barcode = {}'''.format(barcode))
            amount = c.fetchone()
            conn.commit()
            conn.close()
            return amount

        except sqlite3.Error as error:
            print("Problema de conexión con la base de datos. ", error)

        finally:
            if conn:
                conn.close()

    # Return the list of taxes listed for selected past days
    def filterbydays(self, days):
        conn = sqlite3.connect('services.db')
        c = conn.cursor()
        try:
            c.execute('''select * from payables where expirationdate >= date('now', '-{} DAYS') and paymentstatus = 'impago' '''.format(days))
            taxes = c.fetchall()
            conn.commit()
            conn.close()
            return taxes

        except sqlite3.Error as error:
            print("Problema de conexión con la base de datos. ", error)

        finally:
            if conn:
                conn.close()

    # Return specific taxes for service type
    def filterbytype(self, type):
        conn = sqlite3.connect('services.db')
        c = conn.cursor()
        try:
            c.execute('''select * from payables where servicetype = '{}'3 and paymentstatus = 'impago' '''.format(type))
            taxes = c.fetchall()
            conn.commit()
            conn.close()
            return taxes

        except sqlite3.Error as error:
            print("Problema de conexión con la base de datos. ", error)

        finally:
            if conn:
                conn.close()