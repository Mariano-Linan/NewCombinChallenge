# This class handles the filter to show the current bills to pay

import DatabaseManager


class ServiceFilter():

    def __init__(self):
        pass

    def consultbydays(self, days):
        db = DatabaseManager.DatabaseManager()
        taxes = db.filterbydays(days)
        print(taxes)

    def consultbytype(self,type):
        db = DatabaseManager.DatabaseManager()
        taxes = db.filterbytype(type)
        print(taxes)
