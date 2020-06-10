import requests, json

def parse(r, symbol):
	delimiter = '"QuoteSummaryStore":{'
	quote = r.text.split(delimiter)[1] # Trim to the start
	quote = quote.split('(this)')[0][:-3] # Trim the gargabe at the end
	
	quote = quote.split(',"symbol":"%s","esgScores":' % symbol)[0]
	quote = '{%s}' % quote

	with open('data/{}.quote.json'.format(symbol), 'w') as f:
		f.write(quote)

	return json.loads(quote)

def get_quote(symbol):
	r = requests.get('https://finance.yahoo.com/quote/{}'.format(symbol))
	return parse(r, symbol)	

def get_sp500():
	with open('data/sp500.csv') as f:
		return list(map(lambda x: x[:-1], f.readlines()))

tickers = get_sp500()
print(tickers)
print('len: {}'.format(len(tickers)))

get_quote(tickers[0]) # MMM (3M)
