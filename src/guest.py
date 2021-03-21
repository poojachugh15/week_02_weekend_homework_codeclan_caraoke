class Guest:
    
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        
    
    
    def check_in_decrease_amount(self, check_in_guest):
        self.wallet -= check_in_guest.entry_fee