def convert(emo):
    emo = emo.replace(":)","🙂")
    emo = emo.replace(":(","🙁")
    return emo
def main():
    x=input()
    print(convert(x))
main()
