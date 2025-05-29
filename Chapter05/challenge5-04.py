me = {
    "height": "173",
    "fav_color": "red",
    "fav_food": "apple"
}

answer = input("Type height, fav_color or fav_food")
if answer in me:
    result = me[answer]
    print(result)
