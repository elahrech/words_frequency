import argparse
import sys
from src.words_frequency import words_frequency


def run_cli():
    parser = argparse.ArgumentParser(description="Calculate word frequencies in a sentence.")
    parser.add_argument("sentence", type=str, help="The input sentence to analyze.")
    parser.add_argument("n", type=int, help="The number of words to return.")

    args = parser.parse_args()

    try:
        result = words_frequency(args.sentence, args.n)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
