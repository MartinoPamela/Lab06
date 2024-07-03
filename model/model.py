from database.products_dao import ProductsDao
from database.sales_dao import SalesDao
from database.retailers_dao import RetailerssDao
from model import sale
from model.retailer import Retailer
from model.sale import Sale


class Model:
    def __init__(self):
        self._sales_dao = SalesDao()
        self._products_dao = ProductsDao()
        self._retailers_dao = RetailerssDao()
        self.retailers_map = {}

    def get_years(self):
        return self._sales_dao.get_years()

    def get_brands(self):
        return self._products_dao.get_brands()

    def get_retailers(self) -> set[Retailer]:
        return self._retailers_dao.get_retailers(self.retailers_map)

    def get_top_sales(self, anno, brand, retailer_code) -> list[Sale]:
        filtered_sales = self._sales_dao.get_filtered_sales(anno, brand, retailer_code)
        filtered_sales.sort(reverse=True)
        return filtered_sales[0:5]

    def get_sales_stats(self, anno, brand, retailer_code):
        filtered_sales = self._sales_dao.get_filtered_sales(anno, brand, retailer_code)
        ricavo_totale = sum([sale.ricavo for sale in filtered_sales])
        retailers_involved = set([sale.retailer_code for sale in filtered_sales])
        product_involved = set([sale.product_number for sale in filtered_sales])
        return ricavo_totale, len(filtered_sales), len(retailers_involved), len(product_involved)
