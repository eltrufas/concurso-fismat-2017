from flask import Flask, render_template, abort
import json

app = Flask(__name__)

@app.route('/<page_id>.html')
def page(page_id):
    site = json.load(open('pages.json'))

    pages_dict = site['link_details']
    links = site['nav_links']

    page_dict = pages_dict[page_id]

    if page_id in pages_dict and page_dict['type'] == 'template':
        return render_template(page_dict['template'], links=links, pages=pages_dict)
    else:
        return abort(404)



@app.route('/')
def index():
    return page("inicio")


if __name__ == '__main__':
    app.run(debug=True)
