class StoreItem:
    __slots__ = ['name', 'price']
    def __init__(self, *args):
        for attr, value in zip(StoreItem.__slots__, args):
            setattr(self, attr, value)


chips = StoreItem("Chips", 1.99) # Don't modify this line

# TODO: Access the attributes of the chips object and display them
print(chips.name)
print(chips.price)

