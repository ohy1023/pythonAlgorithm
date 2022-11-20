s = input()

string_list = []
for i in s:
    if i.isalpha():
        string_list.append(i.lower())

for j in range(len(string_list)):
    if string_list[j] != string_list[-(j+1)]:
        print(False)
        break
else:
    print(True)


