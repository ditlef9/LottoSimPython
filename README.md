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

[7, 13, 17, 19, 21, 29, 32]
[3, 7, 9, 10, 21, 25, 27]
[1, 3, 5, 9, 20, 26, 31]
[1, 2, 9, 20, 23, 33, 34]
[6, 7, 18, 20, 22, 24, 32]
[8, 18, 20, 21, 25, 27, 31]
[9, 11, 14, 17, 20, 25, 28]
[6, 7, 12, 14, 18, 21, 28]
[4, 7, 13, 16, 22, 25, 29]
[1, 3, 14, 16, 31, 32, 34]
```

### 1.2 Prices
Prices are given for:
 * 7 main numbers - 14 039 045
 * 6 main + 1 additional number - 65 105
 * 6 main numbers - 4315
 * 5 main numbers - 110
 * 4 main numbers - 50

### 1.3 Drawings
Lotto Sim will draw as many cupons as you wanted, or until you get 7 correct numbers.
A drawing where you get 4 correct numbers two times looks like this:
```
~~~~~~~~ Drawing 576 - Year 11 ~~~~~~~~

Main numbers:
[2] [7] [8] [12] [19] [28] [29] 
Sub numbers:
(15) 

Check if won
5 [8] 18 [19] 27 [28] [29] 	4+0 50
[2] [8] [12] 13 (15) [29] 33 	4+1 50
1 5 13 18 24 27 31 	0+0
[2] 5 14 21 24 27 34 	1+0
4 9 13 16 [19] 23 27 	1+0
[2] [7] 11 16 [19] 27 34 	3+0
3 5 10 11 [19] 27 33 	1+0
[12] 14 20 24 30 31 34 	1+0
5 9 13 [19] 22 25 26 	1+0
1 6 [7] 17 21 25 34 	1+0
{'4+0'}
Gain: 100
Wallet: -27440
```

The gain for this drawing is 100, but you have to pay 60 for each drawing.
This makes your wallet balance decrease.

## 2 Install

a) Download and install the latest version of Python <br />
b) Download and install PyCharm <br />
c) Check out this project in PyCharm. <br />
d) Inside PyCharm project select "Add a Configuration" and make it point to file main.py. <br />

Now you can run the app.