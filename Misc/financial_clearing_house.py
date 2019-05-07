transactions = [
  {"payee": "BoA", "amount": 132, "payer": "Chase"},
  {"payee": "BoA", "amount": 827, "payer": "Chase"},
  {"payee": "Well Fargo", "amount": 751, "payer": "BoA"},
  {"payee": "BoA", "amount": 585, "payer": "Chase"},
  {"payee": "Chase", "amount": 877, "payer": "Well Fargo"},
  {"payee": "Well Fargo", "amount": 157, "payer": "Chase"},
  {"payee": "Well Fargo", "amount": 904, "payer": "Chase"},
  {"payee": "Chase", "amount": 548, "payer": "Well Fargo"},
  {"payee": "Chase", "amount": 976, "payer": "BoA"},
  {"payee": "BoA", "amount": 872, "payer": "Well Fargo"},
  {"payee": "Well Fargo", "amount": 571, "payer": "Chase"}
]

def normalize_data(transactions):
	for transaction in transactions:
		if transaction["payee"] > transaction["payer"]:
			temp = transaction["payee"]
			transaction["payee"] = transaction["payer"]
			transaction["payer"] = temp
			transaction["amount"] = -transaction["amount"]
	return transactions


def financially_clear(transactions):
	normalized_transactions = normalize_data(transactions)
	m = {}
	for transaction in normalized_transactions:
		key = str(transaction["payee"]) + str(transaction["payer"])
		if key not in m:
			m[key] = transaction["amount"]
		else:
			m[key] += transaction["amount"]	
	return m

print financially_clear(transactions)
