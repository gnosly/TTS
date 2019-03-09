# -*- coding: utf-8 -*-
'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run
through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details.
'''

_pad = '_'
_eos = '~'
_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!\'(),-.:;? '
_punctuations = '!\'(),-.:;? '
_phoneme_punctuations = '.!;:,?'  # TODO not used!

# Phonemes definition
_vowels = 'iyɨʉɯuɪʏʊeøɘəɵɤoɛœɜɞʌɔæɐaɶɑɒᵻ'
_non_pulmonic_consonants = 'ʘɓǀɗǃʄǂɠǁʛ'
_pulmonic_consonants = 'pbtdʈɖcɟkɡqɢʔɴŋɲɳnɱmʙrʀⱱɾɽɸβfvθðszʃʒʂʐçʝxɣχʁħʕhɦɬɮʋɹɻjɰlɭʎʟ'
_suprasegmentals = 'ˈˌːˑ.'
_other_symbols = 'ʍwɥʜʢʡɕʑɺɧ'
_diacrilics = 'ɚa˞̙e̘e̯n̩e̞e̝e̽ëɫe̠s̬t̬u̟ɔ̜ɔ̹t̼d̼b̰a̰a̤b̤t̪d̪t̺d̺t̻d̻ẽ'
_phonemes = sorted(list(_vowels + _non_pulmonic_consonants + _pulmonic_consonants + _suprasegmentals + _other_symbols + _diacrilics))

# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
_arpabet = ['@' + s for s in _phonemes]

# Export all symbols:
symbols = [_pad, _eos] + list(_characters) + _arpabet
phonemes = [_pad, _eos] + _phonemes + list(_punctuations)

if __name__ == '__main__':
    print(" > TTS symbols {}".format(len(symbols)))
    print(symbols)
    print(" > TTS phonemes {}".format(len(phonemes)))
    print(phonemes)
