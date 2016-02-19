#来自https://github.com/Yixiaohan/show-me-the-code
#敏感词 filtered_words_list，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
#和前面题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「sex是个好城市」，则变成「**是个好城市」。
filtered_words_list = ['love','sex','jiangge']
#用flask做服务器
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def post_form():
    return '''
        <form action="/filtered_words" method="post">
        <p>#filtered_word.Freedom or Human Rights.<input name="post"></p>
        <p><button type="submit">filtered_words</button></p>
        </form>
        <form action="/replace" method="post">
        <p>#filtered_word.replace by **.<input name="post"></p>
        <p><button type="submit">replace_words</button></p>
        </form>
        '''

@app.route('/replace', methods=['POST'])
def replace_words():
    text=request.form['post']
    for x in filtered_words_list:
        text=text.replace(x,'**')
    text += '<h3>return</h3>'
    return text

@app.route('/filtered_words', methods=['POST'])
def filtered_words():
    for x in filtered_words_list:
        if request.form['post'].find(x)!=-1:
            return '<h3>Freedom</h3>'
    return '<h3>Human Rights</h3>'

if __name__ == '__main__':
    app.run()