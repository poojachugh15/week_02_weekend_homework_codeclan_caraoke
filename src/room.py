class Room:
        
    def __init__(self, name, till, entry_fee ):
        self.name = name
        self.till = till
        self.songs = []
        self.guests = []
        self.number_of_spaces = 5
        self.entry_fee = entry_fee
        
    
    def songs_count(self):
        return len(self.songs)
    
    
    def add_songs(self, song):
       self.songs.append(song)
       
    def guest_count(self):
            return len(self.guests)
        
     
    def check_in(self, guest_check_in): 
        if self.guests.count(guest_check_in) > 5:
            return "Guest is not allowed to check-in"
        self.guests.append(guest_check_in)
        return "Guest is allowed to check-in"   
   
   
    def check_out(self, guest_check_out):
        self.guests.remove(guest_check_out)
        
    
    def check_in_increase_amount(self, check_in_guest):  
        self.till += check_in_guest.entry_fee
    
        