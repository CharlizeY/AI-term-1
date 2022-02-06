fruit_market = dict()
fruit_market['apple'] = dict()
fruit_market['apple']['price'] = 1.2
fruit_market['apple']['promo'] = dict()
fruit_market['apple']['promo']['nth'] = 2
fruit_market['apple']['promo']['name'] = 'Buy one apple get one free'
fruit_market['apple']['promo']['discount'] = 0

fruit_market['plum'] = dict()
fruit_market['plum']['price'] = 0.8

fruit_market['pear'] = dict()
fruit_market['pear']['price'] = 1.0

fruit_market['pineapple'] = dict()
fruit_market['pineapple']['price'] = 2.5
fruit_market['pineapple']['promo'] = dict()
fruit_market['pineapple']['promo']['nth'] = 2
fruit_market['pineapple']['promo']['name'] = 'Get 50 pence off two pineapples'
fruit_market['pineapple']['promo']['discount'] = 0.5

fruit_market['kiwi'] = dict()
fruit_market['kiwi']['price'] = 0.4

fruit_market['mango'] = dict()
fruit_market['mango']['price'] = 1.4



def get_regular_cost_of_item(item) -> float:
    return fruit_market[item]['price']


def check_item_has_promo(item) -> bool:
    return fruit_market[item].get('promo') != None


def is_cheap(item) -> bool:
    return fruit_market[item]['price'] < 1.0


def show_cheap_items() -> list:
    return [item for item in fruit_market.keys() if is_cheap(item)]


def items_with_promos(fruit_list: list) -> list:
    dup_list = [item for item in fruit_list if check_item_has_promo(item)]
    nodup_list = list(set(dup_list))  
    return nodup_list      


def total_cost_without_promos(fruit_list: list) -> float:
    return sum([get_regular_cost_of_item(item) for item in fruit_list])


def total_cost_for_item_promo_buy_n_get_one_free(cost: float, number_items: int, number_promo_given: int) -> float:
    ''' promo function - buy n get one of them free '''

    num_of_offer = number_items//number_promo_given
    num_of_remaining_friut = number_items%number_promo_given
    total_cost = cost*(number_promo_given-1)*num_of_offer + cost*num_of_remaining_friut
    return total_cost


def total_cost_for_item_promo_buy_n_get_discount(cost: float, number_items: int, 
                                                 number_promo_given: int, discount: int) -> float:
    ''' promo function - buy n and get a discount '''

    num_of_offer = number_items//number_promo_given
    total_cost = cost*number_items - discount*num_of_offer
    return total_cost


def total_cost_with_promos_applied(fruit_list: list) -> float:
    counts = dict()
    for fruit in fruit_list:
        counts[fruit] = counts.get(fruit, 0) + 1

    list_of_item_costs = []
    
    for item in counts.keys():
        cost = get_regular_cost_of_item(item)
        num_items = counts[item]
        item_total_cost = cost*num_items # if no promotional offer

        # Update the total cost for item if there is promotional offer
        if check_item_has_promo(item):
            num_promo_given = fruit_market[item]['promo']['nth']
            discount = fruit_market[item]['promo']['discount']
            
            if discount == 0:
                item_total_cost = total_cost_for_item_promo_buy_n_get_one_free(cost, num_items, num_promo_given)
                                                             
            else:
                item_total_cost = total_cost_for_item_promo_buy_n_get_discount(cost, num_items, num_promo_given, discount)
                
        list_of_item_costs.append(item_total_cost)

    total_cost_with_promo = sum(list_of_item_costs)
    return total_cost_with_promo
            
        



def main():
    assert get_regular_cost_of_item('apple') == 1.2
    assert get_regular_cost_of_item('mango') == 1.4

    assert check_item_has_promo('pineapple') == True
    assert check_item_has_promo('kiwi') == False

    assert set(show_cheap_items()) == set(['plum', 'kiwi'])

    fruit_list1 = ['apple', 'mango']
    fruit_list2 = ['apple', 'mango', 'apple', 'pineapple']
    fruit_list3 = ['apple', 'mango', 'apple', 'pineapple', 'pineapple', 'pineapple']

    assert items_with_promos(fruit_list1) == ['apple']
    assert set(items_with_promos(fruit_list2)) == set(['apple', 'pineapple'])

    assert round(total_cost_without_promos(fruit_list1), 2) == 2.6
    assert round(total_cost_without_promos(fruit_list2), 2) == 6.3
    assert round(total_cost_without_promos(fruit_list3), 2) == 11.3

    assert round(total_cost_for_item_promo_buy_n_get_one_free(1.2, 2, 2), 2) == 1.2
    assert round(total_cost_for_item_promo_buy_n_get_one_free(1.2, 3, 2), 2) == 2.4

    assert round(total_cost_for_item_promo_buy_n_get_discount(2.5, 2, 2, 0.5), 2) == 4.5
    assert round(total_cost_for_item_promo_buy_n_get_discount(2.5, 3, 2, 0.5), 2) == 7

    assert round(total_cost_with_promos_applied(fruit_list1), 2) == 2.6
    assert round(total_cost_with_promos_applied(fruit_list2), 2) == 5.1
    assert round(total_cost_with_promos_applied(fruit_list3), 2) == 9.6

    print('Everything finished correctly.')

if __name__ == '__main__':
    print('\nInformation about apple: ')
    print(fruit_market['apple'])
    print('\nPromo information for apple:')
    print(fruit_market['apple']['promo'])
    print('\nPromo name for apple:')
    print(fruit_market['apple']['promo']['name'])

    main()

