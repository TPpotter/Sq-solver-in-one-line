while True:
    try:
        print('error' if not sum([a := float(input()), b := float(input()), c := float(input())]) else
              'no x' if ((b ** 2) - (4 * a * c)) < 0

              else f'x = {-c / b}' if a == 0
              else f'x1 = {(-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)}\n'
                   f'x2 = {(-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)}')

    except ValueError:
        print('неправильный ввод')
