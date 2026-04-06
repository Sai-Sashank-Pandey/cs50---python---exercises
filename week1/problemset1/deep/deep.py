a = input("What is the answer to the Great Question of life, the Universe and Everything?  ").strip().lower()
#if a == "42" or a == "forty-two" or a == "forty two":
if a in ["42","forty-two","forty two"]:
    print("Yes")
else:
    print("No")
