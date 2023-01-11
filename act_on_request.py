import dataset
import random
import news_scraper


def print_news():
    news = news_scraper.get_news_headlines()
    print('Here are the top 5 news headlines: \n')
    for i in range(5):
        print(' -', news[i])
    print()
    print_more_news(news)


def print_more_news(news):
    news_len = len(news)
    print(f'There is a total of {news_len} headlines!')
    print('Do you want me to show all of them? (y/n)')
    more_news = input()
    if more_news == 'y':
        for i in range(6, news_len):
            print(' -', news[i])

    elif more_news == 'n':
        return

    else:
        print("Invalid input! Please use either 'y' or 'n' as input characters!")
        print_more_news(news)


def print_response(index):
    responses = dataset.data.get('data')[index].get('responses')
    random_answer_index = random.randrange(len(responses))
    print(responses[random_answer_index])


def get_tag_index(tag):
    index = 0
    for dictonary in dataset.data['data']:
        if dictonary.get('tag') == tag:
            return index

        index = index+1


def act_on_request(tag):
    index = get_tag_index(tag)
    #print(f'Index: {index}')

    if tag == 'greeting':
        print_response(index)

    elif tag == 'goodbye':
        print_response(index)
        return True

    elif tag == 'noanswer':
        print_response(index)

    elif tag == 'news':
        print_news()
