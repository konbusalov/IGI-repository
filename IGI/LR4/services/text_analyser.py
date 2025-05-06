import re
from collections import defaultdict

class TextAnalyser:
    @staticmethod
    def find_lowercase_digit_words(text):
        pattern = r'[a-z]+[0-9]+|[0-9]+[a-z]+'
        matches = re.findall(pattern, text)
        return matches
    
    @staticmethod
    def is_ip_address(text):
        pattern = r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.*'
        return bool(re.fullmatch(pattern, text))
    
    @staticmethod
    def less_than_six_letters(text):
        pattern = r'\b\w{1,5}\b'
        matches = re.findall(pattern, text)
        return len(matches)
    
    @staticmethod
    def shortest_w_word(text):
        pattern = r'\b\w*w\b'
        matches = re.findall(pattern, text)
        matches.sort(key=lambda x: (len(x), x))
        return matches[0]
    
    @staticmethod
    def sort_by_length(text):
        pattern = r'\b\w+\b'
        matches = re.findall(pattern, text)
        matches.sort(key=lambda x: (len(x), x.lower()))
        return matches
    
    @staticmethod
    def count_sentences(text):
        sentences = re.findall(r'[^.!?]+[.!?]', text)
        return len(sentences)

    @staticmethod
    def count_sentence_types(text):
        sentences = re.findall(r'[^.!?]+([.!?])', text)
        counts = defaultdict(int)
        for punct in sentences:
            if punct == '.':
                counts['declarative'] += 1
            elif punct == '?':
                counts['interrogative'] += 1
            elif punct == '!':
                counts['imperative'] += 1
        return dict(counts)

    @staticmethod
    def avg_sentence_length(text):
        sentences = re.split(r'[.!?]', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        if not sentences:
            return 0
            
        total_chars = sum(len(re.sub(r'[^\w\s]', '', s).replace(' ', '')) 
                        for s in sentences)
        return round(total_chars / len(sentences), 2)

    @staticmethod
    def avg_word_length(text):
        words = re.findall(r'\b\w+\b', text)
        if not words:
            return 0
        return round(sum(len(word) for word in words) / len(words), 2)

    @staticmethod
    def count_smileys(text):
        pattern = r'[:;]-*([()\[\]])\1*'
        smileys = re.findall(pattern, text)
        return len(smileys)

    def analyze_text(text):
        return {
            'words_with_lowercase_digits': TextAnalyser.find_lowercase_digit_words(text),
            'ip_address_check': TextAnalyser.is_ip_address(text),
            'words_less_than_six_letters': TextAnalyser.less_than_six_letters(text),
            'shortest_w_word': TextAnalyser.shortest_w_word(text),
            'words_sorted_by_length': TextAnalyser.sort_by_length(text),
            'total_sentences': TextAnalyser.count_sentences(text),
            'sentence_types': TextAnalyser.count_sentence_types(text),
            'avg_sentence_length': TextAnalyser.avg_sentence_length(text),
            'avg_word_length': TextAnalyser.avg_word_length(text),
            'smiley_count': TextAnalyser.count_smileys(text)
        }

