from flask import Flask, render_template_string
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    
    conn = mysql.connector.connect(
        host='mysql-db',
        user='root',
        password='root',
        database='myapp'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

   
    html = """
    <!DOCTYPE html>
    <html>
      <body>
        <h1>PowerBI Mock - Showing Users</h1>
        <table border="1">
          <tr><th>ID</th><th>Name</th><th>Age</th></tr>
          {% for row in rows %}
            <tr>
              <td>{{ row[0] }}</td>
              <td>{{ row[1] }}</td>
              <td>{{ row[2] }}</td>
            </tr>
          {% endfor %}
        </table>
      </body>
    </html>
    """
    return render_template_string(html, rows=rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

