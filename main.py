import re
str2 = """
Subhan contact number is : 0323 1229935
Ahmad contact number is : 0325-0491734
Hassaan contact number is : +92 326 4132946
Azeem chachu number is : 0300 4300176
Mustanser chachu number is : 03224590922
"""
re_for_num = re.compile(r"03[0-4][0-9]\s[0-9]{7}|"+"92\s3[0-4][0-9]\s[0-9]{7}|03[0-4][0-9]-[0-9]{7}|03[0-4][0-9]{8}")
matches1 = re_for_num.finditer(str2)
for match in matches1:
    print(match)