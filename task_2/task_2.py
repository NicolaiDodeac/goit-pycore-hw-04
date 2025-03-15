def get_cats_info(path):
    cats_list = []
    try:
        with open(path, "r", encoding='utf-8') as cats: 
            for cat in cats:
                try:
                    id_info, name_info, age_info = cat.strip().rsplit(",")
                    cat_info = {"id": id_info, "name": name_info, "age": age_info}
                    cats_list.append(cat_info)
                except ValueError:
                    print(f"Некоректний формат рядка: '{cat}'")
        return cats_list
    
    except FileNotFoundError:
        print(f"Файл не знайдено, перевірте шлях: {path}")
        return []

cats_info = get_cats_info("./task_2/cats_file.txt")
print(cats_info)
