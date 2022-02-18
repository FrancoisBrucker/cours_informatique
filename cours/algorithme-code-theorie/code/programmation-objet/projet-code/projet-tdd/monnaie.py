class Dollar:
    def __init__(self, montant):
        self.montant = montant

    def fois(self, multiplicateur):
        self.montant *= multiplicateur
