def read_number(prompt: str):
    while True:
        s = input(prompt).strip().replace(",", ".")
        if s.lower() in ("exit", "quit"):
            raise SystemExit  # eleganckie wyjście z programu
        try:
            return float(s)
        except ValueError:
            print("❗ Niepoprawna liczba – spróbuj ponownie.")

OPS = {
    "+":  lambda a, b: a + b,
    "-":  lambda a, b: a - b,
    "*":  lambda a, b: a * b,
    "/":  lambda a, b: a / b,
    "**": lambda a, b: a ** b,
}

ALLOWED = " ".join(OPS.keys())  # tylko do ładnego prompta

first = None
while True:
    if first is None:
        first = read_number("Podaj pierwszą liczbę: ")
        continue

    op = input(f"Podaj działanie [{ALLOWED}] lub 'reset' / 'exit': ").strip()
    if op == "exit":
        break
    if op == "reset":
        first = None
        continue
    if op not in OPS:
        print("❗ Nieznane działanie.")
        continue

    second = read_number("Podaj drugą liczbę: ")

    # prosta walidacja
    if op == "/" and second == 0:
        print("❗ Dzielenie przez zero jest niedozwolone.")
        continue
    if op == "**" and abs(second) > 100:
        print("❗ Zbyt duże potęgowanie (zabezpieczenie przed przepełnieniem).")
        continue

    try:
        first = OPS[op](first, second)
        print("=", first)
    except OverflowError:
        print("❗ Wynik zbyt duży (Overflow). Spróbuj mniejszych liczb.")
