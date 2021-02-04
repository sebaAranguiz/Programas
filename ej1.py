s = 'azcbobobegghakl'

order = ""
longer = ""

for x in range(len(s)):
    if s[x] >= s[x-1]:
        order += s[x]
        # print("order if: ", order)

    else:
        order = s[x]
        # print("order else: ", order)

    if len(order) > len(longer):
        longer = order
        # print("longer: ", longer)

print('Longest substring in alphabetical order is: ' + str(longer))
