all_items=list()

dict1= {"item_id":10,"item_name":"Fruits"}
all_items.append(dict1)



def add_data_to_list(item):
    all_items.append(item)


def find_item_by_id(item_id):
    for dict in all_items :
        for item in dict:
            if(item["item_id"]==item_id):
                return item
