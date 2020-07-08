#Stock Price simulation from Level 2.
#Methodology: Markov Chain regime control -> Acceleration of Last Price -> Weakning/Buy-Sell.
import random

global current_number
global accumulated_sum
# Base case
accumulated_sum=30.00
current_number=0
for i in range(10):

    y=(random.choices(population=[-0.01,0.00,0.01],weights=[0.3,0.4,0.3])[0])
    current_number = current_number + y
    accumulated_sum = round((accumulated_sum + current_number),2)
    print(accumulated_sum)
