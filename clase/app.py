import uuid
from flask import Flask, render_template, request, jsonify, session
from structures import Stack, Queue

app = Flask(__name__)
app.secret_key = "clave_segura_pila_cola_python_2026"

# Almacenamiento en RAM por usuario: { 'uuid': {'stack': Stack(), 'queue': Queue()} }
USER_DATA: dict[str, dict] = {}

def get_user_structures() -> dict:
    """Garantiza instancias independientes de Pila y Cola por sesión."""
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())
    
    user_id = session['user_id']
    if user_id not in USER_DATA:
        USER_DATA[user_id] = {
            'stack': Stack(capacity=5),
            'queue': Queue(capacity=5)
        }
    
    return USER_DATA[user_id]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/state', methods=['GET'])
def get_state():
    """Retorna el estado de ambas estructuras (Pila y Cola)."""
    structs = get_user_structures()
    return jsonify({
        'stack': {
            'items': structs['stack'].get_items(),
            'capacity': structs['stack'].capacity,
            'is_empty': structs['stack'].is_empty(),
            'is_full': structs['stack'].is_full()
        },
        'queue': {
            'items': structs['queue'].get_items(),
            'capacity': structs['queue'].capacity,
            'is_empty': structs['queue'].is_empty(),
            'is_full': structs['queue'].is_full()
        }
    })

@app.route('/api/config', methods=['POST'])
def set_config():
    """Reconfigura la capacidad de la Pila o la Cola."""
    data = request.get_json() or {}
    struct_type = data.get('struct', 'stack')
    
    try:
        capacity = int(data.get('capacity', 5))
        if capacity < 1 or capacity > 15:
            return jsonify({'success': False, 'message': 'La capacidad debe estar entre 1 y 15.'}), 400
        
        structs = get_user_structures()
        target = structs['stack'] if struct_type == 'stack' else structs['queue']
        
        target.capacity = capacity
        target.clear()
        
        nombre_str = "Pila" if struct_type == "stack" else "Cola"
        return jsonify({
            'success': True,
            'message': f'{nombre_str} reiniciada con capacidad de {capacity} posiciones.',
            'items': target.get_items(),
            'capacity': target.capacity
        })
    except ValueError:
        return jsonify({'success': False, 'message': 'Número de capacidad no válido.'}), 400

@app.route('/api/add', methods=['POST'])
def add_item():
    """Apilar (Push) o Encolar (Enqueue)."""
    data = request.get_json() or {}
    struct_type = data.get('struct', 'stack')  # 'stack' o 'queue'
    item_type = data.get('type')                # 'text' o 'image'
    content = str(data.get('content', '')).strip()

    if item_type not in ['text', 'image'] or not content:
        return jsonify({'success': False, 'message': 'Datos recibidos incompletos o inválidos.'}), 400

    structs = get_user_structures()
    if struct_type == 'stack':
        success, message = structs['stack'].push(item_type, content)
        target = structs['stack']
    else:
        success, message = structs['queue'].enqueue(item_type, content)
        target = structs['queue']

    if success:
        return jsonify({
            'success': True,
            'message': message,
            'items': target.get_items(),
            'capacity': target.capacity
        })
    return jsonify({'success': False, 'message': message}), 400

@app.route('/api/remove', methods=['POST'])
def remove_item():
    """Desapilar (Pop) o Desencolar (Dequeue)."""
    data = request.get_json() or {}
    struct_type = data.get('struct', 'stack')
    
    structs = get_user_structures()
    if struct_type == 'stack':
        success, removed_item, message = structs['stack'].pop()
        target = structs['stack']
    else:
        success, removed_item, message = structs['queue'].dequeue()
        target = structs['queue']

    if success:
        return jsonify({
            'success': True,
            'message': message,
            'item': removed_item,
            'items': target.get_items(),
            'capacity': target.capacity
        })
    return jsonify({'success': False, 'message': message}), 400

@app.route('/api/peek', methods=['GET'])
def peek_item():
    """Inspeccionar Tope (Pila) o Frente (Cola)."""
    struct_type = request.args.get('struct', 'stack')
    structs = get_user_structures()
    
    target = structs['stack'] if struct_type == 'stack' else structs['queue']
    success, item, message = target.peek()

    if success:
        return jsonify({
            'success': True,
            'message': message,
            'item': item
        })
    return jsonify({'success': False, 'message': message}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)