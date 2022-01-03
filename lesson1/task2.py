"""
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
 Меняться должен только последний октет каждого адреса. По результатам проверки должно выводиться соответствующее сообщение.
"""


# Расплывчатое условие задачи =)

from task1 import host_ping
from ipaddress import ip_address

def host_range_ping(ip_range:str):
    #Разделяем полученную строку диапазона на стартовый IP и номер последнего октета
    start_ip, last_val = tuple(ip_range.split("-"))
    #Получаем IP последнего адреса диапазона в числовом представлении
    address_bytes = [int(x) for x in start_ip.split('.')]
    last_ip = (
        address_bytes[0] * (256 ** 3) +
        address_bytes[1] * (256 ** 2) +
        address_bytes[2] * (256 ** 1) +
        int(last_val)
    )
    #Переделываем начальный IP в числовое предстваление
    start_ip = int(ip_address(start_ip))
    #Генерируем список адресов для функции из 1 задания
    iplist = [ip_address(el) for el in range(start_ip, last_ip+1)]
    
    return host_ping(iplist)



if __name__ == "__main__":
    ip_range = "8.8.8.8-10"
    res = host_range_ping(ip_range)
    print(res)

