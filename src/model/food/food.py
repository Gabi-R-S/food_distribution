class FoodItem:
    def __init__(self, type, created_at, time_to_expire):
        self.type = type
        self.created_at = created_at
        self.time_to_expire = time_to_expire

    def __eq__(self, other):
        if not isinstance(other, FoodItem):
            return NotImplemented
        return (
            self.type == other.type and
            self.created_at == other.created_at and
            self.time_to_expire == other.time_to_expire
        )

    def __hash__(self):
        return hash((self.type, self.created_at, self.time_to_expire))