# Values represent number of consumers.
consumers = {
    "sports-drink": 45000000,
    "antioxidant-pill": 5000000,
    "v7": 8000000,
}

# Keys represent $ amounts, value of keys represent percentage of consumers interested in buying the product.
prices = {
    "1.19": {
        "sports-drink": 8,
        "antioxidant-pill": 1,
        "v7": 1,
        "revenue": 0
    },
    "0.99": {
        "sports-drink": 15,
        "antioxidant-pill": 2,
        "v7": 2,
        "revenue": 0
    },
    "0.79": {
        "sports-drink": 20,
        "antioxidant-pill": 20,
        "v7": 2,
        "revenue": 0
    },
    "0.59": {
        "sports-drink": 22,
        "antioxidant-pill": 25,
        "v7": 5,
        "revenue": 0
    },
    "0.39": {
        "sports-drink": 22,
        "antioxidant-pill": 30,
        "v7": 6,
        "revenue": 0
    },
}

flavours = {
    "Yellowknife": {
        "sports-drink": 34,
        "antioxidant-pill": 20,
        "v7": 12,
        "revenue": 0
    },
    "Jasper Mountain": {
        "sports-drink": 31,
        "antioxidant-pill": 17,
        "v7": 24,
        "revenue": 0
    },
    "Whistler": {
        "sports-drink": 25,
        "antioxidant-pill": 20,
        "v7": 10,
        "revenue": 0
    },
    "Alberta Bound": {
        "sports-drink": 10,
        "antioxidant-pill": 21,
        "v7": 50,
        "revenue": 0
    },
    "Yukon Gold": {
        "sports-drink": 5,
        "antioxidant-pill": 22,
        "v7": 4,
        "revenue": 0
    },
}

pricesList = []
flavourRevenues = []

# Finds revenue for each pricing option.
for keys, values in prices.items():
    for consumerType, consumerPercent in values.items():
        currentRevenue = prices[keys]['revenue']
        if consumerType == 'revenue':
            pass
        else:
            # Multiplying by 104 to account for repeat purchases (2 four packs per every 4 weeks = 104 bottles)
            addedRevenue = ((consumerPercent/100)*consumers[consumerType])*(float(keys)*104)
            prices[keys]['revenue'] = currentRevenue + addedRevenue
    print("${0} will generate ${1} in revenue.".format(keys, values['revenue']))
    pricesList.append([keys, values['revenue']])

# Finds revenues for each flavours.

for keys, values, in flavours.items():
    for consumerType, consumerPercent in values.items():
        # Takes the consumer percent for the flavour, and finds its percentage for our optimal price (0.79).
        # i.e 34% of the 8% for sports drink consumers.
        if consumerType == 'revenue':
            pass
        else:
            consumerPercentReal = prices['0.79'][consumerType]*(consumerPercent/100)
            consumerPercentTotal = (consumerPercentReal/100) * consumers[consumerType]
            flavourRevenue = consumerPercentTotal * (0.79*104)
            currentRevenue = flavours[keys]['revenue']
            flavours[keys]['revenue'] = currentRevenue + flavourRevenue
    flavourRevenues.append([keys, values['revenue']])


# Sorts pricesList and flavourRevenues by 2nd element.
def second(elem):
    return elem[1]
pricesList.sort(reverse=True, key=second)
flavourRevenues.sort(reverse=True, key=second)

optimalPrice=pricesList[0][0]
optimalPriceRevenue = pricesList[0][1]

print("The most optimal price is ${0}, generating ${1} in revenue. \n".format(optimalPrice, optimalPriceRevenue))
print("Revenues should be prioritized in the following order:")
for i in range(len(flavourRevenues)):
    print("{0}. {1} generates ${2} in revenue".format(i+1, flavourRevenues[i][0], flavourRevenues[i][1]))

