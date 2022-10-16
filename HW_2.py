# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 16:42:24 2022

@author: ADMIN
"""

from scipy.stats import norm
nd = norm(6.4, 2.7)

x1 = nd.cdf(5)
x2 = nd.cdf(4)
x1 -x2

nd.cdf(14.5) - nd.cdf(2.0)

nd.cdf(7.2)

nd.cdf(3)
1 - nd.cdf(9)

nd = norm(30 ,4)

nd.cdf(40)
1 - nd.cdf(21)
nd.cdf(35) - nd.cdf(30)

nd = norm(850000, 200000)
1 - nd.cdf(1000000)

nd = norm(50000, 20000)

nd.cdf(40000)
nd.cdf(65000) - nd.cdf(45000)
1 - nd.cdf(70000)

nd = norm(29, 5)
nd.cdf(34) - nd.cdf(30)
1 - nd.cdf(23)
nd.cdf(40) - nd.cdf(39)

nd = norm(1000, 100)
nd.cdf(790)
nd.cdf(1000) - nd.cdf(790)

nd = norm(20.50, 3.50)
nd.cdf(24.00) - nd.cdf(20.50)
1- nd.cdf(24.00)
nd.cdf(19.00)
