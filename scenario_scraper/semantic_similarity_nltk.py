import nltk, string
from nltk import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt') # if necessary...
nltk.download('stopwords')

stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)


def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]


'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))


vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')


def cosine_sim(text1, text2, verbose=None):
    tfidf = vectorizer.fit_transform([text1, text2])
    result = ((tfidf * tfidf.T).A)[0, 1]
    if verbose:
        print(result)
    return result


def get_pairwise_similarity_form_corpus(corpus):
    vect = TfidfVectorizer(tokenizer=normalize, min_df=1, stop_words="english")
    # vect = TfidfVectorizer(min_df=1, stop_words="english")
    tfidf = vect.fit_transform(corpus)
    pairwise_similarity = tfidf * tfidf.T
    return pairwise_similarity.A


def calculate_word_freq(corpus, length):
    words = []
    stop_words = set(stopwords.words('english'))

    for item in corpus:
        word_tokens = word_tokenize(item)
        filtered_sentence = [w.lower() for w in word_tokens if not w.lower() in stop_words and w.isalpha()]
        words.extend(filtered_sentence)
    fdist1 = nltk.FreqDist(words)
    return fdist1.most_common(length)
