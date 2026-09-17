def check_for_nulls(dataset):
    mandatory_columns = ["LongName","playerUrl","Nationality","Positions","Name","Age","↓OVA","ID","Height","Weight","foot","Growth"]
    for player in dataset:
        for field, value in player.items():
            if value == None or value == "N/A" :
                player[field] = None
            if field in mandatory_columns:
                if value == None:
                    print(f"Player {player["Name"]} miss some important info, for that reason will be removed from the dataset!")
                    dataset.remove(player)
    return dataset