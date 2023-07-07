import re


def top10():
    text = """
I was working on something and at some point, I needed to check whether the string satisfies this: The string must contain at least 5 words and each separated by a hyphen(-) or an underscore(_). Here is the code that I wrote:
    """
    top = {}
    pun = r'[.,"\'-?:!;]'
    text = re.sub(pun, '', text)

    for word in text.lower().split():
        if len(word) == 1:
            continue
        elif word not in top:
            top[word] = 1
        else:
            top[word] += 1
    sorted_dict = dict(sorted(top.items(), key=lambda x: x[1], reverse=True))
    count = 0
    for key, value in sorted_dict.items():
        if count == 10:
            break
        print(key, value)
        count += 1


if __name__ == '__main__':
    top10()
