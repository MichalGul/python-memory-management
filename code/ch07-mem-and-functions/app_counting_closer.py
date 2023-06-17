from typing import Callable


def main():
    # dopóki c1 lub c2 nie zostanie wyczyszczone zmienne wewnętrzne też snie są czyszczone i dlatego ich stan jest zapamietany
    c1 = create_counter(7, 3)
    c2 = create_counter(0, 10)

    print(c1())
    print(c1())
    print("#2", c2())
    print("#2", c2())
    print("#2", c2())
    print("#2", c2())
    print(c1())
    print(c1())


def create_counter(start: int, step: int) -> Callable:
    current = start - step

    def counter_impl():
        nonlocal current

        current += step
        return current

    return counter_impl


if __name__ == '__main__':
    main()
