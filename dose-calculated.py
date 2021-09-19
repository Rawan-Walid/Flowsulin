import json
import math

with open("food.json") as file:
    data = json.load(file)

    meal = input("What will you eat")

    for meal in data["food"]:

        s = meal["carb_percent"]


weight = float(input ( "what's your weight?"))
InsulinRequirement = 0.55* weight
BasalInsulin = 0.45*InsulinRequirement
carb_cover = 500/ InsulinRequirement
CorrectionFactor = 1800 /InsulinRequirement



quantity = float(input("how much you will eat"))
carbs = quantity* float(s)

CHOinsulin = carbs/carb_cover

blood = float(input("what's your blood sugar?"))
blood_diff= blood - 80
HBinsulin = blood_diff/ CorrectionFactor

Total_dose = CHOinsulin + HBinsulin
TotalDose = math.ceil(Total_dose)

carb_record= []
insulin_record =[]

carb_record.append(quantity)
insulin_record.append(Total_dose)
print ("your total dose is " + str(Total_dose))
print ("approximately " + str(TotalDose))
print (insulin_record)
