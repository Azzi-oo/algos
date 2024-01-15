def hex_string_to_RGB(hex_string): 
    # your code here
    # Преобразование шестнадцатеричной строки в десятичное число
    red = int(hex_string[1:3], 16)
    green = int(hex_string[3:5], 16)
    blue = int(hex_string[5:7], 16)
    
    # Установка значений RGB в словаре
    rgb = {"r": red, "g": green, "b": blue}
    
    return rgb
