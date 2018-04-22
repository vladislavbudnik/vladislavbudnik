usd = 57
euro = 60
kron = 3
yen = 2

def evr(money, currency):
	if currency == 400:
    		cache = round(money / usd, 2)
    		return cache
	elif currency == 401:
    		cache = round(money / euro, 2)
    		return cache
	elif currency == 402:
		cache = round(money / kron, 2)
		return cache
	elif currency == 403:
		cache = round(money / yen, 2)
		return cache
