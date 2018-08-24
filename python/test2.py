i = -1
while True:
    i += 1

    if (i > 20):
        break

    # i is odd
    if (i % 2 != 0):
        continue

    print (i)

# start at -1
# add 1 to -1 which equals 0
# is 3 greater than 20? No, so we do NOT break
# is 3 % 2 equal to 0? ie. is 3 an even number? NO IT IS NOT EVEN IT IS ODD
# so we do NOT continue
# we go straight to our print statement
# so we print 0 first.
