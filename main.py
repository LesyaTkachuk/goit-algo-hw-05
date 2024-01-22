from timeit import timeit

from task_3.kmp_search import kmp_search
from task_3.boyer_moore_search import boyer_moore_search
from task_3.rabin_karp_search import rabin_karp_search


if __name__ == "__main__":
    with open("task_3/text_1.txt") as fh:
        text_1 = fh.read()

    with open("task_3/text_2.txt") as fh:
        text_2 = fh.read()

    search_pattern_1 = "аналіз"
    unexisting_search_pattern_1 = "аналізатор"

    print(
        f"Pattern '{search_pattern_1}' was found at index ",
        rabin_karp_search(text_1, search_pattern_1),
    )
    print(
        f"Pattern '{unexisting_search_pattern_1}' was not found ",
        rabin_karp_search(text_1, unexisting_search_pattern_1),
    )

    # calculation of search time of existing pattern in text_1 for three algorithm types
    existing_pattern_kmp_search_time_text_1 = timeit(
        lambda: kmp_search(text_1, search_pattern_1), number=5
    )
    existing_pattern_boyer_moore_search_time_text_1 = timeit(
        lambda: boyer_moore_search(text_1, search_pattern_1), number=5
    )
    existing_pattern_rabin_karp_search_time_text_1 = timeit(
        lambda: rabin_karp_search(text_1, search_pattern_1), number=5
    )

    # calculation of search time of unexisting pattern in text_1 for three algorithm types
    unexisting_pattern_kmp_search_time_text_1 = timeit(
        lambda: kmp_search(text_1, unexisting_search_pattern_1), number=5
    )
    unexisting_pattern_boyer_moore_search_time_text_1 = timeit(
        lambda: boyer_moore_search(text_1, unexisting_search_pattern_1), number=5
    )
    unexisting_pattern_rabin_karp_search_time_text_1 = timeit(
        lambda: rabin_karp_search(text_1, unexisting_search_pattern_1), number=5
    )

    search_pattern_2 = "Хеш-таблиця"
    unexisting_search_pattern_2 = "Двозв'язні списки"

    print(
        f"Pattern '{search_pattern_2}' was found at index ",
        rabin_karp_search(text_2, search_pattern_2),
    )
    print(
        f"Pattern '{unexisting_search_pattern_2}' was not found ",
        rabin_karp_search(text_2, unexisting_search_pattern_2),
    )

    # calculation of search time of existing pattern in text_2 for three algorithm types
    existing_pattern_kmp_search_time_text_2 = timeit(
        lambda: kmp_search(text_2, search_pattern_2), number=5
    )
    existing_pattern_boyer_moore_search_time_text_2 = timeit(
        lambda: boyer_moore_search(text_2, search_pattern_2), number=5
    )
    existing_pattern_rabin_karp_search_time_text_2 = timeit(
        lambda: rabin_karp_search(text_2, search_pattern_2), number=5
    )

    # calculation of search time of unexisting pattern in text_2 for three algorithm types
    unexisting_pattern_kmp_search_time_text_2 = timeit(
        lambda: kmp_search(text_2, unexisting_search_pattern_2), number=5
    )
    unexisting_pattern_boyer_moore_search_time_text_2 = timeit(
        lambda: boyer_moore_search(text_2, unexisting_search_pattern_2), number=5
    )
    unexisting_pattern_rabin_karp_search_time_text_2 = timeit(
        lambda: rabin_karp_search(text_2, unexisting_search_pattern_2), number=5
    )

    print(f"{'-'*72}")
    print(
        f"{'Algorithm':<20} | {'Time existing pattern':<22} | {'Time unexisting pattern':<22}"
    )
    print(f"{'-'*72}")
    print("Text 1")
    print(f"{'-'*72}")
    print(
        f"{'Knuth-Morris_Pratt': <20} | {existing_pattern_kmp_search_time_text_1:<22} | {unexisting_pattern_kmp_search_time_text_1:<22}"
    )
    print(
        f"{'Boyer-Moore search': <20} | {existing_pattern_boyer_moore_search_time_text_1:<22} | {unexisting_pattern_boyer_moore_search_time_text_1:<22}"
    )
    print(
        f"{'Rabin-Karp search': <20} | {existing_pattern_rabin_karp_search_time_text_1:<22} | {unexisting_pattern_rabin_karp_search_time_text_1:<22}"
    )
    print(f"{'-'*72}")
    print("Text 2")
    print(f"{'-'*72}")
    print(
        f"{'Knuth-Morris_Pratt': <20} | {existing_pattern_kmp_search_time_text_2:<22} | {unexisting_pattern_kmp_search_time_text_2:<22}"
    )
    print(
        f"{'Boyer-Moore search': <20} | {existing_pattern_boyer_moore_search_time_text_2:<22} | {unexisting_pattern_boyer_moore_search_time_text_2:<22}"
    )
    print(
        f"{'Rabin-Karp search': <20} | {existing_pattern_rabin_karp_search_time_text_2:<22} | {unexisting_pattern_rabin_karp_search_time_text_2:<22}"
    )
    print(f"{'-'*72}")
