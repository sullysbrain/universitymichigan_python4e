text = "X-DSPAM-Confidence:    0.8475"
slicePos = text.find('0')
sliced = float(text[slicePos:])
print(sliced)
