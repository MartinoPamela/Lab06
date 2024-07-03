from database.DB_connect import DBConnect
from model.retailer import Retailer


class RetailerssDao:

    def get_retailers(self, retailers_map) -> set[Retailer] | None:
        """
        Function that reads the retailers present in the database and returns them.
        :param retailers_map: It is a dictionary that maps retailer_codes to Retailer objects. It is
        populated by this function.
        :return: A set of Retailers, or None if there are connection errors.
        """
        cnx = DBConnect.get_connection()
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT *
                FROM go_retailers"""
            cursor.execute(query)
            result = set()
            for row in cursor.fetchall():
                read_retailer = Retailer(row["Retailer_code"],
                                         row["Retailer_name"],
                                         row["Type"],
                                         row["Country"])
                result.add(read_retailer)
                retailers_map[read_retailer.retailer_code] = read_retailer
            cursor.close()
            cnx.close()
            return result
        else:
            print("Errore nella connessione")
            return None