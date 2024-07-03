import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._anno = None
        self._brand = None
        self._retailer_code = None

    def handle_top_vendite(self, e):
        top_vendite = self._model.get_top_sales(self._anno, self._brand, self._retailer_code)
        self._view.lst_result.controls.clear()
        if len(top_vendite) == 0:
            self._view.lst_result.controls.append(ft.Text("Nessuna vendita con i filtri selezionati"))
        else:
            for vendita in top_vendite:
                self._view.lst_result.controls.append(ft.Text(vendita))
        self._view.update_page()

    def handle_analizza_vendite(self, e):
        statistiche_vendite = self._model.get_sales_stats(self._anno, self._brand, self._retailer_code)
        self._view.lst_result.controls.clear()
        self._view.lst_result.controls.append(ft.Text("Statistiche vendite: "))
        self._view.lst_result.controls.append(ft.Text(f"Giro d'affari: {statistiche_vendite[0]}"))
        self._view.lst_result.controls.append(ft.Text(f"Numero vendite: {statistiche_vendite[1]}"))
        self._view.lst_result.controls.append(ft.Text(f"Numero retailers coinvolti: {statistiche_vendite[2]}"))
        self._view.lst_result.controls.append(ft.Text(f"Numero prodotti coinvolti: {statistiche_vendite[3]}"))
        self._view.update_page()

    def populate_dd_anno(self):
        anni = self._model.get_years()
        anni.sort()
        for anno in anni:
            self._view.dd_anno.options.append(ft.dropdown.Option(anno[0]))
        self._view.update_page()

    def read_anno(self, e):
        if e.control.value == "None":
            self._anno = None
        else:
            self._anno = e.control.value

    def populate_dd_brand(self):
        brands = self._model.get_brands()
        for brand in brands:
            self._view.dd_brand.options.append(ft.dropdown.Option(brand[0]))
        self._view.update_page()

    def read_brand(self, e):
        if e.control.value == "None":
            self._brand = None
        else:
            self._brand = e.control.value

    def populate_dd_retailer(self):
        retailers = self._model.get_retailers()
        for retailer in retailers:
            self._view.dd_retailer.options.append(ft.dropdown.Option(text=retailer.retailer_name,
                                                                     data=retailer,
                                                                     on_click=self.read_retailer))
        self._view.update_page()

    def read_retailer(self, e):
        if e.control.data is None:
            self._retailer_code = None
        else:
            self._retailer_code = e.control.data.retailer_code
