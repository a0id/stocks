import requests, json

def parse(r, symbol):
	delimiter = '"QuoteSummaryStore":{'
	quote = r.text.split(delimiter)[1] # Trim to the start
	quote = quote.split('(this)')[0][:-3] # Trim the gargabe at the end
	
	quote = quote.split(',"symbol":"%s","esgScores":' % symbol)[0]
	quote = '{%s}' % quote

	with open('data/{}.quote.json'.format(symbol), 'w') as f:
		f.write(quote)
	
	print('parsed {}'.format(symbol))
	return json.loads(quote)

def get_quote(symbol):
	r = requests.get('https://finance.yahoo.com/quote/{}'.format(symbol))
	return parse(r, symbol)	

def get_sp500():
	with open('data/sp500.csv') as f:
		return list(map(lambda x: x[:-1], f.readlines()))

def select_data(q):
	data = {
		'symbol': q['price']['symbol'],
		'general': {
			'profitMargins': q['defaultKeyStatistics']['profitMargins']['fmt'],
			'52weekChange': q['defaultKeyStatistics']['52WeekChange']['fmt'],
			'sharesOutstanding': q['defaultKeyStatistics']['sharesOutstanding']['longFmt'],
		},
		'info': {
			'companyName': q['quoteType']['longName'],
			'sector': q['summaryProfile']['sector'],
			'industry': q['summaryProfile']['industry'],
			'employees': q['summaryProfile']['fullTimeEmployees'],
			'summary': q['summaryProfile']['longBusinessSummary'],
			'website': q['summaryProfile']['website'],
		},
		'price': {
			'price': q['price']['regularMarketPrice']['fmt'],
			'marketOpen': q['price']['regularMarketOpen']['fmt'],
			'dayHigh': q['price']['regularMarketDayHigh'],
			'dayLow': q['price']['regularMarketDayLow'],
			'dollarChange': q['price']['regularMarketChange']['fmt'],
			'percentChange': q['price']['regularMarketChangePercent']['fmt'],
			'volume': q['price']['regularMarketVolume']['longFmt'],
			'marketCap': q['price']['marketCap']['longFmt'],
		},
		'financialData': {
			'freeCashflow': q['financialData']['freeCashflow']['longFmt'],
			'earningsGrowth': q['financialData']['earningsGrowth']['fmt'],
			'returnOnAssets': q['financialData']['returnOnAssets']['fmt'],
			'totalRevenue': q['financialData']['totalRevenue']['longFmt'],
		}
	}
	return data

def bprint(obj):
	print(json.dumps(obj, indent=4))

'''
tickers = get_sp500()
for ticker in tickers:
	get_quote(ticker)
'''

t = 'MSFT'
bprint(select_data(get_quote(t)))

