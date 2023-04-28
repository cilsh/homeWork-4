class Shifr:
    def __init__(self, code):
        self.code = code

    def shifr(self):
        self.code = self.code * 55555
        return self.code

    def antyshifr(self):
        self.code = self.code / 55555
        return self.code


if __name__ == '__main__':
    cr = Shifr(int(input('Введіть код: ')))
    print('Зашифрований код:', cr.shifr())
    print('Розшифрований код:', cr.antyshifr())
