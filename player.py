from items import *
from map import rooms

inventory = [item_id, item_laptop, item_money]
mass = items['laptop']['mass'] + items['id']['mass'] + items['money']['mass']
min_mass = 0
max_mass = 3000
# Start game at the reception
current_room = rooms["Reception"]
