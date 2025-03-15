import sys
from pathlib import Path
from colorama import init, Fore, Style

def show_directory(path: Path, gap: str = ""):
    try:
        for item in sorted(path.iterdir()):
            if item.name.startswith('.'):
                continue
            if item.is_dir():
                print(f"{gap}{Fore.BLUE}{item.name}{Style.RESET_ALL}")
                show_directory(item, gap + "    ")
            else:
                print(f"{gap}{Fore.GREEN}{item.name}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Помилка: {e}{Style.RESET_ALL}")

def main():
    init(autoreset=True)
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Помилка: Необхідно вказати шлях до директорії.{Style.RESET_ALL}")
        return

    directory_path = Path(sys.argv[1])

    print(f"{Fore.YELLOW}Структура директорії: {directory_path}{Style.RESET_ALL}")
    show_directory(directory_path)

if __name__ == "__main__":
    main()

# path for command line: python task_3/task_3.py .

