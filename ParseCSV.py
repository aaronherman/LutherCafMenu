import datetime
import calendar
import copy
import pytz
from pytz import timezone

def setUpDictionary():
    menu = {}
    
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    meals = ["Brunch", "Breakfast", "Lunch", "Dinner"]
    areas = ["Hot Cereals", "Omelet", "Breakfast", "Grab and Go", "Comfort", "Simple Servings",
             "Vegan Entree", "Grill", "Pizza", "Pasta", "Deli", "Salad", "Vegan Bar", 
             "Exhibition", "Special", "Soups"]
    
    for day in days:
        menu[day] = {}
        for meal in meals:
            if day == 'Sunday':
                if meal != 'Lunch' and meal != 'Breakfast':
                    menu[day][meal] = {}
                    for area in areas:
                        menu[day][meal][area] = []                    
            else:
                if meal != 'Brunch':
                    menu[day][meal] = {}
                    for area in areas:
                        menu[day][meal][area] = []                    
                
    return menu


def populateMenu(menu):
    f = open("caf_menu.csv", "r")
    start = False
    dontInclude = False
    
    for line in f:
        if start:
            line = line.split(",")
            date = line[6]
            
            year = ""
            for x in range(0,4):
                year += date[x+1]
            month = ""
            for x in range(0,2):
                month += date[x+5]
            day = ""
            for x in range(0,2):
                day += date[x+7]
            
            x = datetime.date(int(year), int(month), int(day)).weekday()
            day = calendar.day_name[x]
            
            meal = line[7]
            meal = meal.strip('"')

            digits = ["0","1","2","3","4","5","6","7","8","9"]
            
            area = line[8]
            area = area[12:-1]
            if "*" in area:
                firstStar = area.index("*")
                area = area[:firstStar]
            area = area.strip()
            if area[:4] == "Misc":
                dontInclude = True
            if area == "":
                dontInclude = True
            elif area[0] in digits:
                dontInclude = True            
            elif area[0] == "B":
                area = "Breakfast"
            elif area == "G&G":
                area = "Grab and Go"
            elif area == "G & G":
                area = "Grab and Go"
            elif area == "Grab n Go":
                area = "Grab and Go"
            elif area == "Salads":
                area = "Salad"
            elif area == "Simple Serving":
                area = "Simple Servings"
            elif area == "Special Function":
                area = "Special"
        
            area = area.rstrip()
        
            index = 9
            food = line[index]
            while (food[1] not in digits) or (food[2] not in digits) or (food[3] not in digits):
                index += 1
                food = line[index]   
            index += 1
            food = line[index]
            food = food.strip('"')
            if not dontInclude:
                menu[day][meal][area].append(food)

        start = True  
        dontInclude = False
        
    return menu

def removeEmptyLines(menu):
    newMenu = copy.deepcopy(menu)
    for day in newMenu:
        for meal in newMenu[day]:
            for area in newMenu[day][meal]:
                if len(newMenu[day][meal][area]) == 0:
                    del menu[day][meal][area]  
    
    return menu

def getWeek():
    return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def getMeals():
    return ["Breakfast", "Brunch","Lunch","Dinner"]

def getDay():
    time = datetime.datetime.now(timezone('America/Chicago'))
    intDay = time.today().weekday()
    day = calendar.day_name[intDay]
    return day

def getCurrentMeal():
    day = getDay()
    time = datetime.datetime.now(timezone('America/Chicago'))
    hour = datetime.datetime.strftime(time, "%H")
    hour = int(hour)
    if day != "Sunday":
        if hour < 10:
            return "Breakfast"
        elif hour < 15:
            return "Lunch"
        else: 
            return "Dinner"
    else:
        if hour < 15:
            return "Brunch"
        else:
            return "Dinner"

def main():

    menu = setUpDictionary()
    menu = populateMenu(menu)
    menu = removeEmptyLines(menu)
    
    currentMeal = getCurrentMeal()
    intDay = datetime.datetime.today().weekday()
    day = calendar.day_name[intDay]
    
if __name__ == "__main__":
    main()
  