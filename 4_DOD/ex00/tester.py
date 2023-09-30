from statistics import ft_statistics

# should print the mean, median and quartiles
#   mean: 95.6 ((1+42+360+11+64) / 5)
#   median: 42 (middle of [1, 11, 42, 64, 360])
#   lower quartile: 11 (second (5 // 4) of [1, 11, 42, 64, 360])
#   upper quartile: 64 (forth (5 // 4 * 3) of [1, 11, 42, 64, 360])
ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
print("-----")

# should print the standard deviation and variance
#   standard deviation: 17982.70124086944 (square root of the variance)
#   variance: 323377543.9183673 (sum of squared differences between
#                                each number and average / amount of numbers)
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")

# should not print anything as the keys/values are invalid
ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
              ejfhhe="heheh", ejdjdejn="kdekem")
print("-----")

# should print ERROR for each argument as no numbers were given
ft_statistics(toto="mean", tutu="median", tata="quartile")
