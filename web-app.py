from flask import Flask, jsonify, request, render_template, abort

app = Flask(__name__)

#creo un dizionario
classe = {
    1: {'nome': 'giuseppe', 'cognome': 'oliviero'},
    2: {'nome': 'luca', 'cognome': 'vespoli'},
    3: {'nome': 'vincenzo', 'cognome': 'orsini'},
    4: {'nome': 'vincenzo', 'cognome': 'milano'}
}

@app.route('/')
def index():
    return 'lista della classe CyberAcademy'

#definiamo il primo metodo get
@app.route('/classe', methods = ['GET'] )
def get_students():
    if request.headers.get('Content-Type') == 'application/json':
       return jsonify(classe)
    else:
        return render_template('classe.html', classe=classe)
    
@app.route('/classe/<int:student_id>', methods = ['GET'])
def get_student(student_id):
    student = classe.get(student_id)
    if student_id in classe:
        if request.headers.get('Content-Type') == 'application/json':   #in postman headers content-type (key) application/json (value)
            return jsonify(classe[student_id])
        else:
            return render_template('student.html', student=student, student_id=student_id)
    else:
        return 'Studente non trovato', 404
    
@app.route('/add_student', methods=['POST'])
def add_student():
    if request.method == 'POST':
        


        if request.headers.get('Content-Type') == 'application/x-www-form-urlencoded':
            # Gestione dei dati x-www-form-urlencoded
            nome = request.form.get('nome')  # Ottieni il valore del parametro 'nome'
            cognome = request.form.get('cognome')  # Ottieni il valore del parametro 'cognome'

            if nome and cognome:
                    new_student_id = max(classe.keys(), default=0) + 1
                    classe[new_student_id] = {'nome': nome, 'cognome': cognome}
                    new_student_details = classe[new_student_id]
                    message = f"Studente aggiunto con ID: {new_student_id}"
                    response = {'message': message, 'new_student_details': new_student_details}
                   
                    if request.headers.get('Accept') == 'application/json':
                        return jsonify(response), 201
                    else:
                        mess = f"Studente aggiunto con ID: {new_student_id}"
                        return render_template('popup.html', mess=mess)
                    
            else:
                    return jsonify({'error': 'I dati inviati non sono completi'}), 400
            
        elif request.headers.get('Content-Type') == 'application/json':
            # Gestione dei dati JSON
            data = request.json  # Ottieni i dati dalla richiesta POST
            new_student_id = max(classe.keys()) + 1
            classe[new_student_id] = {'nome': data['nome'], 'cognome': data['cognome']}
            new_student_details = classe[new_student_id]
            message = f"Studente aggiunto con ID: {new_student_id}"
            response = {'message': message, 'new_student_details': new_student_details}

            return jsonify(response), 201
    
        else:
            return "Contenuto non supportato", 406
    else: return 0
    
        
    

@app.route('/add_student', methods=['GET'])
def show_add_student_form():
    return render_template('add_student.html')


if __name__ == '__main__':
    app.run(debug=True)
