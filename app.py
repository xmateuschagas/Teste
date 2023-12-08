from flask import Flask, request
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__,static_folder='public')

# Configuracao db
db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/add', methods=['GET','POST'])
def add():
  if request.method=='POST':
    user_details = request.form
    primeiro_nome = user_details['primeiro_nome']
    sobrenome = user_details['sobrenome']
    data_admissao = user_details['data_admissao']
    id_setor = user_details['id_setor']
    id_cargo = user_details['id_cargo']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO funcionario(primeiro_nome, sobrenome, data_admissao, id_setor, id_cargo) VALUES(%s, %s, %s, %s, %s)", (primeiro_nome, sobrenome, data_admissao, id_setor, id_cargo))
    mysql.connection.commit()
    cur.close()
    return 'success'
  return 'OK,GET'
    

if __name__ == '__main__':
  app.run(debug=True)