from typing import Dict


def count_words(input: str) -> int:
    c = len(input.split(" "))
    return c


def count_characters(input: str) -> Dict[str, int]:
    if len(input) == 0:
        return {}

    # use-ahead decl
    count: Dict[str, int] = {}

    # filter out the values we don't need
    results = "".join(filter(lambda x: x.isalpha() or x.isdigit(), input.lower()))

    for c in results:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1

    return count


def print_report(title: str, character_occurrences: Dict[str, int]) -> None:
    padding = print_padding(character_occurrences)
    header = f"--- Begin report of {title} ---\n"
    footer = f"--- End report of {title} ---\n"

    contents = [f'The character "{k}" was found {v:>{padding}} times\n' for k, v in sorted(character_occurrences.items())]
    contents.insert(0, header)
    contents.append(footer)

    print("".join(contents))


def print_padding(d: Dict[str, int]) -> int:
    # we're going to create an inverted dictionary that makes the values the keys
    d_vals = sorted({v: k for k, v in d.items()}, reverse=True)

    # apparently math.log10 can return inaccurate numbers past a point, but before that, it supposedly beats
    # stringifying a number and returning the length, but in all other cases, doing this wins; although there is
    # technically a memory inefficiency here with using a string...but too bad!
    padding = len(str(d_vals[0]))

    return padding


def main():
    with open("../books/frankenstein.txt") as f:
        results = count_characters(f.read())
        print_report("Frankenstein", results)


if __name__ == "__main__":
    main()
