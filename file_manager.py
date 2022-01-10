def _extract_digit(filename: str) -> int:
    return int("".join([char for char in filename if char.isdigit()]))
  
  
def _extract_max_digit(files: List[str]) -> int:
    return max([_extract_digit(file) for file in files])


def _remove_digit(filename: str) -> int:
    return "".join([char for char in filename if not char.isdigit()])


def _increment(file: str) -> str:
    name, extension = file.split(sep='.')
    try:
        return _remove_digit(name) + str(_extract_digit(name) + 1) + extension
    except ValueError:
        if name.endswith("_"):
            return name + "1" + extension
        return name + "_1" + extension
      

def _increment(number: int):
    return "contact_matrix_" + str(number + 1) + ".csv"


def manage_files(path: Union[Path, str]):
    files = os.listdir(path)
    return _increment(_extract_max_digit(files))
