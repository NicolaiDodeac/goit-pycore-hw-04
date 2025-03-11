def total_salary(path):
    try:
        with open(path, 'r') as fh:
            lines_amount = 0
            salaries = []
            for el in fh.readlines():
                lines_amount +=1
                _, salary = el.strip().split(",")
                salaries.append(float(salary))
        total = sum(salaries)
        average = total / lines_amount if lines_amount else 0
        return (int(total), int(average))
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return "?", "?"

total, average = total_salary("./salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
