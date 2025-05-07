# Words Frequency Project

## Description
This project calculates the frequency of words in a given sentence and returns the top `n` most frequent words. This is a technical assessment for Foodles.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/elahrech/words_frequency.git
   cd words_frequency
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To calculate word frequencies, run the project as a module:
```bash
python -m src "your sentence here" n
```

### Example Usage
#### Example 1:
Input:
```bash
python -m src "bar baz foo foo zblah zblah zblah baz toto bar" 3
```
Output:
```
[('zblah', 3), ('bar', 2), ('baz', 2)]
```

#### Example 2:
Input:
```bash
python -m src "foo, bar! baz? foo..." 2
```
Output:
```
[('foo', 2), ('bar', 1)]
```

## Testing
Run the tests using `pytest`:
```bash
pytest
```