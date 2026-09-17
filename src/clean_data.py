def clean_data(dataset):
    for player in dataset:
        for field, value in player.items():
            player[field] = value.strip().replace("\n", " ").replace("★","").strip()
            if field == "Height":
                convert_height(player,field)
            if field == "Weight":
                convert_weight(player,field)
            if field == "Value" or field == "Wage" or field == "Release Clause":
                convert_money(player,field)
            if value.isdigit():
                player[field] = int(value) 
            
    return dataset

def convert_height(player,field):
    player[field] = player[field].replace('"',"")
    height = player[field].split("'")
    if height[0].isdigit() and height[1].isdigit():  
        player[field] = round((float(height[0]) * 0.3048) + (float(height[-1]) * 0.0254),2)
    else:
        print("Height not valid!")

def convert_weight(player,field):
    player[field] = player[field].replace("lbs", "")
    if player[field].isdigit():
        player[field] = round(float(player[field]) * 0.453592,2)
    else:
        print("Weight not valid!")

def convert_money(player,field):
    try:
        multipliers = {"K": 1000, "M":1000000}
        sufix = player[field][-1]
        player[field] = player[field].replace("€","")
        if sufix in multipliers.keys():
            player[field] = round(float(player[field].replace(sufix, "")) * multipliers[sufix])
    except Exception as e:
        print("Error while converting money:", e)