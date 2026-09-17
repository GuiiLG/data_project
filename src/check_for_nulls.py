def check_for_nulls(dataset):
    for player in dataset:
        for field, value in player.items():
            if value == None or value == "N/A" :
                player[field] = None
    return dataset