import pandas as pd
from collections import Counter

def load_data(filepath: str) -> pd.DataFrame:
    """Load CSV data into a DataFrame."""
    return pd.read_csv(filepath)

def clean_text(text: str) -> list[str]:
    """Lowercase and split text into words."""
    text = text.lower()
    words = text.split()
    return words


def compute_word_frequency(df: pd.DataFrame) -> Counter:
    """Compute word frequency from a DataFrame."""
    all_words = []
    for text in df["text"]:
        all_words.extend(clean_text(text))
    return Counter(all_words)

def main():
    data_path = "data/sample_texts.csv"
    df = load_data(data_path)
    word_freq = compute_word_frequency(df)

    print("Top words:")
    for word, count in word_freq.most_common(5):
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
