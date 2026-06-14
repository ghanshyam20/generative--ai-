import tiktoken 

enc=tiktoken.encoding_for_model("gpt-4o")

#examples of encoding and decoding 

text="Hello nokia i am coming"

# tokens=enc.encode(text)


#tokens [13225, 18727, 535, 575, 939, 7245]
# print("tokens", tokens)


decoded=enc.decode([13225, 18727, 535, 575, 939, 7245])

print("decoded", decoded)

