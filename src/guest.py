class Guest:
    
    def __init__(self, guest_name, wallet):
        self.guest_name = guest_name
        self.wallet = wallet

    def pay_for_room(self, room, guest):
        if self.wallet >= room.room_price:
            self.wallet -= room.room_price
            return self.wallet
        else:
            return "You don't have enough money"

