# -*- coding: utf-8 -*-

import tqdm
from typing import Union


def validate(id_number: Union[int, str]) -> bool:
    """Validate format and checksum of the identity number.
    :param id_number: Saudi Arabian identity number
    :type id_number: int or str
    https://github.com/homaily/Saudi-ID-Validator/blob/master/validateSAID.py
    """

    digits = [int(d) for d in str(id_number)] 

    if len(digits) != 10 or digits[0] not in [1, 2]: 
        return False

    odd_sum = sum(digits[-1::-2]) #مثال : 1134422111  راح يحذف الخانات هذي 1,3,5,7,9 وراح تكون 14211 نجمعها 9
    even_sum = sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]]) # مثال : 1134422111 راح يحذف الخانات هذي 1,3,5,7,9 وراح تكون 13421 ناخذ كل رقم ونضربه ب 2 ونقسمه على 10 وناخذ حاصل القسمة ونكررها على باقي الخمس ارقام ونجمعها يطلع 22
    checksum = (odd_sum + even_sum) % 10 # مثال : نجمع 22 + 9 اذا قبل القسمه على 10 الهويه صحيح

    return bool(checksum == 0)
for id in tqdm.tqdm(range(1134422111,1134422999)): # they'll check from 1134422111 to 1134422998
    if validate(id) == True: # if true will save in file with name id1.txt
        f = open("id1.txt", "a")
        ff= str(id)
        f.write(ff+'\n')
