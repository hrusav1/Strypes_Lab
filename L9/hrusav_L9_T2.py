import sys


def load_stem_file(filename):
    
    stem_dict = {}
    
    with open(filename, 'r') as file:
        
        for line in file:
            parts = line.strip().split(':')
            
            if len(parts) == 2:
                word, stem = parts
                stem_dict[word] = stem
    
    return stem_dict


def find_stem(stem_dict, word):
    
    if word in stem_dict:
        return stem_dict[word]
    
    else:
        return "Stem not found for word '{}'".format(word)


if __name__ == "__main__":
    
    if len(sys.argv) != 3:
        print("Use python3 hrusav_L9_T2.py <stem_file> <word>")
        sys.exit(1)

    stem_file = sys.argv[1]
    target_word = sys.argv[2]

    stem_dict = load_stem_file(stem_file)
    result = find_stem(stem_dict, target_word)
    print(result)

