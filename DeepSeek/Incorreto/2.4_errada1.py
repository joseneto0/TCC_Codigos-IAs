# Ler as 4 linhas do poema
v1 = input().strip()
v2 = input().strip()
v3 = input().strip()
v4 = input().strip()

def count_common_letters(last_word1, last_word2):
    min_length = min(len(last_word1), len(last_word2))
    common = 0
    for i in range(min_length):
        if last_word1[i] == last_word2[i]:
            common += 1
    return common

lw_v1 = v1.split()[-1]
lw_v2 = v2.split()[-1]
lw_v3 = v3.split()[-1]
lw_v4 = v4.split()[-1]

rhyme1 = count_common_letters(lw_v1, lw_v3)
rhyme2 = count_common_letters(lw_v2, lw_v4)

total_beauty = rhyme1 + rhyme2

print(total_beauty)