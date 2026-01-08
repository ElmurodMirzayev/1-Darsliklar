unlilar = "aeuio"
name = "Elmurod".lower()
unli_count = 0
undosh_count = 0
for harf in name:
    if harf in unlilar:
        unli_count += 1
    else:
        undosh_count += 1

print(f"unlilar soni: {unli_count}")
print(f"undoshlar soni: {undosh_count}")