class Bar:
    def __call__(self, *args, **kwargs):
        return 1

if __name__ == '__main__':
    b = Bar()
    print(b())