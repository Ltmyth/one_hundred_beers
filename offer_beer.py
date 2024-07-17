def offer100beers():
    bottle_count = 100
    while bottle_count>0:
        print("\n\nHi friend!")
        print("\nWe still have",bottle_count,"out of the 100 bottles of beer left!")
        order = int(input("\nPlease enter the number of beers you want to drink:\n"))
        if order <= bottle_count:
            bottle_count -= order
        else:
            print("\nWe only had 100 beers banange!, We don't have enough for those!\n\nPlease try again\n")
        if bottle_count==0:
            print("\nWe need a refill banange!, The are no more beers to drink!\n")
            break
offer100beers()
