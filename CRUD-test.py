import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database= 'bdlogins'
)

cursor = conexao.cursor()

#CRUD

#comando = ''
#cursor.execute(comando)
#conexao.commit() ->EDITA O BANCO DE DADOS
#resultado = cursor.fetchall() -> LER O BANCO DE DADOS

#CREATE

nome_user = "Grauber"
senha_user = "remela123"
comando = f'INSERT INTO login_db (nome_user, senha_user) VALUES ("{nome_user}", "{senha_user}") '
cursor.execute(comando)
conexao.commit()



#READ
"""
comando = f'SELECT * FROM login_db'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)
"""


#UPDATE
"""
comando = f'UPDATE login_db SET senha_user = "demon666" WHERE nome_user = "Grauber" '
cursor.execute(comando)
conexao.commit()
"""



#DELETE
"""
comando = f'DELETE FROM login_db'
cursor.execute(comando)
conexao.commit()


id_user=0
"""




cursor.close()
conexao.close()