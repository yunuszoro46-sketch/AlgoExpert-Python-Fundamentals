from collections import Counter

def get_n_longest_unique_words(words, n):
    word_counts = Counter(words)
    unique_words = [word for word, count in word_counts.items() if count == 1]
    
    # Sort unique words by length in descending order
    unique_words.sort(key=len, reverse=True)
    
    return unique_words[:n]
