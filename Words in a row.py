#m2y hi1 i4s val5era name3

def in_a_row(string: str) -> str:
    list_with_words = string.split(" ") #["m2y" "hi1" "i4s" "val5era" "name3"]
    num = list(range(1, len(list_with_words) + 1)) #[1, 2, 3, 4, 5]
    correct_list = []

    for n in num: #take a number from num
        for i in list_with_words: #we take a word from list_with_words
            for t in i: #in each word we take every element
                if str(n) == t: #if this element = number from num
                    correct_list.append(i) #we add a word(i)
                    #so that we compare in a row (as it goes in num) it adds every word in the correct order

    return correct_list

print(in_a_row("m2y hi1 i4s val5era name3 I6 a8m from7 Russ9ia"))





