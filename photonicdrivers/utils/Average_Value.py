    
class Average_Value:
    def __init__(self, value, standard_deviation, unit):
        self.value: float = value
        self.standard_deviation: float = standard_deviation
        self.confidence_interval: Range = Range(self.value - self.standard_deviation, self.value + self.standard_deviation)
        self.unit: str = unit
    
    def __repr__(self):
        return f"Average_Value({self.value}+-{self.standard_deviation} {self.unit})"