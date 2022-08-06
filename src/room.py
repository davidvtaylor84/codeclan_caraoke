class Room:
    
    def __init__(self, room_name, room_capacity, room_price):
        self.room_name = room_name
        self.room_capacity = room_capacity
        self.room_price = room_price
        self.guests_in_room = []
        self.song_list = []
        self.drinks_tab = float(0)
        self.drinks_list = []

    def check_in_guests(self, customer):
        self.guests_in_room.append(customer)
        return self.guests_in_room

    def check_out_guests(self, customer):
        self.guests_in_room.remove(customer)
        return self.guests_in_room

    def add_song_to_room(self, song):
        self.song_list.append(song)
        return self.song_list

    def room_capacity_check(self, room):
        if len(self.guests_in_room) > self.room_capacity:
            return "ROOM CAPACITY EXCEEDED"
        else:
            return "Acceptable number of people in room. Sing away!"

    def add_to_tab(self, room, drink_price):
        self.drinks_tab += drink_price
        return self.drinks_tab

    # EXTRA FUNCTION:
    # ONCE THE BAR TAB REACHES £150, THE SONG, 
    #"BIG SPENDER" BY SHIRLEY BASSEY, IS LOADED ONTO THEIR SONG LIST.

    def big_spender(self):
        if self.drinks_tab >= 150.00:
            self.add_song_to_room("Big Spender by Shirley Bassey")
        