from expression_evaulation import evaluate, prettify


def main():
    # input loop
    while True:
        try:
            expr = input("\n>>>")
            result = evaluate(expr)
            print(prettify(result))
        except (KeyboardInterrupt, EOFError):
            print()
            quit()
        except ValueError as e:
            print(e)
if __name__ == '__main__':
    main()
