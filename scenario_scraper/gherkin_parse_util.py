from gherkin.parser import Parser
from gherkin.token_scanner import TokenScanner


def get_language_from_feature(text):
    parser = Parser()

    try:
        feature = parser.parse(TokenScanner(text))
        language = feature['feature']['language']
    except:
        language = 'N/A'

    return language


def parse_text(text):
    parser = Parser()
    return parser.parse(TokenScanner(text))


if __name__ == "__main__":
    file = open('test.feature', 'r')
    text = file.read(1000)
    lang = get_language_from_feature(text)
    print(lang)
