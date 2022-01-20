class File(object):
    def __init__(self, num_client : str, num_produit : str, qte : str, price : str, tax : str = None):
        self.num_client = num_client
        self.num_produit = num_produit
        self.qte = qte
        self.price = price
        self.tax = tax