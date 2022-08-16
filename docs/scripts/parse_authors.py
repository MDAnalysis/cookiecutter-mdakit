import pathlib
import re

abs_filepath = pathlib.Path(__file__).resolve()
COOKIECUTTER_PATH = abs_filepath.parent.parent.parent
AUTHOR_FILE = COOKIECUTTER_PATH / "AUTHORS.md"


def parse_authors(sort_alphabetically: bool = False):
    username_pattern = "<@[\S]+>"
    with AUTHOR_FILE.open("r") as f:
        contents = [x.strip() for x in f.readlines()]

    authors = []
    for line in contents:
        if not line.startswith("-"):
            continue

        if re.search(username_pattern, line):
            author_name = re.sub(username_pattern, "", line)[1:]
            authors.append(author_name.strip().strip("\\").strip())

    if sort_alphabetically:
        authors = sorted(authors, key=lambda x: x.split()[::-1])
    return authors


if __name__ == "__main__":
    print(parse_authors())
