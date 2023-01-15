# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 12:09:42 2023

@author: Xomidov Xushnud
"""
class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        1748. Sum of Unique Elements
        bu masalada berilgan listda faqat bir martadan qatnashgan
        elementlar yig;indisini qaytarishimiz so'ralgan
        """
        summa = 0
        nums = sorted(nums)
        # sorted() metodi bilan numsni o'sish tartibaga keltiramiz
        num = set(nums)
        # set() metodi bilan numsdagi elementlarni faqat bittadan numga o'tkazamiz
        for i in num:
            t1 = 0
            for j in nums:
                if i == j:
                    t1 += 1
                    # bu shart yordamida numdagi har bir element, 
                    # numsda nechtaligini aniqlaymiz
                elif t1 > 0:
                    break
            if t1 == 1:
                summa += i
                # agar numdagi element numsda bitta bo'lsa summaga osha 
                # elementni qo'shamiz
        return summa
        # eng oxirida numsdagi faqat bir martada qatnashgan elementlar
        # yig'indisini qaytaramiz
        

