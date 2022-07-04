# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 15:13:24 2022

@author: User
"""

car_0 = {'model':'ferrari', 'rang':'qizil'}
#print(car_0 ['model'])
#print(car_0 ['rang'])

en_uz = {'apple':'olma', 'peach':'shaftoli', 'apricot':"o'rik" }
#print(en_uz)
#print(en_uz['apple'])

mevalar = {'olma':10000, 'tarvuz':8000, 'qovun':12000}

#print(f"Olma narhi {mevalar['olma']} so'm")
#print(f"Qovun narhi {mevalar['qovun']} so'm")

talaba_0 = {'ism':'murod olimov', 'yosh':20, 't_yil':2000}
#print(f"{talaba_0['ism'].title()},\
#     {talaba_0['t_yil']}-yilda tu'ilgan,\
#         {talaba_0['yosh']} yoshda") 

del talaba_0 ['yosh']
#print(talaba_0)

meva = en_uz.get('pineapple', 'Bunday meva mavjud emas')
print(meva)
