from flask import request, jsonify
from config import app, db
from models import Seccion, Carrera, Estudiante, EstudiantePorSeccion
from analisis import limpieza

limpieza()


@app.route('/secciones', methods=['GET'])
def get_secciones():
    secciones = Seccion.query.all()
    json_secciones = list(map(lambda seccion: seccion.to_json(), secciones))
    return jsonify({"secciones":json_secciones})

@app.route('/estudiantes', methods=['GET'])
def get_estudiantes():
    estudiantes = Estudiante.query.all()
    json_estudiantes = list(map(lambda estudiante: estudiante.to_json(), estudiantes))
    return jsonify({"estudiantes":json_estudiantes})

@app.route('/carreras', methods=['GET'])
def get_carrera():
    carreras = Carrera.query.all()
    json_carreras = list(map(lambda carrera: carrera.to_json(), carreras))
    return jsonify({"carreras":json_carreras})

@app.route('/estudiantesPorSeccion', methods=['GET'])
def get_estudiantesPorSeccion():
    estudiantesPorSeccion = EstudiantePorSeccion.query.all()
    json_estudiantesPorSeccion = list(map(lambda estudiantePorSeccion: estudiantePorSeccion.to_json(), estudiantesPorSeccion))
    return jsonify({"estudiantesPorSeccion":json_estudiantesPorSeccion})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)