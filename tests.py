from expression_evaulation import evaluate


def verify():
    tests = [
        ("0-3-3", -6),
        ("-3", -3),
        ("-3.7", -3.7),
        ("2^3", 8),
        ("2^2", 4),
        ("(16/2)/2", 4),
        ("3.0+1.0", 4),
        ("(9+7)/(3+1)", 4),
        ("1+2", 3),
        ("1+2+3", 6),
        ("1*2+3", 5),
    ]
    for expression, result in tests:
        print("Testing {}={}:".format(expression, result), end='')
        try:
            r = evaluate(expression)
            print(r)
            assert r == result
        except AssertionError:
            print(" incorrect")
        except ValueError:
            print("bad expression")


def main():
    verify()
    pass
if __name__ == '__main__':
    main()
