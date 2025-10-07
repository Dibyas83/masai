import json



def jd():
    lib = {"name":"city lib","books":[{"title":"book A","author":"a","year":1920},
                                      {"title":"book b","author":"b","year":1940}]}

    with open("lib.json","w") as f1:
        json.dump(lib,f1, indent=4)

    with open("lib.json", "r") as f1:
        loaded_lib = json.load(f1)

    for book in  loaded_lib["books"]:
        if book["year"] > 1919:
            print(book["title"])

jd()




















