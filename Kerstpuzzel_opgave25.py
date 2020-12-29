# Be sure to install Python 3.6 or higher and pip
# The use pip to install, numpy, pandas and openpyxl 

import numpy as np
import pandas as pd 
import inspect
import itertools

def find_matches(teller, noemer, goktekst, match, file):
    def gcd(a, b):
        """Calculate the Greatest Common Divisor of a and b.

            Unless b==0, the result will have the same sign as b (so that when
            b is divided by it, the result comes out positive).
            """
        while b:
            a, b = b, a % b
        return a

    def simplify_fraction(numer, denom):
        if denom == 0:
            return "Division by 0 - result undefined"

        # Remove greatest common divisor:
        common_divisor = gcd(numer, denom)
        (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
        # Note that reduced_den > 0 as documented in the gcd function.

        if reduced_den == 1:
            return "%d/%d is simplified to %d" % (numer, denom, reduced_num)
        elif common_divisor == 1:
            return "%d/%d is already at its most simplified state" % (numer, denom)
        else:
            return reduced_num, reduced_den
            #return "%d/%d is simplified to %d/%d" % (numer, denom, reduced_num, reduced_den)
    
    def splitword(word):
        return [char for char in word]

    df = pd.read_excel(pd.ExcelFile(file), "Sheet1")

    letters = splitword(goktekst)

    letter_list = []
    for l in letters:
        locations = df[df == l].stack().index.tolist()
        letter_list.append(locations)

    # turn the number pairs into fractions
    factored_letter_list = letter_list
    combination2 = [p for p in itertools.product(*letter_list)]
    for i in range(len(letter_list)):
        for j in range(len(letter_list[i])):
            factored_letter_list[i][j] = ( (letter_list[i][j][0] + 1) / letter_list[i][j][1] )

    combination = [p for p in itertools.product(*factored_letter_list)]
    ratio = teller / noemer
    n = 0
    print(f"Ratio = {ratio}")
    for i in range(len(combination)):
        # find and print the combinations that we've found
        sum = 0
        for j in range(len(combination[i])):
            sum += combination[i][j]
            if (abs(sum - ratio) < match): # exacte getallen matchen niet, maar een heel klein verschil is goed genoeg
                numbers1 = []
                numbers2 = []
                # make answer combinations
                for combo_counter in range(len(combination2[i])): # store tuple values in two lists
                    numbers1.append(combination2[i][combo_counter][0] + 1)
                    numbers2.append(combination2[i][combo_counter][1])
                    # print(combination2[i][combo_counter])
                # check answer
                # calculate noemer
                reconstructed_noemer = 1
                for k in range(len(numbers2)):
                    reconstructed_noemer *= numbers2[k]
                #print("Noemer is ", reconstructed_noemer)
                # calculate teller
                reconstructed_teller = 0
                for i in range(len(numbers1)):
                    reconstructed_teller += ((numbers1[i] * reconstructed_noemer) / numbers2[i])
                reconstructed_noemer2 = simplify_fraction(reconstructed_teller, reconstructed_noemer)[1]
                if reconstructed_noemer2 == noemer:
                    n += 1
                    print(f"\n\nCombinatie nr. {n} gevonden :)")
                    print(f"Som is {sum}")
                    print(f"Verschil is {sum - ratio}")
                    for k in range(len(letters)): # print out the answer
                        print(f"Letter {letters[k]} staat in vraag {numbers1[k]} van 20{numbers2[k]}")

                    #print("Teller is", reconstructed_teller)
                    print(f"Oorspronkelijke teller en noemer zijn: {teller} en {noemer}")
                    print(f"De gevonden teller en noemer zijn:     {simplify_fraction(reconstructed_teller, reconstructed_noemer)}")


"""
301925	99484	Wiens
121	48	Nr
		1
521	273	Hit
62	99	Is
113	112	er
		50
12815	3536	jaar
399	208	na
2458	1001	haar
1466473	314160	geboorte
1749257	652080	
1466473	314160	bezongen
"""

match = 0.0001
file = r".\Kerstpuzzel letters.xlsx"

teller = 1466473
noemer = 314160
goktekst = "GEBOORTE"
find_matches(teller, noemer, goktekst, match, file)

# opties = [
#     #teller, noemer, goktekst
#     [113, 112, "ER"]
#     ,[12815, 3536, "JAAR"]
#     ,[399, 208, "NA"]
#     ,[2458, 1001, "HAAR"]
# ]
# for i in range(len(opties)):
#     find_matches(opties[i][0], opties[i][1], opties[i][2], match, file)