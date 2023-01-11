import dataset


def get_pattern_tag(word_list):
    data_tag = 'undefined'
    count_appearances = 0
    for dictonary in dataset.data['data']:
        if len(word_list) < 1:
            return 'noanswer'

        count_in_loop = 0
        pattern_list = dictonary.get('paterns')
        for word in word_list:

            if word in pattern_list:
                count_in_loop += 1
                data_tag_in_loop = dictonary.get('tag')

        if count_in_loop > count_appearances:
            count_appearances = count_in_loop
            data_tag = data_tag_in_loop

    print('Detected DataTag: ' + data_tag)
    return data_tag
