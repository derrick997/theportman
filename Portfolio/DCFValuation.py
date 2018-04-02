





#yearly values
ebit = 0
taxes = 0


year = 0

#constant value
perpetual_growth = 0


#yearly calc

taxrate = #derive
nopat = ebit*(1-taxrate)


#single calc
terminal_value = 0


input("Calculated WACC is " + str(wacc) + ". Use a different WACC? (Y/N): ")