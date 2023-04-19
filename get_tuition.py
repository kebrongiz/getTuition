def get_tuition():
    curr_tuition = 10000

    for _ in range(10):
        curr_tuition += (curr_tuition * 0.05)

    print("Tuition after 10 years will be {}".format(round(curr_tuition, 2)))

    four_year_total = curr_tuition
    for _ in range(3):
        curr_tuition += (curr_tuition * 0.05)
        four_year_total += curr_tuition

    print("The total cost of a four years' worth of tuition starting 10 years from now is {}".format(
        round(four_year_total, 2)))


get_tuition()
