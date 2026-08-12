sentence = input("Enter the sentence: ")

# Clean and normalize the sentence
cleaned=sentence.strip()
normalized=cleaned.lower().replace('.','')
# Split the sentence and create the slug
word=normalized.split()
slug='-'.join(word)
# Produce the uppercase form and search result
uppercase=normalized. upper()
python_position=normalized. find( 'python' )
# Display all processed values
print(f"Cleaned: {cleaned}")
print(f"Normalized: {normalized}")
print(f"Words: {word}")
print(f"Slug: {slug}")
print(f"Uppercase: {uppercase}")
print(f"Python Position: {python_position}")