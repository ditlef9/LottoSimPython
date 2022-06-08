# Lotto Sim Python
A Python app that simulates Norwegian Lotto.

## 1. About Lotto Simulator for Python
The app will first create a random cupon for you. Then it will ask you how many
drawings you want to try. You can here select between 1 and endless drawings (until you win by getting 7 right numbers).

### 1.1 Coupon
In Lotto you will get a coupon consisting of 10 rows with 7 numbers per row.
Each coupon costs 60.
```
~~~~~~~~  Coupon ~~~~~~~~ 

[13, 16, 17, 19, 24, 25, 29]
[6, 10, 12, 13, 14, 20, 24]
[5, 10, 14, 21, 29, 32, 34]
[3, 5, 7, 15, 26, 29, 32]
[3, 7, 15, 16, 23, 25, 26]
[3, 12, 13, 14, 16, 27, 33]
[2, 3, 7, 11, 17, 18, 34]
[2, 11, 13, 18, 24, 26, 32]
[12, 15, 19, 25, 26, 28, 29]
[4, 18, 22, 31, 32, 33, 34]
```

### 1.2 Prices
Prices are given for:
 * 7 main numbers - 14 039 045
 * 6 main + 1 additional number - 65 105
 * 6 main numbers - 4315
 * 5 main numbers - 110
 * 4 main numbers - 50

### 1.3 Drawings
Lotto Sim will draw as many coupons as you wanted, or until you get 7 correct numbers.
A drawing where you get 5 correct numbers one time looks like this:
```
~~~~~~~~ Drawing 46 - Year 0 ~~~~~~~~

Main numbers:
[3] [7] [15] [21] [29] [31] [32] 
Sub numbers:
(17) 

Check if won
13 16 (17) 19 24 25 [29] 	1+1
6 10 12 13 14 20 24 	0+0
5 10 14 [21] [29] [32] 34 	3+0
[3] 5 [7] [15] 26 [29] [32] 	5+0 110
[3] [7] [15] 16 23 25 26 	3+0
[3] 12 13 14 16 27 33 	1+0
2 [3] [7] 11 (17) 18 34 	2+1
2 11 13 18 24 26 [32] 	1+0
12 [15] 19 25 26 28 [29] 	2+0
4 18 22 [31] [32] 33 34 	2+0
{'5+0'}
Gain: 110
Wallet: -2150
```

The gain for this drawing is 100, but you have to pay 60 for each drawing.
This makes your wallet balance decrease.

## 2 Install

a) Download and install the latest version of Python <br />
b) Download and install PyCharm <br />
c) Check out this project in PyCharm. <br />
d) Inside PyCharm project select "Add a Configuration" and make it point to file main.py. <br />

Now you can run the app.