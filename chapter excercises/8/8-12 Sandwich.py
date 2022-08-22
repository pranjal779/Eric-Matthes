def sandwich(first, last, **order):
    order['First Name'] = first,
    order['Last Name'] = last,
    return order


order_details = sandwich('Pranjal', 'Shukla',
                         item_1="Burger",
                         item_2="coca-cola")
order_details2 = sandwich('court', 'Sleepy',
                         item_1="sandwich",
                         item_2="orange juice")

order_details3 = sandwich('xanr', 'unar',
                         item_1="chicken",
                         item_2="chili-sauce")

print(order_details)
print(order_details2)
print(order_details3)


def order2(**items_in_menu):
    return items_in_menu


menu_item1 = order2(item1="cupcakes", item2="coffe", item3="gralic breads")
menu_item2 = order2(item1="iii", item2="rasgula", item3="maggi")

print(menu_item1)
print(menu_item2)
