text = """Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick"""
text_s = []
text_n = []
text_d = []
text = text.split("\n")
for i in text:
    text_s = text_s+[i.split()]
for i in text_s:
    text_n = text_n+[' '.join(word for word in i if len(word) > 3)]
for i in text_n:
    text_d = text_d+[i.split()]
print(text_d)