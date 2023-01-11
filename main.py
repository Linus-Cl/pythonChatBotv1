
import get_pattern_tag as gpt
import split_sentence
import act_on_request as aor
import dataset as ds

ds.update_words()

while True:

    break_tag = aor.act_on_request(gpt.get_pattern_tag(
        split_sentence.split_sentence(input('Input: '))))

    if(break_tag):
        break
