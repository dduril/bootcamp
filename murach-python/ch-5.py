# -------------------------------------
# Chapter 5 Code Examples
#   Testing and Debugging
# -------------------------------------


# use of the print() function to trace execution
def calculate_future_value(monthly_investment, yearly_interest, years):

    # trace execution
    print("Entering calculate_future_value()")

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(1, months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

        # trace execution
        print("i = ", i, " future value ", future_value)

    return future_value
