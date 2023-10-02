class Computer:
    def __init__(self, processor_name, processor_speed, memory_size):
        self.processor_name = processor_name
        self.processor_speed = processor_speed
        self.memory_size = memory_size

    def quality(self):
        return 0.1 * self.processor_speed + self.memory_size

class ComputerWithHDD(Computer):
    def __init__(self, processor_name, processor_speed, memory_size, hdd_size):
        super().__init__(processor_name, processor_speed, memory_size)
        self.hdd_size = hdd_size

    def quality(self):
        return super().quality() + 0.5 * self.hdd_size

comp = ComputerWithHDD("Intel Core i5", 3200, 8192, 1000)
quality = comp.quality()
print(f"Качество компьютера равно {quality}")