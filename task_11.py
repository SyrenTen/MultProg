import re


def find_orientation(name):
    positive_words = ['good', 'great', 'excellent', 'positive', 'incredible', 'amazing']
    negative_words = ['bad', 'terrible', 'poor', 'negative', 'awful']

    with open(name, 'r') as task11:
        article = task11.read().lower()

    words = re.findall(r'\b\w+\b', article)

    count_pos = 0
    count_neg = 0

    for word in words:
        if any(re.search(r'\b{}\b'.format(pos_word), word) for pos_word in positive_words):
            count_pos += 1
        elif any(re.search(r'\b{}\b'.format(neg_word), word) for neg_word in negative_words):
            count_neg += 1

    if count_pos > count_neg:
        orientation = 'Positive'
    elif count_pos == count_neg:
        orientation = 'Neutral'
    else:
        orientation = 'Negative'

    print('Article orientation:', orientation)


if __name__ == '__main__':
    article_name = 'article_for_task_11.txt'
    find_orientation(article_name)
