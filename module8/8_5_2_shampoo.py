# Write a function shampoo_instructions() with parameter num_cycles. If num_cycles is less than 1, print "Too few.".
# If more than 4, print "Too many.". Else, print "N : Lather and rinse." num_cycles times, where N is the cycle number,
# followed by "Done.". Sample output for the given program:
#
# 1 : Lather and rinse.
# 2 : Lather and rinse.
# Done.
#
#
# Hint: Define and use a loop variable.


def shampoo_instructions(num_cycles):

    if num_cycles < 1:
        print("Too few.")
    elif num_cycles > 4:
        print("Too many.")
    else:
        cycle = 1
        for i in range(0, num_cycles):
            while cycle != num_cycles + 1:
                print("{} : Lather and rinse.".format(cycle))
                cycle += 1
        print("Done.")


shampoo_instructions(0)
