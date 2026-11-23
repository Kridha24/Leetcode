class ProductOfNumbers:
    def __init__(self):
        # Sentinel 1 allows computing the product of all elements since the last 0
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # Any future window reaching this 0 will have a product of 0
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-1 - k]