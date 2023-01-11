
import get_pattern_tag as gpt
import split_input_sentence
import act_on_request as aor


while True:
    break_tag = aor.act_on_request(gpt.get_pattern_tag(
        split_input_sentence.split_input_sentence()))

    if(break_tag):
        break
