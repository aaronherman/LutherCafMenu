import datetime
import calendar
import copy

def setUpDictionary():
    menu = {}
    
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    meals = ["Breakfast", "Lunch", "Dinner", "Brunch"]
    areas = ["Hot Cereals", "Omelet", "Breakfast", "Grab and Go", "Comfort", "Simple Servings",
             "Vegan Entree", "Grill", "Pizza", "Pasta", "Deli", "Salad", "Vegan Bar", 
             "Exhibition"]
    
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
            
            if area == "":
                dontInclude = True
            elif area[0] in digits:
                dontInclude = True            
            elif area[0] == "B":
                area = "Breakfast"
            elif area == "G&G":
                area = "Grab and Go"
            elif area == "Salads":
                area = "Salad"
            
            area = area.rstrip()
        
            index = 9
            food = line[index]
            while food[1] not in digits:
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

def getDay():
    intDay = datetime.datetime.today().weekday()
    day = calendar.day_name[intDay]
    
    return day

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

def main():

    menu = setUpDictionary()
    menu = populateMenu(menu)
    menu = removeEmptyLines(menu)
    
    intDay = datetime.datetime.today().weekday()
    day = calendar.day_name[intDay]
    
if __name__ == "__main__":
    main()
  