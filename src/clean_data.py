def clean_data(datasets):
    for player in datasets["fifa21_raw_data"]:
        for field, value in player.items():
            player[field] = value.strip().replace("\n", " ").replace("★","").strip()
            multipliers = {"K": 1000, "M":1000000}
            if field == "Height":
                player[field] = player[field].replace('"',"")
                height = player[field].split("'")
                player[field] = round((float(height[0]) * 0.3048) + (float(height[-1]) * 0.0254),2)
            if field == "Weight":
                player[field] = player[field].replace("lbs", "")
                player[field] = round(float(player[field]) * 0.453592,2)
            if field == "Value" or field == "Wage" or field == "Release Clause":
                sufix = player[field][-1]
                player[field] = player[field].replace("€","")
                if sufix in multipliers.keys():
                    player[field] = round(float(player[field].replace(sufix, "")) * multipliers[sufix])
            if value.isdigit():
                player[field] = int(value) 
        # print(player)
            
    return datasets