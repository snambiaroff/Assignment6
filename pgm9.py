def calculate_total_cost(quantity, unit_price):
  

  total_cost = quantity * unit_price

  if total_cost > 1000:
    discount = total_cost * 0.1
    total_cost -= discount

  return total_cost

