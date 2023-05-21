from flask import Flask, render_template, send_file
import csv
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    with open('static/css/jkjk_3.csv', 'r', encoding='utf-8') as csv_file:
        csv_data = list(csv.reader(csv_file, delimiter=','))

    html_table = generate_html_table(csv_data)

    return render_template('index.html', html_table=html_table)

    # Прочитайте CSV файл в DataFrame
    df = pd.read_csv('static/css/jkjk_3.csv', delimiter=',')

    # Конвертируйте DataFrame в формат XLSX
    xlsx_file = 'static/css/jkjk_3.xlsx'
    df.to_excel(xlsx_file, index=False)

    return render_template('index.html', xlsx_file=xlsx_file)


def generate_html_table(csv_data):
    header_html = '<tr>'
    rows_html = ''
    for i, row in enumerate(csv_data):
        if i == 0:
            for cell in row:
                header_html += f'<th>{cell}</th>'
            header_html += '</tr>'
        else:
            rows_html += '<tr>'
            for cell in row:
                rows_html += f'<td>{cell}</td>'
            rows_html += '</tr>'
    table_html = {'header': header_html, 'rows': rows_html}
    return table_html


@app.route('/download')
def download():
    filename = 'static/css/jkjk_3.xlsx'
    return send_file(filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
