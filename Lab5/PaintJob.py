def main():
  sqrFt = int(input("Enter wall space in square feet: "))
  paintCost = float(input("Enter paint price per gallon: "))
  paint(sqrFt, paintCost)
 
def paint(sqrFt, paintCost):
  FT_PER_GAL = 112
  LABOR_HRS = 8
  LABOR_CHARGE = 35
  paintGals = sqrFt / FT_PER_GAL
  labor = LABOR_HRS * paintGals
  paintCharge = paintGals * paintCost
  laborCost = labor * laborCharge
  total = paintCharge + laborCost
  totalCost(paintGals, labor, paintCharge, laborCost, total)
  
  
def totalCost(paintGals, labor, paintCharge, laborCost, total): 
  print('Gallons of paint:', format(paintGals, '.0f'))
  print('Hours of labor:', format(labor, '.0f'))
  print('Paint charges: $', format(paintCharge, '.2f')) 
  print('Labor charges: $', format(laborCost, '.2f'))  
  print('Total cost: $', format(total, '.2f'))  
  
main()
