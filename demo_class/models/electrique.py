class Electrique():
    
    def definir(self, autonomie):
        self.autonomie_km = autonomie
        return f"Mode électrique défini (autonomie {self.autonomie_km})"

    def charger (self):
        return f"Charge en cours... autonomie : {self.autonomie_km}"