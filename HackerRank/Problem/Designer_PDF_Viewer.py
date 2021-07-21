def designerPdfViewer(h, word):
    li = []
    for i in word:
        li.append(h[ord(i) - 97])

    return max(li) * len(word)


if __name__ == "__main__":
    h = list(map(int,input().rstrip().split()))

    word = input().strip().lower()

    print(designerPdfViewer(h, word))