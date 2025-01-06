def cus_join(separator:str,items:list) -> str:
    if not items:
        return  ""
    result = items[0]
    for item in items[1:]:
        result += separator + item

    return result


print(cus_join(" ",["hel","gh"]))
print(cus_join(",",["gel","hii"]))




























