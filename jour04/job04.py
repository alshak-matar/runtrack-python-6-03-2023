def add_fruits(fruit_list):
    fruit_list.insert(2, "Mangue")
    return fruit_list
fruits = ["pomme", "cerise", "orange", "molen"]
updated_fruits = add_fruits(fruits)
print(updated_fruits)
