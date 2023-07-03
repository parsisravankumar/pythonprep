"""A milk vendor buys milk at the rate of 3.25/lt then adds a litre of water for every
4 litres of milk and sells the water milk at the rate of 4.15/lt. Calculate the gain
for milk vendor."""
#Cost of buying milk:
#Cost of buying 'x' liters of milk at the rate of 3.25 per liter
milk_quantity = float(input("enter the number of liters"))
buying_cost = 3.25 * milk_quantity
water_quantity = milk_quantity // 4
diluted_quantity = milk_quantity + water_quantity
selling_price = 4.15 * diluted_quantity

gain = selling_price - buying_cost
print("Gain for the milk vendor:",gain)
