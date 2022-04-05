from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
list_1 = []


def get_jokes(n, flag=False):
    for i in range(n):
        random_nouns = choice(nouns)
        random_adverbs = choice(adverbs)
        random_adjectives = choice(adjectives)
        joke = f'{random_nouns} {random_adverbs} {random_adjectives}'
        list_2 = []
        print(joke)
        if flag == True:
            list_2 = joke.split()
            for noun in nouns:
                for fun in list_2:
                    if noun == fun:
                        nouns.remove(noun)

            for adverb in adverbs:
                for fun in list_2:
                    if adverb == fun:
                        adverbs.remove(adverb)


            for adjective in adjectives:
                for fun in list_2:
                    if adjective == fun:
                        adjectives.remove(adjective)




get_jokes(n=5, flag=True)