class User():
    def __init__(self, name, market, start_amount = 0):
        self.name = name
        self.stocks = {}
        self.wallet = start_amount
        self.market = market
    def buy_stock(self, player, quantity):
        self.market.buyTransaction(player, quantity, self)
    def sell_stock(self, player, quantity):
        self.market.sellTransaction(player, quantity, self)
    def get_name(self):
        return self.name
    def get_wallet(self):
        return self.wallet
    def get_stocks(self):
        return self.stocks
    def set_name(self, name):
        self.name = name
    def set_wallet(self, amount):
        self.wallet = amount;
    def updateStock(self, player, amount):
        self.stocks[player.name] = amount
    
    



        
