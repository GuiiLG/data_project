def clean_structure(datasets):
    for player in datasets["fifa21_raw_data"]:
        for field, value in player.items():
            player[field] = value.strip().replace("\n", " ")
            if value.isdigit():
                player[field] = int(value)
        print(player)   