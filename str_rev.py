str = input('Enter a sentence: ')
print(str)

rev= ''

for ch in str:
    rev = ch + rev
print('Reversed string is:',rev)

#algorithm
# | `ch`  | `rev = ch + rev` | Value of `rev` after iteration |
# | ----- | ---------------- | ------------------------------ |
# | `'a'` | `'a' + ''`       | `"a"`                          |
# | `'p'` | `'p' + 'a'`      | `"pa"`                         |
# | `'p'` | `'p' + 'pa'`     | `"ppa"`                        |
# | `'l'` | `'l' + 'ppa'`    | `"lppa"`                       |
# | `'e'` | `'e' + 'lppa'`   | `"elppa"`                      |


#OUTPUT
# Enter a sentence: Hello Python Developers!
# Hello Python Developers!
# Reversed string is: !srepoleveD nohtyP olleH