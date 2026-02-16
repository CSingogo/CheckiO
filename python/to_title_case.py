# nput: Original string (str).

# Output: Converted string (str).

# Examples:

# assert to_title_case("hello world") == "Hello World"
# assert to_title_case("openai gpt-4") == "Openai Gpt-4"
# assert to_title_case("this is a title") == "This Is A Title"
# assert to_title_case("THE QUICK BROWN FOX") == "The Quick Brown Fox"
# 1
# 2
# 3
# 4
# How it’s used:

# for text processing and data normalization tasks;
# for rendering text in UI in a standard title case format.
# Preconditions:

# sentence ∈ string;
# length(sentence) >= 0.


def to_title_case(sentence: str) -> str:
    # your code here
    return sentence.title()

if __name__ == "__main__":
    print(to_title_case("my name is sOMO"))