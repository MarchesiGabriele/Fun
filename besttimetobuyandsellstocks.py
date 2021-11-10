def main():
    prices = [7,6,4,3,2,1]
    print(maxProfit(prices))
    
def maxProfit(prices):
    tot = 0
    prezzoPagato = 0
    stock = False

    for index in range(len(prices)):
    
        if (index+1)<len(prices):
            if prices[index] > prices[index+1]:
                #se ho una stock la vendo altrimenti non faccio nulla
                if stock: 
                   tot = tot + prices[index]-prezzoPagato
                   stock = False
            else:
                #Compro
                if not stock:
                    prezzoPagato = prices[index]
                    stock = True

        else:
            if stock:
                tot = tot + prices[index] - prezzoPagato

    return tot


if __name__ == "__main__":
    main()
