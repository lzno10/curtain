#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import getopt
try:
    opts, args = getopt.getopt(sys.argv[1:],"-n:-p:-b:-s:",["help","output="])
except getopt.GetoptError:
    print "-n 1.5"
for name,value in opts:
    if name in ('-n','help'):
        times = float(value)
        print "长度倍数:"+value
    if name in ('-p','help'):
        print "遮光率:"+value
    if name in ('-b','help'):
        bu_money=float(value)
        print "每米布的价格:"+value
    if name in ('-s','help'):
        sha_money=float(value)
        print "每米纱的价格:"+value
keting_le = 2.78
zhuwo_le = 2.88
yangguang_le = 7.44
money = (keting_le+zhuwo_le+yangguang_le)*bu_money+(keting_le+zhuwo_le)*sha_money
resu = money*times
result = bytes(resu)
print "窗帘布+窗帘纱总价格:"+result
#money = length_bu*float(times)*float(money_bu)+length_sha*float(times)*float(money_sha)
#print money

