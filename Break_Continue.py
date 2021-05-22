#Break, Continue
#Sometimes we need more control over when a loop should end, or skip an iteration. In these cases, we use the break and continue keywords, which can be used in both for and while loops.

# break terminates a loop
# continue skips one iteration of a loop

manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

# the code breaks the loop when weight exceeds or reaches the limit
print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking loop now!")
        break
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))


manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

# the code breaks the loop when weight exceeds or reaches the limit
print("METHOD RODRIGO")
weight = 0
weight_limit = 100

items = []
for cargo_name, cargo_weight in manifest:
    if weight + cargo_weight >= weight_limit:
        continue
    weight+=cargo_weight
    items.append(cargo_name)


print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))


#------ Exemple 2

# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here
for news in headlines:
    news_ticker+= news+' '
    if len(news_ticker)>= 140:
        news_ticker = news_ticker[0:140]
        break
print(news_ticker)
    
## ------  Exemple Prime Numbers  ????????????

check_prime = [26, 39, 51, 53, 57, 79, 85]

for n in check_prime:
    for i in range(2,n):
        if (n%i) == 0:     
           break  
        if i == n -1:     
            print('{} is prime number'.format(n))    




check_prime = [26, 39, 51, 53, 57, 79, 85]

# iterate through the check_prime list
for num in check_prime:

# search for factors, iterating through numbers ranging from 2 to the number itself
    for i in range(2, num):

# number is not prime if modulo is 0
        if (num % i) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
            break

# otherwise keep checking until we've searched all possible factors, and then declare it prime
        if i == num -1:    
            print("{} IS a prime number".format(num))