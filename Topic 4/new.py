geek = {"404": "clueless.  From the web error message 404, meaning page not found.",
        "Googling": "searching the Internet for background information on a person.",
        "Keyboard Plaque": "the collection of debris found in computer keyboards.",
        "Link Rot": "the process by which web page links become obsolete.",
        "Percussive Maintenance": "the act of striking an electronic device to make it work.",
        "Uninstalled": "being fired.  Especially popular during the dot-bomb era."}
print(geek["404"])

if "404" in geek:
    print("Я знаю. что такое 404")
else:
    print("Я понятия не имею. что такое Dancing Baloney.")

print(geek.get("4041"))

print(geek.keys())
print(geek.values())
print(geek.items())