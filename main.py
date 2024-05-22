path_to_file = "./books/frankenstein.txt"

def get_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def word_count(text):
        words = text.split()
        return len(words)

def char_freq(text):
    text = text.lower()
    freq = {}
    for char in text:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    return freq

def sort_on(dict):
    return dict["num"]

def dict_to_lod(dict):
    lod = []
    for k, v in dict.items():
        lod.append({"char": k, "num": v})
    return lod

def print_report(path_to_file):
    text = get_text(path_to_file)
    freq_dict = char_freq(text)
    lod = dict_to_lod(freq_dict)
    lod.sort(reverse=True, key=sort_on)

    print(f'--- Begin report of {path_to_file} ---')
    print(f'{word_count(text)} words found in the document')

    for d in lod:
        if d["char"].isalpha():
            print(f"The '{d["char"]}' character was found {d["num"]} times")

    print("--- End report ---")

def main():
    print_report(path_to_file)

if __name__ == '__main__':
    main()





