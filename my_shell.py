# >>> from shop.models import *
# >>> item_dictionary = {"apple": 300, "banana": 400, "orange": 250, "melon": 500, "onion": 200}
# >>> for k, v in item_dictionary.items():
# ...     Item.objects.create(name=k, price=v)
# ...
# >>> from random import randrange
# >>> purchase_dictionary = {"Kubat": 19, "Azamat": 18, "Elnur": 17, "Daun": 21, "Animal": 35}
# >>> item_count = len(Item.objects.all())
# >>> for k, v in purchase_dictionary.items():
# ...     Purchase.objects.create(name=k, age=v, item_id=randrange(1, item_count+1))
# ...
# >>> exit()

# В базе данных в shop_purchase 8 элементов так как когда кое что проверял добавлял первые 3 элемента,
# а с 4 по 8 это через итерацию в коде выше
