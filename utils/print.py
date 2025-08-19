# this will be the print function
import os, subprocess, platform


# This function will prepare data from stickers and call another function that creates txt
def stickers_to_txt(submaster):
    stickers_to_print = ""
    for sticker in submaster.stickers:
        if stickers_to_print == "":
            stickers_to_print = submaster.stickers[sticker].get_label_text()
        else:
            stickers_to_print = (
                stickers_to_print + "\n" + submaster.stickers[sticker].get_label_text()
            )
    print(f"Stickers to print from print.py: \n{stickers_to_print}")
    create_txt(stickers_to_print)


# This function creates txt file from the sticker_to_txt input
def create_txt(text_to_file):
    file_for_text = "print_list.txt"
    if os.path.exists(file_for_text):
        os.remove(file_for_text)
    with open(file_for_text, "a") as f:
        f.write(text_to_file)
        open_text_file()

    print("Hotovo... asi")

def open_text_file():
    if platform.system() == "Darwin":
        subprocess.call(("open", "print_list.txt"))
    elif platform.system() == "Windows":
        os.startfile("print_list.txt")
    else:
        subprocess.call(("xdg-open", "print_list.txt"))