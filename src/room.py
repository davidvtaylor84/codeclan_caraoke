class Room:
    
    def __init__(self, room_name, room_capacity, room_price):
        self.room_name = room_name
        self.room_capacity = room_capacity
        self.room_price = room_price
        self.guests_in_room = []
        self.song_list = []

    # def check_in_guests(self, customer, karaoke_room):
    #     if karaoke_room == self.room_name:
    #         self.guests_in_room.append(customer)
    #     return self.guests_in_room

    def check_in_guests(self, customer):
        self.guests_in_room.append(customer)
        return self.guests_in_room

    def check_out_guests(self, customer):
        self.guests_in_room.remove(customer)
        return self.guests_in_room

    def add_song_to_room(self, song):
        self.song_list.append(song)
        return self.song_list