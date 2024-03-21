transitions = {
    'start': {'she': 'subject', 'he': 'subject'},
    'subject': {'walked': 'verb_past_tense', 'jumped': 'verb_past_tense'},
    'verb_past_tense': {'to': 'to'},
    'to': {'the': 'the'},
    'the': {'park': 'noun', 'fence': 'noun'},
    'noun': {'yesterday': 'time_adverb'},
    'time_adverb': {}
}
current_state = 'start'
sentence1 = "she walked to the park yesterday"
for word in sentence1.split():
    if current_state in transitions and word.lower() in transitions[current_state]:
        current_state = transitions[current_state][word.lower()]
    else:
        current_state = 'error'
        break
if current_state == 'time_adverb':
    print("Parsed Successfully!")
    print("Past Tense Sentence:", sentence1.replace("walked", "walked"))
current_state = 'start'
sentence2 = "he jumped over the fence"
for word in sentence2.split():
    if current_state in transitions and word.lower() in transitions[current_state]:
        current_state = transitions[current_state][word.lower()]
    else:
        current_state = 'error'
        break
if current_state == 'time_adverb':
    print("Parsed Successfully!")
    print("Past Tense Sentence:", sentence2.replace("jumped", "jumped"))
