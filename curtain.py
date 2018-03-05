#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
times = sys.argv[1]
money_bu = sys.argv[2]
money_sha = sys.argv[3]
length_bu = 7.44+2.78+2.88
length_sha = 2.78+2.88
money = length_bu*float(times)*float(money_bu)+length_sha*float(times)*float(money_sha)
print money
