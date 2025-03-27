
from transliterate import to_cyrillic, to_latin

matn = input("Matn kiriting: ").lower()

if matn.isascii():
    matn = to_cyrillic(matn)
else:
    matn = to_latin(matn)
    
print(matn.title())


