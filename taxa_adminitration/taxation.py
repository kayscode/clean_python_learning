products_price = [345.67, 435.67, 567.67]


def calculate_tax(products_prices):
    tax_somme = 0
    for price in products_prices:
        tax_somme += (price * 0.16)

    return tax_somme


def get_data_from_excel():
    pass


def get_data_from_csv():
    pass


def get_data_from_database():
    pass


class TaxManager:

    def create_tax_declaration(self, year):
        """
        some description about what my function do

        :param year:
        :return:
        """

    def get_tax_declaration_by(self, declaration_id):
        """
        some implementation of the code is there
        :param declaration_id:
        :return: 
        """
        pass
