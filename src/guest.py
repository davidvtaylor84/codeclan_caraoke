class Guest:
    
    def __init__(self, guest_name, wallet, favourite_song):
        self.guest_name = guest_name
        self.wallet = wallet
        self.favourite_song = favourite_song

    def pay_for_room(self, room, guest):
        if self.wallet >= room.room_price:
            self.wallet -= room.room_price
            return self.wallet
        else:
            return "You don't have enough money"

    def my_favourite_song(self, room, guest):
        if self.favourite_song in room.song_list:
            return "Yes! This is my jam!"
        else:
            return "Meh.."

