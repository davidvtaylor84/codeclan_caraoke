class Room:
    
    def __init__(self, room_name, room_capacity, room_price):
        self.room_name = room_name
        self.room_capacity = room_capacity
        self.room_price = room_price
        self.guests_in_room = []
        self.song_list = []
