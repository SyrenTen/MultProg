import re


def find_orientation(article_name):
    positive_words = ['good', 'great', 'excellent', 'positive', 'incredible', 'amazing']
    negative_words = ['bad', 'terrible', 'poor', 'negative', 'awful']

    with open(article_name, 'r') as task11:
        article = task11.read().lower()

    count_pos = sum(1 for word in article.split() if any(re.search(r'\b{}\b'.format(pos_word),
                                                                   word) for pos_word in positive_words))
    count_neg = sum(1 for word in article.split() if any(re.search(r'\b{}\b'.format(neg_word),
                                                                   word) for neg_word in negative_words))

    orientation = 'Positive' if count_pos > count_neg else 'Neutral' if count_pos == count_neg else 'Negative'

    print(f'Article orientation: {orientation}')


if __name__ == '__main__':
    find_orientation('article_for_task_11.txt')
