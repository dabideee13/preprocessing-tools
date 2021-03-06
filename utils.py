"""
Runtime: Python 3.9.7
"""
from typing import Iterable, Any, Callable
from itertools import groupby, chain
from operator import itemgetter

from nltk.corpus import stopwords


def get_indices(data: Iterable, search: str) -> Iterable:
    indices = {}

    for index, elem in enumerate(data):
        if search in elem:
            indices[index] = elem

    return indices


def pipe(raw_input: Any, *functions, **functions_with_args) -> Any:
    """
    Creates a pipeline (or chain) for every function. Basically,
    this function initially accepts a data then passes it to the next
    function, then the output passes it to the next function as input.

    Args:
        raw_input (Any): Any input, could be list, tuple, etc.

    Other Parameters:
        param1 (Callable): Any function with only one argument.
        param2 (Callable): Any function with only one argument.
        ...

    Keyword Args:
        key1 (Callable): Any function with one or more than one
            arguments with arguments written as list.
        key2 (Callable): Any function with one or more than one
            arguments with arguments written as list.
        ...

    Returns:
        Any: Any output as a result of the functions it goes through.
    """

    # TODO: Needs more improvement for robustness.
    # Currently it will only work for some cases.
    output = raw_input

    if functions:
        for function in functions:
            output = function(output)

    if functions_with_args:
        for function, args_list in functions_with_args.items():
            output = eval(function)(output, *args_list)

    return output


def word_tokenize(text: str) -> list[str]:
    """Converts a text (in string format) to a list of string.

    Args:
        text (str): Raw text format, usually having a '.txt' file extension.

    Returns:
        list[str]: List of strings from the raw text.
    """

    first_pattern = r"[A-Za-z]{2,}"
    second_pattern = r"W+^[\s+]"
    new_text = re.sub(second_pattern, "", text)
    return re.findall(first_pattern, new_text)


def remove_stops(text: str) -> str:
    return " ".join(
        [
            word for word in text.split()
            if word not in stopwords.words("english")
        ]
    )


def remove_punctuations(text: str) -> str:
    return text.translate(str.maketrans("", "", string.punctuation))


def remove_digits(text: str) -> str:
    return "".join([i for i in text if not i.isdigit()])


def remove_double_whitespaces(text: str) -> str:
    return re.sub(" +", " ", text)


def remove_months(text: str) -> str:
    months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    return " ".join([word for word in text.split() if word not in months])


def clean_text(text: str) -> str:
    return pipe(
        text,
        remove_stops,
        remove_punctuations,
        remove_digits,
        remove_double_whitespaces,
        remove_months,
        str.strip
    )


def apply_df(df: pd.DataFrame, function: Callable) -> pd.DataFrame:
    _df = df.copy(deep=True)
    
    for series in _df:
        _df[series] = _df[series].apply(function)
    return _df


def extract_by_pos(data: Iterable, position: int = 0) -> Iterable:
    return [i for i, _ in groupby(data, itemgetter(position))]


def flatten_list(data: list[list[Any]]) -> list[Any]:
    return list(chain(*data))


def find_duplicates(iterable: list[int]) -> list[int]:
    return [x for i, x in enumerate(iterable) if i != iterable.index(x)]


def find_specific_words(specific_words: list[str], text: str) -> list[str]:
    pattern = r"\W.*?({})\W.*?".format("|".join(specific_words))
    return re.findall(pattern, text)


def strip_empty(strings: list[str]) -> list[str]:
    _strings = deepcopy(strings)

    while _strings[0] == "":
        _strings.pop(0)
    while _strings[-1] == "":
        _strings.pop(-1)

    return _strings


def run_timer(seconds: Optional[int] = None, start: int = 2, end: int = 10) -> None:
    if seconds is not None:
        time.sleep(seconds)
        return
    
    time.sleep(random.randint(start, end))

    
def get_latest_data(dir_path: Union[str, Path], n_files: int = 3, suffix: str = '.csv') -> list[str]:
    """
    Get latest downloaded or created data in the current (or defined) directory.
    """
    files = glob.glob(str(dir_path) + f'/*{suffix}')
    return sorted(files, key=os.path.getctime)[-n_files:]
