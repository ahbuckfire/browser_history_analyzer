import collections
import itertools
from nltk.corpus import stopwords
import operator
import re
import tabulate
import unicodecsv as csv

import matplotlib.pyplot as plt
from wordcloud import WordCloud

stop = stopwords.words('english')

"""
def convert_epoch_to_datetime(db_rows, fieldname):
    return datetime(db_rows[fieldname]/1000000-11644473600, "unixepoch")
"""

def get_base_url(url):
    return url["url"].split("/")[2]


def column_to_count_dict(file_path, field):
    counter = collections.defaultdict(int)
    with open(file_path, "r") as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            if field == "url":
                counter[get_base_url(row)] += 1
            else:
                counter[row[field]] += 1
    return sorted(counter.items(), key=operator.itemgetter(1), reverse=True)


def word_cloud(titles):
    wordcloud = WordCloud(
                          background_color='white',
                          max_words=200,
                          max_font_size=40, 
                          random_state=42
                         ).generate(str(titles))

    print wordcloud
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()

def parse_page_titles(file_path, field):
    with open(file_path, "r") as in_file:
        reader = csv.DictReader(in_file)
        titles = []
        for row in reader:
            title = re.findall("[\\w']+", row[field].lower())
            title = [str(word.strip("\'")) for word in title if word not in stop and word not in ["edu", "org", "com", "net"]]
            titles.extend(title)

    print word_cloud(titles)

def create_table(data, headers):
    data_list = [[d[0], d[1]] for d in data]
    return tabulate.tabulate(data_list, headers=headers)


parse_page_titles(args.target, "title")
#print create_table(column_to_count_dict(args.target, "url"), ["url", "visits"])
