from flask import Flask, render_template
import psycopg2
from config import config

app = Flask(__name__)

@app.route('/api/update_basket_a')
def update():
    try:
        connection = psycopg2.connect(
            user=config.username,
            password=config.password,
            host=config.host,
            port=config.port,
            database=config.database
        )
        cursor = connection.cursor()
    except(Exception, psycopg2.Error) as error:
        return render_template('update.html', log_html = error)
        
    try:
        query = 'INSERT INTO basket_a (a, fruit_a) VALUES (5, \'Cherry\')'
        cursor.execute(query)
        return render_template('update.html', log_html = 'Success!')
    except(Exception, psycopg2.Error) as error:
        return render_template('update.html', log_html = error)
    
    cursor.close()
    connection.close()
    
@app.route('/api/unique')
def unique():
    try:
        connection = psycopg2.connect(
            user=config.username,
            password=config.password,
            host=config.host,
            port=config.port,
            database=config.database
        )
        cursor = connection.cursor()
    except(Exception, psycopg2.Error) as error:
        return render_template('unique.html', log_html = error)
        
    try:
        query = '''
        SELECT fruit_a as unique_fruits from basket_a LEFT JOIN basket_b on fruit_b=fruit_a WHERE b is NULL 
        UNION 
        SELECT fruit_b from basket_b LEFT JOIN basket_a on fruit_a=fruit_b WHERE a is NULL
        '''
        cursor.execute(query)
        col_names = [desc[0] for desc in cursor.description]
        
        return render_template('unique.html', sql_table = cursor.fetchall(), table_title = col_names)
    except(Exception, psycopg2.Error) as error:
        return render_template('unique.html', log_html = error)
    
    cursor.close()
    connection.close()
        
if __name__ == '__main__':
    app.debug = True
    ip = '127.0.0.1'
    app.run(host=ip)