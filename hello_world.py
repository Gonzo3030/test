def greet(name='World'):
    return f'Hello, {name}!'

def main():
    print(greet())
    print(greet('GitHub'))

if __name__ == '__main__':
    main()