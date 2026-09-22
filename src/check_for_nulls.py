def check_for_nulls(dataset):
    mandatory_columns = ["LongName","playerUrl","Nationality","Positions","Name","Age","↓OVA","ID","Height","Weight","foot","Growth"]
    cleaned_dataset = []
    nulls = []
    for player in dataset:
        for field, value in player.items():
            if value == None or value == "N/A" :
                player[field] = None
            if field in mandatory_columns:
                if player[field] == None:
                    print(f"Player {player["Name"]} miss some important info, for that reason will be removed from the dataset!")
                    continue
        cleaned_dataset.append(player)
    return cleaned_dataset