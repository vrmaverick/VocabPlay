import random
vocab_list = {
    '1': {'word': 'aberration',
          'meaning': 'a departure from what is normal or expected',
          'example': 'The sudden decision to quit his job was an aberration; he had always been a reliable employee.',
          'keywords': ['departure', 'normal', 'expected', 'reliable']},
    '2': {'word': 'benevolent',
          'meaning': 'kind and generous',
          'example': 'The benevolent millionaire donated a large sum of money to the local orphanage.',
          'keywords': ['kind', 'generous', 'donated', 'money']},
    '3': {'word': 'catalyst',
          'meaning': 'a substance that increases the rate of a chemical reaction',
          'example': 'The enzyme acted as a catalyst, speeding up the chemical reaction in the laboratory experiment.',
          'keywords': ['substance', 'increases', 'rate', 'chemical reaction']},
    '4': {'word': 'debilitate',
          'meaning': 'to make someone weak or infirm',
          'example': 'The prolonged illness debilitated his strength, and he struggled to regain his former vitality.',
          'keywords': ['make', 'weak', 'infirm', 'struggle']},
    '5': {'word': 'ephemeral',
          'meaning': 'lasting for a very short time',
          'example': 'The beauty of the cherry blossoms is ephemeral, as they bloom for only a brief period each spring.',
          'keywords': ['lasting', 'short time', 'bloom', 'brief period']},
    '6': {'word': 'fortuitous',
          'meaning': 'happening by chance or accident',
          'example': 'Their fortuitous encounter at the coffee shop eventually led to a lifelong friendship.',
          'keywords': ['happening', 'chance', 'accident', 'encounter']},
    '7': {'word': 'gregarious',
          'meaning': 'fond of company; sociable',
          'example': 'Known for his gregarious nature, he easily made friends at social gatherings.',
          'keywords': ['fond', 'company', 'sociable', 'gatherings']},
    '8': {'word': 'harangue',
          'meaning': 'a lengthy and aggressive speech',
          'example': 'The politician delivered a harangue against corruption, urging the public to demand transparency.',
          'keywords': ['lengthy', 'aggressive', 'speech', 'corruption']},
    '9': {'word': 'iconoclast',
          'meaning': 'a person who attacks or criticizes established beliefs or institutions',
          'example': 'The artist was considered an iconoclast for challenging traditional artistic conventions.',
          'keywords': ['person', 'attacks', 'criticizes', 'established beliefs']},
    '10': {'word': 'juxtapose',
           'meaning': 'to place or deal with close together for contrasting effect',
           'example': 'The exhibition juxtaposed classical paintings with modern sculptures to highlight the evolution of art.',
           'keywords': ['place', 'deal', 'close together', 'contrasting effect']},
    '11': {'word': 'kaleidoscope',
           'meaning': 'a constantly changing pattern or sequence of elements',
           'example': 'The cityscape at night was a kaleidoscope of lights and colors.',
           'keywords': ['constantly', 'changing', 'pattern', 'sequence']},
    '12': {'word': 'languid',
           'meaning': 'slow and relaxed',
           'example': 'The hot summer afternoon made everyone feel languid and inclined to take a nap.',
           'keywords': ['slow', 'relaxed', 'hot summer', 'inclined']},
    '13': {'word': 'mellifluous',
           'meaning': 'pleasantly smooth or musical to hear',
           'example': 'The singer\'s mellifluous voice captivated the audience, leaving them enchanted.',
           'keywords': ['pleasantly smooth', 'musical', 'captivated', 'audience']},
    '14': {'word': 'nefarious',
           'meaning': 'wicked, villainous, or criminal',
           'example': 'The nefarious plot to overthrow the government was uncovered by the intelligence agency.',
           'keywords': ['wicked', 'villainous', 'criminal', 'plot']},
    '15': {'word': 'obfuscate',
           'meaning': 'to deliberately make something unclear or difficult to understand',
           'example': 'The lawyer tried to obfuscate the facts of the case to confuse the jury.',
           'keywords': ['deliberately', 'make', 'unclear', 'difficult to understand']},
    '16': {'word': 'paradox',
           'meaning': 'a statement or proposition that contradicts itself',
           'example': 'The concept of time travel is a paradox, as it involves contradictory ideas about cause and effect.',
           'keywords': ['statement', 'proposition', 'contradicts itself', 'time travel']},
    '17': {'word': 'quixotic',
           'meaning': 'extremely idealistic; unrealistic and impractical',
           'example': 'His quixotic pursuit of perfection often led to frustration and disappointment.',
           'keywords': ['extremely idealistic', 'unrealistic', 'impractical', 'pursuit of perfection']},
    '18': {'word': 'reverie',
           'meaning': 'a state of being pleasantly lost in one\'s thoughts; a daydream',
           'example': 'As the sun set, she drifted into a reverie, reminiscing about the happy moments of her childhood.',
           'keywords': ['pleasantly lost', 'thoughts', 'daydream', 'reminiscing']},
    '19': {'word': 'serendipity',
           'meaning': 'the occurrence and development of events by chance in a happy or beneficial way',
           'example': 'Their meeting at the bookstore was pure serendipity, leading to a lifelong friendship.',
           'keywords': ['occurrence', 'development', 'events by chance', 'happy or beneficial way']},
    '20': {'word': 'taciturn',
           'meaning': 'reserved or uncommunicative in speech; saying little',
           'example': 'The taciturn man rarely spoke at social gatherings, preferring to listen and observe.',
           'keywords': ['reserved', 'uncommunicative', 'speech', 'social gatherings']},
    '21': {'word': 'ubiquitous',
           'meaning': 'present, appearing, or found everywhere',
           'example': 'In today\'s digital age, smartphones have become ubiquitous, with almost everyone owning one.',
           'keywords': ['present', 'appearing', 'found everywhere', 'digital age', 'smartphones']},
    '22': {'word': 'vex',
           'meaning': 'to make someone feel annoyed, frustrated, or worried',
           'example': 'The constant delays began to vex the passengers waiting at the airport.',
           'keywords': ['make', 'annoyed', 'frustrated', 'worried', 'constant delays']},
    '23': {'word': 'wanderlust',
           'meaning': 'a strong desire to travel and explore the world',
           'example': 'Her wanderlust led her to explore remote and exotic destinations around the globe.',
           'keywords': ['strong desire', 'travel', 'explore', 'world', 'wanderlust']},
    '24': {'word': 'xenophobe',
           'meaning': 'a person who dislikes or is prejudiced against people from other countries',
           'example': 'The politician\'s xenophobic remarks stirred controversy and criticism from the international community.',
           'keywords': ['person', 'dislikes', 'prejudiced', 'people from other countries', 'xenophobic remarks']},
    '25': {'word': 'yearn',
           'meaning': 'to have an intense feeling of longing for something',
           'example': 'Despite achieving success, he continued to yearn for the sense of purpose that had eluded him.',
           'keywords': ['intense feeling', 'longing', 'achieved success', 'sense of purpose']},
    '26': {'word': 'zealous',
           'meaning': 'full of enthusiasm and fervor',
           'example': 'The zealous volunteers worked tirelessly to provide aid to the victims of the natural disaster.',
           'keywords': ['full of enthusiasm', 'fervor', 'volunteers', 'worked tirelessly', 'provide aid']},
    '27': {'word': 'alacrity',
           'meaning': 'brisk and cheerful readiness',
           'example': 'She accepted the challenge with alacrity, eager to demonstrate her skills and enthusiasm.',
           'keywords': ['brisk', 'cheerful', 'readiness', 'accepted challenge', 'demonstrate skills']},
    '28': {'word': 'belligerent',
           'meaning': 'hostile and aggressive',
           'example': 'The belligerent nations engaged in a prolonged conflict, causing widespread suffering and destruction.',
           'keywords': ['hostile', 'aggressive', 'nations', 'prolonged conflict', 'suffering', 'destruction']},
    '29': {'word': 'cacophony',
           'meaning': 'a harsh, discordant mixture of sounds',
           'example': 'The cacophony of horns and sirens in the city was overwhelming for the quiet countryside visitor.',
           'keywords': ['harsh', 'discordant', 'mixture of sounds', 'horns', 'sirens', 'city']},
    '30': {'word': 'deleterious',
           'meaning': 'causing harm or damage',
           'example': 'The deleterious effects of pollution on the environment are a growing concern for scientists and policymakers.',
           'keywords': ['causing harm', 'damage', 'effects of pollution', 'environment', 'growing concern', 'scientists', 'policymakers']},
    '31': {'word': 'ebullient',
           'meaning': 'cheerful and full of energy',
           'example': 'Her ebullient personality brought joy and positivity to everyone around her.',
           'keywords': ['cheerful', 'full of energy', 'personality', 'joy', 'positivity']},
    '32': {'word': 'facetious',
           'meaning': 'treating serious issues with deliberately inappropriate humor',
           'example': 'His facetious comments during the serious meeting were met with disapproval from his colleagues.',
           'keywords': ['treating serious issues', 'deliberately inappropriate humor', 'comments', 'serious meeting', 'disapproval', 'colleagues']},
    '33': {'word': 'garrulous',
           'meaning': 'excessively talkative, especially on trivial matters',
           'example': 'The garrulous tour guide provided more information than the visitors could absorb during the tour.',
           'keywords': ['excessively talkative', 'trivial matters', 'tour guide', 'information', 'visitors', 'absorb', 'tour']},
    '34': {'word': 'histrionic',
           'meaning': 'overly theatrical or melodramatic in character or style',
           'example': 'Her histrionic reaction to the news of a minor setback surprised everyone in the room.',
           'keywords': ['overly theatrical', 'melodramatic', 'character', 'style', 'reaction', 'news', 'minor setback', 'surprised', 'everyone', 'room']},
    '35': {'word': 'ineffable',
           'meaning': 'too great or extreme to be expressed or described in words',
           'example': 'The beauty of the sunset over the ocean was ineffable, leaving the onlookers speechless.',
           'keywords': ['too great', 'extreme', 'expressed', 'described in words', 'beauty', 'sunset', 'ocean', 'onlookers', 'speechless']}}


def is_word_in_meanings(word_to_check, vocabulary):
    for i in vocabulary['keywords']:
        if word_to_check.lower() in vocabulary['meaning']:
            return True
    return False
def show(vocabulary):
    print(f"Word : {vocabulary['word']}")
    print(f"Meaning :{vocabulary['meaning']}")
    print(f"Sentence usage :{vocabulary['example']}")


if __name__ == '__main__':
    s = 0
    i = 0
    while(i<10):
        i+=1
        print("This is a vocabulary you have 10 rounds All the best")
        a = random.randint(1,(len(vocab_list)+1))
        print("Word : " + vocab_list[f'{a}'][f'word'])
        m = input('Enter Meaning: ')
        result = is_word_in_meanings(m,vocab_list[f'{a}'])
        if result==False:
            print("You Were Wrong")
        else:
            print("You may be Right See the full Solution below :)")
            s += 10
        show(vocab_list[f'{a}'])
    print(f"Your Score is {s}")
    if(80<s):
        print("Excellent Score")
    elif(60<s):
        print("Good Can do better")
    else:
        print("Poor need to work harder")

