from flask import Flask, render_template, request, redirect, url_for
# from sqlalchemy import text
from database import load_book, load_book_from_genre, load_book_high_ratings, load_book_from_bookname, load_book_from_author, load_latest, load_books_from_search

app = Flask(
  __name__,
  template_folder="templates",  # name of folder containing html templates
  static_folder="static"  # name of folder for static files
)

# @app.route("/")
# def hello_book():
#   booksdynamic = generatedict()
#   hot_picks = booksdynamic[30:36]
#   return render_template('reviewconnect.html', booksinput=hot_picks)


@app.route("/home")
def hello_home():
  output1 = load_latest()
  output2 = load_book_high_ratings()
  return render_template('homepage.html',
                         latestbooks=output1,
                         popularbooks=output2)


@app.route("/home", methods=['POST'])
def search_genre():
  data = request.form
  print(data)
  input = data['search_text']
  print(input)
  output = load_books_from_search(input)
  # print(output)
  return redirect(url_for('hello_searched_genre', inp=output))
  # return render_template('finalrecomm.html')


# @app.route("/search/genre")
# def hello_searched_genre(inp):
# out = load_book_from_genre(inp)
# return render_template('finalrecomm.html')


@app.route("/search", methods=['POST'])
def hello_searched_genre():
  data = request.form
  inp = data['search_text']
  out = load_books_from_search(inp)
  return render_template('finalrecomm.html', booksinput=out)


@app.route("/overview/<book_id>")
def hello_specific_book(book_id):
  output1 = load_book(book_id)
  return render_template('finalreview.html', booksinput=output1)


@app.route("/overview/<book_id>", methods=['POST'])
def search_genre1():
  data = request.form
  print(data)
  input = data['search_text']
  print(input)
  output = load_books_from_search(input)
  # print(output)
  return redirect(url_for('hello_searched_genre', inp=output))


@app.route("/genre/<genre_input>")
def hello_genre(genre_input):
  output2 = load_book_from_genre(genre_input)
  return render_template('finalrecomm.html', booksinput=output2)


@app.route("/genre/<genre_input>", methods=['POST'])
def search_genre2():
  data = request.form
  print(data)
  input = data['search_text']
  print(input)
  output = load_books_from_search(input)
  # print(output)
  return redirect(url_for('hello_searched_genre', inp=output))


@app.route("/book/<bookname_input>")
def hello_book(bookname_input):
  output2 = load_book_from_bookname(bookname_input)
  return render_template('finalrecomm.html', booksinput=output2)


@app.route("/book/<bookname_input>", methods=['POST'])
def search_genre3():
  data = request.form
  print(data)
  input = data['search_text']
  print(input)
  output = load_books_from_search(input)
  # print(output)
  return redirect(url_for('hello_searched_genre', inp=output))


@app.route("/author/<author_input>")
def hello_author(author_input):
  output2 = load_book_from_author(author_input)
  return render_template('finalrecomm.html', booksinput=output2)


@app.route("/author/<author_input>", methods=['POST'])
def search_genre4():
  data = request.form
  print(data)
  input = data['search_text']
  print(input)
  output = load_books_from_search(input)
  # print(output)
  return redirect(url_for('hello_searched_genre', inp=output))


@app.route("/popularbooks")
def hello_popular_seeall():
  output = load_book_high_ratings()
  return render_template('finalrecomm.html', booksinput=output)


@app.route("/popularbooks", methods=['POST'])
def search_genre5():
  data = request.form
  print(data)
  input = data['search_text']
  print(input)
  output = load_books_from_search(input)
  # print(output)
  return redirect(url_for('hello_searched_genre', inp=output))


@app.route("/latest")
def hello_latest():
  output = load_latest()
  return render_template('finalrecomm.html', booksinput=output)


@app.route("/latest", methods=['POST'])
def search_genre6():
  data = request.form
  print(data)
  input = data['search_text']
  print(input)
  output = load_books_from_search(input)
  # print(output)
  return redirect(url_for('hello_searched_genre', inp=output))


# @app.route("/searches/genre/<input>")
# def hello_genre_search(input):
#   data = request.args
#   output = load_book_from_genre(data)
#   return render_template('finalrecomm.html', booksinput=output)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
