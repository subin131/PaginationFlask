from flask import Flask, render_template, request
import requests

app = Flask(__name__)
todos_per_page = 10  # number of todos to display per page

@app.route('/')
def index():
    page = int(request.args.get('page', 1))  # get current page number from query string, default to 1
    start_idx = (page - 1) * todos_per_page
    end_idx = start_idx + todos_per_page

    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    if response.ok:
        todos = response.json()[start_idx:end_idx]
        total_todos = len(response.json())
        return render_template('index.html', todos=todos, page=page, total_todos=total_todos, todos_per_page=todos_per_page)
    else:
        return 'Error fetching data from API'

if __name__ == '__main__':
    app.run()
