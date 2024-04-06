from simple_term_menu import TerminalMenu


def goodbye():
    exit("\nSee you later, super star ⭐")


def create_options_menu(options: list):
    options_to_display = []
    for i, entry in enumerate(options):
        options_to_display.append(f"[⭑] {entry[0]}")
    return options_to_display


def show_menu(options: list, menu_title: str):
    options_for_display = create_options_menu(options)
    terminal_menu = TerminalMenu(options_for_display, title=menu_title)
    menu_entry_index = terminal_menu.show()
    entry_name = terminal_menu.chosen_menu_entry
    match entry_name:
        case "Main Menu":
            from sparking_stars import sparking_stars
            sparking_stars()
        case "Exit":
            goodbye()
        case _:
            return menu_entry_index
