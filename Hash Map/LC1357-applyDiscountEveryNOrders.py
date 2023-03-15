class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.discount = discount
        self.id_to_amount = defaultdict(int)
        self.disc_n = n
        self.cur_n = 0

        for i in range(len(products)):
            self.id_to_amount[products[i]] = prices[i]

    def getBill(self, product: List[int], amount: List[int]) -> float:
        s = 0
        for i in range(len(product)):
            s += self.id_to_amount[product[i]] * amount[i]

        self.cur_n += 1
        if self.cur_n % self.disc_n == 0:
            return s * ((100 - self.discount) / 100)
        else:
            return s


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
