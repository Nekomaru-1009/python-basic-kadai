# -*- coding: utf-8 -*-
"""test

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18IWZjBO9Of1CdUsQmkc8hDLn-skrdGxt
"""

class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def check_adult(self):
    if self.age >= 20:
      print(f"{self.name}さんは大人である")
    else:
      print(f"{self.name}さん大人でない")

user_1 = Human("ナミヘイ", 20)
user_1.check_adult()

user_2 = Human("フネ", 19)
user_2.check_adult()

user_3 = Human("サザエ", 24)
user_3.check_adult()

user_4 = Human("カツオ", 11)
user_4.check_adult()

user_5 = Human("ワカメ", 9)
user_5.check_adult()