class Stock():
	def __init__(self):
		self.symbol = None
		self.datetime = None
		self.price = None
		self.bid = None
		self.ask = None
		self.name = None
		self.beta = None
		self.dividends = None
		self.marketcap = None
		self.enterprisevalue = None
		self.numberbought = None
		self.pricebought = None
		self.market = None

	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	def setSymbol(self, symbol):
		self.symbol = symbol

	def getSymbol(self):
		return self.symbol

	def setDateTime(self, datetime):
		self.datetime = datetime

	def getDateTime(self):
		return self.datetime

	def setPrice(self, price):
		self.price = price

	def getPrice(self):
		return self.price

	def setAsk(self, ask):
		self.ask = ask

	def getAsk(self):
		return self.ask

	def setBid(self, bid):
		self.bid = bid

	def getBid(self):
		return self.bid

	def setDividends(self, dividends):
		self.dividends = dividends

	def getDividends(self):
		return self.dividends

	def setMarketcap(self, marketcap):
		self.marketcap = marketcap

	def getMarketcap(self):
		return self.marketcap

	def setBeta(self, beta):
		self.beta = beta

	def getBeta(self):
		return self.beta

	def setEnterprisevalue(self, enterprisevalue):
		self.enterprisevalue = enterprisevalue

	def getEnterprisevalue(self):
		return self.enterprisevalue

	def setNumberbought(self, numberbought):
		self.numberbought = numberbought

	def getNumberbought(self):
		return self.numberbought

	def setPricebought(self, pricebought):
		self.pricebought = pricebought

	def getPricebought(self):
		return self.pricebought

	def setMarket(self, market):
		self.market = market

	def getMarket(self):
		return self.market

	def toString(self):
		string = ""
		if (self.name != None):
			string = string + "\nStock name: " + self.name
		if (self.symbol != None):
			string = string + "\nTicker symbol: " + self.symbol
		if (self.market != None):
			string = string + "\nStock market: " + str(self.market)
		if (self.datetime != None):
			string = string + "\nUpdated: " + self.datetime
		if (self.price != None):
			string = string + "\nStock price: $" + str(self.price)
		if (self.bid != None):
			string = string + "\nBid price: $" + str(self.bid)
		if (self.ask != None):
			string = string + "\nAsk price: $" + str(self.ask)
		if (self.beta != None):
			string = string + "\nBeta: " + str(self.beta)
		if (self.dividends != None):
			string = string + "\nDividends: $" + str(self.dividends)
		if (self.marketcap != None):
			string = string + "\nMarket cap: $" + str(self.marketcap)
		if (self.enterprisevalue != None):
			string = string + "\nEnterprise value: $" + str(self.enterprisevalue)
		if (self.pricebought != None):
			string = string + "\nPrice bought: $" + str(self.pricebought)
		if (self.numberbought != None):
			string = string + "\nShares bought: " + str(self.numberbought)
		return string



