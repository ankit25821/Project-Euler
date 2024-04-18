# Even Fibonacci Numbers
'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 
terms will be:

        1, 2, 3, 5, 8, 13, 21, 34, 55, 89,...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

even_num_sum = 0
limit = 4_000_000 # 4 million
a, b = 1, 2

while b <= limit:
    if b % 2 == 0:
        even_num_sum += b
    
    a, b = b, a + b

print(even_num_sum)
