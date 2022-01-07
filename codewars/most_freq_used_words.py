def top_3_words(text):
    from string import punctuation
    
    def check(st):
        if all([i in punctuation for i in st]):
            return False
        return True
    
    p = punctuation.replace("'", "")
    text = text.translate(str.maketrans('','', p))
    lst = [i.lower() for i in text.split()]    
    lst = list(filter(check, lst))

    counter = {}
    for i in lst:
        if i not in counter:
            counter.setdefault(i, 1)
        else:
            counter[i] += 1
    
    counter = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
    top = list(counter.items())[:3]
    
#     print(lst)
#     print(counter)
    
    if len(lst) == 0:
        return []
    
    return [i[0] for i in top]
    
