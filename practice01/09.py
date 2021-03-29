# 문제9.
# 주어진 if 문을 dict를 사용해서 수정하세요.

menu = input('메뉴: ')
menu_dict = {}

if menu == '오뎅':
    menu_dict = {"오뎅": '300'}
elif menu == '순대':
    menu_dict = {'순대':'400'}
elif menu == '만두':
    menu_dict = {'만두':'500'}
else:
    menu_dict = {menu : "0"}

print('가격: {0}' .format(menu_dict[menu]))
