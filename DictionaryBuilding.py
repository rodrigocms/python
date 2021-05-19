
# Method 1
book_title=['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter={}

for word in book_title:
    if word in word_counter:
        word_counter[word]=1
    else:  
        word_counter[word]+=1

#Method 2
book_title=['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter={}
for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1        

print(word_counter)



# Contar o numero de palavras
str = 'Diante de tantos indícios, a Advocacia-Geral da União não aprovou as duas dispensas de licitação. Depois de assinados, os contratos da reforma no ministério e nos galpões foram anulados. Mesmo assim, a AGU quer que a investigação continue para verificar se há indícios de conluio entre os servidores e a empresa contratada.Jean Oliveira é o dono e o único gestor da SP Serviços, que está inscrita na Prefeitura de Magé como microempresa. Mesmo assim, por telefone, ele disse que a empresa teria condições de fazer a obra: “Eu tenho caminhão caçamba, tenho duas vans, eu tenho retro. A empresa hoje tem 16 equipamentos. Eu ia vender uma parte dessa frota para você iniciar ela, mas eu tenho caixa também.'
lst = str.split(' ')
print(lst)

word_count = {} 

for word in lst:
    word_count[word] = word_count.get(word,0)+1

print(word_count) 
print(word_count.get('tenh3o','Não Encontrada'))


### Interate Key and Value from Dictionary
cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

for name,role in cast.items():
    print('{} plays {} in the serie.'.format(name,role))


### Exemple Count 

# You would like to count the number of fruits in your basket.  In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number of fruits, but you do not want to count the other items in your basket.
result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for f in fruits:
    result+=basket_items.get(f,0)

print(result)

### Count Fuit and Not Fruit
fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary

for obj,count in basket_items.items():
    if obj in fruits:
        fruit_count+=count
    else:
        not_fruit_count+=count

print(fruit_count,not_fruit_count)