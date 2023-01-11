favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

print("\n")

coders = ['jen', 'sarah', 'edward', 'phil', 'max', 'bunny']
for coder in coders:
    if coder in favorite_languages.keys():
        print(f"\n{coder.title()}! Thank you for responding.")
    else:
        print(f"\n{coder.title()}, you need to respond!")
