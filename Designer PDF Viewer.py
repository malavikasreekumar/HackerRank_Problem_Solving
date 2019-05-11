def designerPdfViewer(h, word):
    height = []
    for i in word:
        height += [h[ord(i) - ord('a')]]
    return len(word) * max(height)
