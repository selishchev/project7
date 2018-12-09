import sys

_list = []
item = ''
print('Enter the items you want to buy today (one item per entering).'
      'When you finish, enter "ok". If you want to exit the program, enter "exit".')
while item != 'ok':
    item = input().lower()
    if item != 'ok':
        _list.append(item)
    if item == 'exit':
        print('Goodbye!')
        sys.exit()
print('Your list:', _list)
while len(_list) != 0:
    comparing = input('Enter the bought item from your list: ').lower()
    if comparing == 'exit':
        print('Goodbye!')
        sys.exit()
    if comparing in _list:
        _list.remove(comparing)
    else:
        print("Oops, this item isn't in your list! Please, enter the bought item again")
    print('Your current list:', _list)
print("That's all you wanted to buy today. Goodbye!")
