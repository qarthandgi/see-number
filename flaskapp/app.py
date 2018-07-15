from flask import Flask
from flask import request
from sklearn import datasets, svm
from PIL import Image
from numpy import array

import csv
from pprint import pformat
from io import BytesIO

from urllib.request import urlopen

mine = True
train = False

if mine:
    digits = []
    with open('numbers.csv', newline='') as f:
        reader = csv.reader(f)
        digits = list(reader)
    clf = svm.SVC(gamma=0.0001, C=100)
    x_digits = [digit[:-1] for digit in digits]
    y_digits = [digit[-1] for digit in digits]
    x, y = x_digits, y_digits
    clf.fit(x, y)
else:
    digits = datasets.load_digits()
    clf = svm.SVC(gamma=0.0001, C=100)
    x, y = digits.data[:], digits.target[:]
    clf.fit(x, y)

app = Flask(__name__)

def save_row(row):
    with open('numbers.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(row)

def scale_num(x):
    num = ((16.0 - 0.0)*(float(x) - 0))/(255.0)
    return num

@app.route('/', methods=['POST'])
def get_four():
    data_url = request.form['data_url']
    img = Image.open(urlopen(data_url))
    img = img.resize((16, 16), Image.ANTIALIAS)
    arr = array(img)
    pixels = [scale_num(x[3]) for row in arr for x in row]
    if train:
        real_number = int(request.form['real_number'])
        pixels.append(real_number)
        save_row(pixels)
        return 'ok'
    # app.logger.info('NILES OK')
    # app.logger.info(pixels)
    # app.logger.info(real_number)
    # app.logger.info('NILES NILES: {}'.format(str(clf.predict([pixels]))))
    return clf.predict([pixels])[0]

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')