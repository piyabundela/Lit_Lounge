from sqlalchemy import create_engine
from sqlalchemy import text
import mysql.connector
# pip install mysql-connector-python

db_string = "mysql+pymysql://ny8aovsgg0sa7lvn12jx:pscale_pw_mwixYCu5ZQs64CjaG4n1cBNLL5JZzeq8fwJLZhygWLV@aws.connect.psdb.cloud/books"

# db_string = "mysql+pymysql://<username>:<pw>@host/<db_name>"
# db_string is an input for the connection

engine = create_engine ( # Make a connection to the database
  db_string,
  connect_args = {
    "ssl": {
      "ssl_ca": # Certificate for connection
      "/etc/ssl/cert.pem"  # Configuration for a secure connection 
    }
  } )


def load_book(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM booksCOP WHERE id = :val"),
                          dict(val=id))
    books = []
    for rows in result.all():
      books.append(rows._asdict())
  return books


def load_latest():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM booksCOP WHERE date > 2010"))
    books = []
    for rows in result.all():
      books.append(rows._asdict())
  return books


def load_book_high_ratings():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM booksCOP where likes >= 800000"))
    books = []
    for rows in result.all():
      books.append(rows._asdict())
  return books


def load_book_from_genre(genre_input):
  with engine.connect() as conn:
    result = conn.execute(
      text(
        "SELECT * FROM booksCOP WHERE genre0 like Concat('%', :genre_input, '%') OR genre1 like Concat('%', :genre_input, '%') OR genre2 like Concat('%', :genre_input, '%') OR genre3 like Concat('%', :genre_input, '%')"
      ), dict(genre_input=genre_input))
    # dict(val=genre_input))
    books = []
    for rows in result.all():
      books.append(rows._asdict())
    i = len(books)
    if i < 51:
      return books
    else:
      return books[0:51]


def load_book_from_author(author_name):
  inputs = author_name.split()
  size = len(inputs)
  i = 0
  books = []

  with engine.connect() as conn:
    output = conn.execute(
      text(
        "SELECT * FROM booksCOP WHERE author like Concat('%', :fullval , '%')"
      ), dict(fullval=author_name))
    for results in output.all():
      books.append(results._asdict())

    if len(books) == 0:
      while (i < size):
        word = inputs[i]
        result = conn.execute(
          text(
            "SELECT * FROM booksCOP WHERE author like Concat('%', :val , '%')"
          ), dict(val=word))
        for rows in result.all():
          books.append(rows._asdict())
        i += 1

    return books


def load_book_from_bookname(book_input):
  inputs = book_input.split()
  size = len(inputs)
  i = 0
  books = []

  with engine.connect() as conn:
    output = conn.execute(
      text(
        "SELECT * FROM booksCOP WHERE titleComplete like Concat('%', :fullval , '%')"
      ), dict(fullval=book_input))
    for results in output.all():
      books.append(results._asdict())

    if len(books) == 0:
      while (i < size):
        word = inputs[i]
        result = conn.execute(
          text(
            "SELECT * FROM booksCOP WHERE titleComplete like Concat('%', :val , '%')"
          ), dict(val=word))
        for rows in result.all():
          books.append(rows._asdict())
        i += 1

    return books


def load_books_from_search(book_input):
  out1 = load_book_from_genre(book_input)
  out2 = load_book_from_bookname(book_input)
  out3 = load_book_from_author(book_input)
  size2 = len(out2)
  size3 = len(out3)
  i = 0
  j = 0
  while i < size2:
    out1.append(out2[i])
    i += 1
  while j < size3:
    out1.append(out3[j])
    j += 1

  return out1


def generatedict():
  conn = mysql.connector.connect(
    host='aws.connect.psdb.cloud',
    database='books',
    user='ny8aovsgg0sa7lvn12jx',
    password='pscale_pw_mwixYCu5ZQs64CjaG4n1cBNLL5JZzeq8fwJLZhygWLV')

  # Generate data for the dictionary
  # Conn is a connector

  cursor = conn.cursor(dictionary=True)
  cursor.execute("SELECT * FROM booksCOP")
  finaldata = []
  for row in cursor:
    finaldata.append(row)

  return finaldata
  # Full dictionary as obtained from the database
  # print(finaldata)
  cursor.close()
  conn.close()
