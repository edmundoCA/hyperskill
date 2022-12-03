# imports from Stage 1/4
from collections import Counter
from lxml import etree
import nltk
from nltk.tokenize import word_tokenize

# imports from Stage 2/4
import string
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# imports from Stage 4/4
from sklearn.feature_extraction.text import TfidfVectorizer

# downloads from Stage 1/4
# nltk.download('punkt')

# downloads from Stage 2/4
# nltk.download('wordnet')
# nltk.download('stopwords')
# nltk.download('omw-1.4')
#
# downloads from stage 3/4
# nltk.download('averaged_perceptron_tagger')

xml_path = "news.xml"
root = etree.parse(xml_path).getroot()

news = dict()

lemmatizer = WordNetLemmatizer()
dataset = list()
voc = set()
headers = list()
for element in root.findall(".//news"):
    head = element.find("value[@name='head']").text
    headers.append(head)
    text = element.find("value[@name='text']").text.lower()
    dataset.append(text)

    # lemmatize through map and lambda function (0.321589 s)
    tokens = list(map(lambda x: lemmatizer.lemmatize(x), sorted(word_tokenize(text), reverse=True)))

    # lemmatize through for (0.323398 s)
    # tokens = sorted(word_tokenize(text.lower()), reverse=True)
    # for i in range(len(tokens)):
    #     tokens[i] = lemmatizer.lemmatize(tokens[i])

    # lemmatize through list comprehension (0.325688 s)
    # tokens = [lemmatizer.lemmatize(token) for token in sorted(word_tokenize(text.lower()), reverse=True)]

    freq_counter = Counter(tokens)
    freq_counter_temp = Counter()
    for key, value in freq_counter.items():
        if key not in stopwords.words('english') and key not in tuple(string.punctuation):
            freq_counter_temp[key] = value
    freq_counter = Counter()
    for key, value in freq_counter_temp.items():
        if nltk.pos_tag([key])[0][1] == "NN":
            freq_counter[key] = value
            voc.add(key)

vectorizer = TfidfVectorizer(vocabulary=list(voc))
tfidf_matrix = vectorizer.fit_transform(dataset)
terms = vectorizer.get_feature_names_out()

for i in range(10):
    pondered_words = Counter()
    for j, term in enumerate(terms):
        pondered_words[term] = tfidf_matrix[i, j]
    keywords = pondered_words.most_common(5)
    string_keywords = " ".join([x[0] for x in keywords])
    print("{}:\n{}".format(headers[i], string_keywords))


