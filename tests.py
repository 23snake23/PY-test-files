percent = float(input('input percent of test in numbers'))

if percent >= 90 and percent < 101:
    print ('Student is grade 9')
elif percent >= 80 and percent < 90:
    print ('Student is grade 8')
elif percent >= 70 and percent < 80:
    print ('Student is grade 7')
elif percent >= 60 and percent < 70:
    print ('Student is grade 6')
elif percent >= 50 and percent < 60:
    print ('Student is grade 5')
elif percent >= 40 and percent < 50:
    print ('Student is grade 4')
elif percent >= 30 and percent < 40:
    print ('Student is grade 3')
elif percent >= 20 and percent < 30:
    print ('Student is grade 2')
elif percent >= 10 and percent < 20:
    print ('Student is grade 1')
elif percent >= 0 and percent < 10:
    print ('Student is ungraded')
else:
    print('invalid interger')
