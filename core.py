all_items=[]
from typing import List, Dict

dict1= {"item_id":10,"item_name":"Fruits"}


all_items.append(dict1)


def add_multiple_items(items:List[Dict]):
    global all_items
    print("Item is going to add ",items)
    all_items.extend(items)
    return True

def find_item_by_id(item_id):
    for item in all_items :
        if(item['item_id']==item_id):
                return("Item ", item)

