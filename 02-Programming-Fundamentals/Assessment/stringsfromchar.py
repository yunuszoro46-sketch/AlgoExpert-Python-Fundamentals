from collections import Counter

def create_strings_from_characters(frequencies, string1, string2):
    def can_create(freq_dict, string):
        char_counts = Counter(string)
        for char, count in char_counts.items():
            if freq_dict.get(char, 0) < count:
                return False
        return True

    can_s1 = can_create(frequencies, string1)
    can_s2 = can_create(frequencies, string2)
    can_both = can_create(frequencies, string1 + string2)

    if can_both:
        return 2
    if can_s1 or can_s2:
        return 1
    return 0
