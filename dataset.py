import split_sentence as sis

data = {"data": [
    {"tag": "greeting",
     "paterns": ["hi", "hello", "hey", "gday", "good day"],
     "responses": ["Hello", "Good to see you!", "Hi there"]
     },

    {"tag": "goodbye",
     "paterns": ["bye", "goodbye", "cu", "see you", "see u", "see you later", "Till next time"],
     "responses": ["See you!", "Goodbye", "Have a nice Day!", "May the force be with you!"]
     },

    {"tag": "noanswer",
     "paterns": ["", " "],
     "responses": ["Please give me more info", "I can't understand that!", "You have to enter a text!"]
     },

    {"tag": "news",
     "paterns": ["news"],
     "responses": [""]
     }


]
}

words = []


def update_words():
    for dictonary in data['data']:
        for patern in dictonary.get('paterns'):
            split_patern = sis.split_sentence(patern)
            for word in split_patern:
                if word not in words:
                    words.append(word)

        for response in dictonary.get('responses'):
            split_response = sis.split_sentence(response)
            for word in split_response:
                if word not in words:
                    words.append(word)
