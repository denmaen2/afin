import pandas as pd
import seaborn as sns
import string
import re
import matplotlib.pyplot as plt


value = [[0, 'а'], [1, 'б'], [2, 'в'], [3, 'г'], [4, 'ґ'], [5, 'д'], 
         [6, 'е'], [7, 'є'], [8, 'ж'], [9, 'з'], [10, 'и'], [11, 'і'], 
         [12, 'ї'], [13, 'й'], [14, 'к'], [15, 'л'], [16, 'м'], [17, 'н'], 
         [18, 'о'], [19, 'п'], [20, 'р'], [21, 'с'], [22, 'т'], [23, 'у'], 
         [24, 'ф'], [25, 'х'], [26, 'ц'], [27, 'ч'], [28, 'ш'], [29, 'щ'], 
         [30, 'ь'], [31, 'ю'], [32, 'я']]
value = pd.DataFrame(data=value, columns=['int', 'symbol'])


def stat(text):
    
    unique_symbol = set(text)
    
    symbol_count = {'symbol':[], 'count':[]}
    for f in unique_symbol:
        symbol_count['symbol'].append(f)
        symbol_count['count'].append(text.count(f))
    symbol_count = pd.DataFrame(symbol_count)
    
    symbol_count['frequency'] = symbol_count['count'] / sum(symbol_count['count'])
    
    for f in range(len(symbol_count)):
        print("'" + symbol_count.iloc[f]['symbol'] + "'", 
              '\tfreq.: ' + str(round(symbol_count.iloc[f]['frequency'],5)))
    return symbol_count


def stat_bi(text):
    
    text = text.replace(' ', '')
    text = text.lower()
    unique_symbol = pd.DataFrame(set(text), columns=['first'])
    unique_symbol2 = pd.DataFrame(columns=['first'])
    for f in set(text):
        a = unique_symbol.copy()
        a['second'] = f
        unique_symbol2 = pd.concat([unique_symbol2, a])
    
    unique_symbol2['bigram'] = unique_symbol2['first'] + unique_symbol2['second']
    
    symbol_count = {'symbol':[], 'count':[]}
    for f in unique_symbol2['bigram']:
        symbol_count['symbol'].append(f)
        symbol_count['count'].append(text.count(f))
    symbol_count = pd.DataFrame(symbol_count)
    
    symbol_count['frequency'] = symbol_count['count'] / sum(symbol_count['count'])
    
    return symbol_count


def stat_tre(text):
    
    text = text.replace(' ', '')
    text = text.lower()
    unique_symbol = pd.DataFrame(set(text), columns=['first'])
    unique_symbol2 = pd.DataFrame(columns=['first'])
    for f in set(text):
        a = unique_symbol.copy()
        a['second'] = f
        unique_symbol2 = pd.concat([unique_symbol2, a])
        
    unique_symbol3 = pd.DataFrame(columns=['first'])
    for f in set(text):
        a = unique_symbol2.copy()
        a['third'] = f
        unique_symbol3 = pd.concat([unique_symbol3, a])
    
    unique_symbol3['tregram'] = unique_symbol3['first'] + unique_symbol3['second'] + unique_symbol3['third']
    
    symbol_count = {'symbol':[], 'count':[]}
    for f in unique_symbol3['tregram']:
        symbol_count['symbol'].append(f)
        symbol_count['count'].append(text.count(f))
    symbol_count = pd.DataFrame(symbol_count)
    
    symbol_count['frequency'] = symbol_count['count'] / sum(symbol_count['count'])
    
    return symbol_count


def code(text, a, b):
    text = text.lower()
    
    pattern = r'[' + string.punctuation + ']'
    text = re.sub(pattern, '', text)
    text = text.replace('\n', ' ').replace('\r', '').replace('«', '').replace('»', '')
    text = text.replace('0', ' ').replace('1', '').replace('2', '').replace('3', '')
    text = text.replace('4', ' ').replace('5', '').replace('6', '').replace('7', '')
    text = text.replace('8', ' ').replace('9', '').replace('№', '')
    #a = 2
    #b = 3
    
    text1 = text
    text1 = list(text1)
    for f in range(len(value)):
        text1 = [w.replace(value.iloc[f]['symbol'], str((value.iloc[f]['int'] * a + b) % 33)) for w in text1]
    for f in range(len(value)):
        text1 = [w.replace(str(value.iloc[32-f]['int']), value.iloc[32-f]['symbol']) for w in text1]
        
    return text1


def decode(text, a, b):
    text = text.lower()
    
    pattern = r'[' + string.punctuation + ']'
    text = re.sub(pattern, '', text)
    text = text.replace('\n', ' ').replace('\r', '').replace('«', '').replace('»', '')
    text = text.replace('0', ' ').replace('1', '').replace('2', '').replace('3', '')
    text = text.replace('4', ' ').replace('5', '').replace('6', '').replace('7', '')
    text = text.replace('8', ' ').replace('9', '').replace('№', '')
    #a = 3
    #b = 13
    a = mulinv(a, 33)
    m = 33
    
    text1 = afin
    text1 = list(text1)
    for f in range(len(value)):
        text1 = [w.replace(value.iloc[f]['symbol'], str(a*(value.iloc[f]['int'] + m - b)%33)) for w in text1]
    for f in range(len(value)):
        text1 = [w.replace(str(value.iloc[32-f]['int']), value.iloc[32-f]['symbol']) for w in text1]
        
    return text1


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)


def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n
    
    

text1 = open("C:\\Users\\denma\\Desktop\\lab4 sec\\Kaidasheva_simya.txt", "r", encoding='utf8' )
text1 = text1.read()

text2 = open("C:\\Users\\denma\\Desktop\\lab4 sec\\Мойсей.txt", "r", encoding='utf8' )
text2 = text2.read()

pattern = r'[' + string.punctuation + ']'
text = re.sub(pattern, '', text2)
text = text.replace('\n', ' ').replace('\r', '').replace('«', '').replace('»', '')
text = text.replace('0', ' ').replace('1', '').replace('2', '').replace('3', '')
text = text.replace('4', ' ').replace('5', '').replace('6', '').replace('7', '').replace('i', '').replace('v', '')
text = text.replace('8', ' ').replace('9', '').replace('№', '').replace('I', '').replace('V', '')
text = text.replace('    ', '').replace('—', ' ').replace('’', '')

answer = stat(text)
answer = answer.sort_values(['frequency'], ascending=False)


answer_bi = stat_bi(text)
answer_bi = answer_bi.sort_values(['frequency'], ascending=False)
answer_bi['first'] = answer_bi['symbol'].str[0]
answer_bi['second'] = answer_bi['symbol'].str[1]

heatmap = answer_bi.pivot(index='first', columns='second', values='frequency')

plt.figure(figsize=(25, 22))
sns.heatmap(heatmap, annot=True)
plt.savefig('C:\\Users\\denma\\Desktop\\lab4 sec\\Мойсей.png')

print(' '.join(answer_bi['symbol'][:30].to_list()))

answer_tre = stat_tre(text)
answer_tre = answer_tre.sort_values(['frequency'], ascending=False)
answer_tre['first'] = answer_tre['symbol'].str[0]
answer_tre['second'] = answer_tre['symbol'].str[1]
answer_tre['third'] = answer_tre['symbol'].str[2]



afin = code("""У закладах вищої освіти та їх структурних підрозділах
                діє студентське самоврядування, яке є невід’ємною частиною
                громадського самоврядування відповідних навчальних
                закладів. Студентське самоврядування - це право і можливість студентів
                (курсантів, крім курсантів-військовослужбовців) вирішувати питання
                навчання і побуту, захисту прав та інтересів студентів, а також брати участь в
                управлінні закладом вищої освіти.""", 5, 6)
afin = ''.join(afin)
decode_afin = decode(afin, 5 ,6)
decode_afin = ''.join(decode_afin)


afin = code("""їюгпхкь г єу жезейуклїб ґг еоагщґ їлїхя бю м аьєеєх йе илфх южх ґл їюгїмєгє їлїхя кещ ґгюгс ке олщю х жуїьвеєущ гїуґриеґґущ вепл дмку кгв йл єхґ вепауєущ ву щезе ґл сгжлилфмнве сєхїґе п чр єхйжеєхйґея жлилєхиюея ґг гґкужагзхгкґус жиезигвгр""", 2, 3)
decode_afin = decode(afin, 2 ,3)
decode_afin = ''.join(decode_afin)


afin = code("""хгре їгзш нгєвшну ґш вгиглфхш іьєькхе іьйг іьріш іжлсьєью""", 5, 6)
decode_afin = decode(afin, 5 ,6)
decode_afin = ''.join(decode_afin)

decode_afin = "Хьх нкжпцл інвьацчснмх йпіт"
decode_afin = decode(afin, 2 ,4)
decode_afin = ''.join(decode_afin)
