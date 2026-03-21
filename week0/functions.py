def main():
    hello()
    name=input("What's your name? ")
    hello(name)
    hello("daniel day lewis")
def hello(x='Pandey'):
    print("Hello,",x.title())
main()
