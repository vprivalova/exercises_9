class MorseMsg:
    dictionary_eng = {'•—': 'A', '—•••': 'B',  '—•—•': 'C', '—••': 'D', '•': 'E', '••—•': 'F',
                      '——•': 'G', '••••': 'H', '••': 'I', '•———': 'J', '—•—': 'K', '•—••': 'L',
                      '——': 'M', '—•': 'N', '———': 'O', '•——•': 'P', '——•—': 'Q', '•—•': 'R',
                      '•••': 'S', '—': 'T', '••—': 'U', '•••—': 'V', '•——': 'W', '—••—': 'X',
                      '—•——': 'Y', '——••': 'Z'}

    dictionary_rus = {'.-': 'А', '-...': 'Б', '.--': 'В', '--.': 'Г', '-..': 'Д', '.': 'Е',
                      '...-': 'Ж', '--..': 'З', '..': 'И', '.---': 'Й', '-.-': 'К', '.-..': 'Л',
                      '--': 'М', '-.': 'Н', '---': 'О', '.--.': 'П', '.-.': 'Р', '...': 'С',
                      '-': 'Т', '..-': 'У', '..-.': 'Ф', '....': 'Х', '-.-.': 'Ц', '---.': 'Ч',
                      '----': 'Ш', '--.-': 'Щ', '--.--': 'Ъ',  '-.--': 'Ы', '-..-': 'Ь', '..-..': 'Э',
                      '..--': 'Ю', '.-.-': 'Я'}
    vowels_rus = ["А", "Е", "Ё", "И", "О", "У", "Ы", "Э", "Ю", "Я"]
    consonants_rus = ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц',
               'X', 'Ш', 'Щ', 'Ч']
    vowels_eng = ['A', 'E', 'I', 'O', 'U', 'Y']
    consonants_eng = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V',
                      'W', 'X', 'Z']

    def __init__(self, line):
        self.letters = line.split(' ')

    def eng_decode(self):
        result = []
        for elem in self.letters:
            result.append(MorseMsg.dictionary_eng[elem])
        return ''.join(result)

    def ru_decode(self):
        result2 = []
        for elem in self.letters:
            result2.append(MorseMsg.dictionary_rus[elem])
        return ''.join(result2)

    def get_vowels(self, lang):
        if lang == 'ru':
            result3 = []
            counter = 0
            for elem in self.letters:
                result3.append(MorseMsg.dictionary_rus[elem])
            for elem1 in result3:
                if elem1 in MorseMsg.vowels_rus:
                    counter += 1
        else:
            result4 = []
            counter = 0
            for elem in self.letters:
                result4.append(MorseMsg.dictionary_eng[elem])
            for elem1 in result4:
                if elem1 in MorseMsg.vowels_eng:
                    counter += 1
        return counter

    def get_consonants(self, lang):
        if lang == 'ru':
            result5 = []
            counter = 0
            for elem in self.letters:
                result5.append(MorseMsg.dictionary_rus[elem])
            for elem1 in result5:
                if elem1 in MorseMsg.consonants_rus:
                    counter += 1
        else:
            result6 = []
            counter = 0
            for elem in self.letters:
                result6.append(MorseMsg.dictionary_eng[elem])
            for elem1 in result6:
                if elem1 in MorseMsg.consonants_eng:
                    counter += 1
        return counter

