print ("Provide 5 numbers to find average, min, and max values. ")
num1 = int(raw_input("First number: "))
num2 = int(raw_input("Second number: "))
num3 = int(raw_input("Third number: "))
num4 = int(raw_input("Fourth number: "))
num5 = int(raw_input("Fifth number: "))
num_total = 0
x = []
if num_total == 0 or num_total > 0:
    #print num_values into list
    x.append(num1)
    x.append(num2)
    x.append(num3)
    x.append(num4)
    x.append(num5)
    print x

    #finding average
    num_total = float(num_total + num1 + num2 + num3 + num4 + num5)
    average = num_total / len(x)
    print "The average is %s." % average

    #finding min value
    print "The minimum value is %s." % min(x)

    #finding max value
    print "The maximum value is %s." % max(x)
