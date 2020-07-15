    if __name__ == '__main__':
        s = input()
        alphanum = [i.isalnum() for i in s]
        print(any(alphanum))

        alpha = [i.isalpha() for i in s]
        print(any(alpha))

        digit = [i.isdigit() for i in s]
        print(any(digit))

        lower = [i.islower() for i in s]
        print(any(lower))

        upper = [i.isupper() for i in s]
        print(any(upper))
