from flask import Flask, render_template
import psycopg2
import config

app = Flask(__name__)

app.route('/api/update_basket_a')
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
    except:
        print('failed to connect to database')
        
    try:
        query = 'INSERT INTO basket_a (a, fruit_a) VALUES (5, \'Cherry\')'
        cursor.execute(query)
        return render_template('update.html', log_html = 'Success!')
    except(Exception, psycopg2.Error) as error:
        return render_template('update.html', log_html = record2)
    
    cursor.close()
    connection.close()
    
    # record = util.run_and_fetch_sql(cursor, "insert into basket_a(a, fruit_a)")
    # if record == -1:
    #     print('first query failed')
    
    # record2 = util.run_and_fetch_sql(cursor, "")
    # if record == -1:
    #     print('second query failed')

    # record3 = util.run_and_fetch_sql(cursor, "")
    # if record == -1:
    #     print('third query failed')
    
    
        
if __name__ == '__main__':
    app.debug = True
    ip = '127.0.0.1'
    app.run(host=ip)