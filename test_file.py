import textwrap

# Длинная строка
base_str = 'этосамоедлиновоесловочрезвычайнодлинноеипотребуетразбивки а эти, не требуют'
split_base_str = base_str.split()
words_list = []
new_w_l = []
for sub_str in split_base_str:
    words_list.append(textwrap.wrap(sub_str, width=10))
for i in words_list:
    for j in i:
        new_w_l.append(j)
print(new_w_l)
print(' '.join(new_w_l))

def string_limiter():
