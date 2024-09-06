class Range:
    def __init__(self, min: float, max: float):
        if min > max:
            raise ValueError("The minimum value must be less than or equal to maximum value")
        self.min: float = min
        self.max: float = max

    def __repr__(self):
        return f"Range(min={self.min}, max={self.max})"

    def contains(self, value: float) -> bool:
        return self.min <= value <= self.max
