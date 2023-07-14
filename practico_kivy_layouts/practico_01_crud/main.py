"""
1) Realizar un CRUD (puede ser de un producto, personas, etc) empleando KIVY 
y SQLITE (dado por el Profesor de Teoría), empaquetarlo empleando Buildozer
y subir el código y el empaquetado (APK) al GITHUB.
- Los campos deben ser validados a la hora de dar un alta o modificación.
- Se debe emplear lo más posible el lenguaje intermedio KV.

2) Elegir un Widgets de UX complejo y de comportamiento y armar un ejemplo de uso sencillo y subirlo al GITHUB (uno por grupo)
"""

import sqlite3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class AlumnoDB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS alumnos
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre TEXT,
                            edad INTEGER,
                            email TEXT)''')
        self.conn.commit()

    def insertar_alumno(self, nombre, edad, email):
        self.cursor.execute("INSERT INTO alumnos (nombre, edad, email) VALUES (?, ?, ?)",
                            (nombre, edad, email))
        self.conn.commit()

    def actualizar_alumno(self, id_alumno, nombre, edad, email):
        self.cursor.execute("UPDATE alumnos SET nombre=?, edad=?, email=? WHERE id=?",
                            (nombre, edad, email, id_alumno))
        self.conn.commit()

    def eliminar_alumno(self, id_alumno):
        self.cursor.execute("DELETE FROM alumnos WHERE id=?", (id_alumno,))
        self.conn.commit()

    def obtener_todos_los_alumnos(self):
        self.cursor.execute("SELECT * FROM alumnos")
        return self.cursor.fetchall()

class AlumnoCRUD(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.label = Label(text="CRUD de Alumnos", size_hint=(1, 0.1))
        self.add_widget(self.label)

        self.nombre_input = TextInput(hint_text="Nombre", size_hint=(1, 0.1))
        self.add_widget(self.nombre_input)

        self.edad_input = TextInput(hint_text="Edad", size_hint=(1, 0.1))
        self.add_widget(self.edad_input)

        self.email_input = TextInput(hint_text="Email", size_hint=(1, 0.1))
        self.add_widget(self.email_input)

        self.agregar_button = Button(text="Agregar", size_hint=(1, 0.1))
        self.agregar_button.bind(on_press=self.agregar_alumno)
        self.add_widget(self.agregar_button)

        self.actualizar_button = Button(text="Actualizar", size_hint=(1, 0.1))
        self.actualizar_button.bind(on_press=self.actualizar_alumno)
        self.add_widget(self.actualizar_button)

        self.eliminar_button = Button(text="Eliminar", size_hint=(1, 0.1))
        self.eliminar_button.bind(on_press=self.eliminar_alumno)
        self.add_widget(self.eliminar_button)

        self.lista_alumnos_label = Label(text="Lista de Alumnos", size_hint=(1, 0.1))
        self.add_widget(self.lista_alumnos_label)

        self.lista_alumnos = TextInput(multiline=True, readonly=True, size_hint=(1, 0.4))
        self.add_widget(self.lista_alumnos)

        self.db = AlumnoDB("alumnos.db")
        self.actualizar_lista_alumnos()

    def agregar_alumno(self, instance):
        nombre = self.nombre_input.text.strip()
        edad = self.edad_input.text.strip()
        email = self.email_input.text.strip()

        if nombre and edad and email:
            self.db.insertar_alumno(nombre, edad, email)
            self.actualizar_lista_alumnos()
            self.limpiar_campos()

    def actualizar_alumno(self, instance):
        nombre = self.nombre_input.text.strip()
        edad = self.edad_input.text.strip()
        email = self.email_input.text.strip()

        if nombre and edad and email:
            alumno_seleccionado = self.lista_alumnos.text.split("\n")[0]
            id_alumno = alumno_seleccionado.split(":")[0]

            self.db.actualizar_alumno(id_alumno, nombre, edad, email)
            self.actualizar_lista_alumnos()
            self.limpiar_campos()

    def eliminar_alumno(self, instance):
        alumno_seleccionado = self.lista_alumnos.text.split("\n")[0]
        id_alumno = alumno_seleccionado.split(":")[0]

        self.db.eliminar_alumno(id_alumno)
        self.actualizar_lista_alumnos()
        self.limpiar_campos()

    def actualizar_lista_alumnos(self):
        alumnos = self.db.obtener_todos_los_alumnos()
        self.lista_alumnos.text = ""
        for alumno in alumnos:
            info_alumno = f"{alumno[0]}: {alumno[1]}, {alumno[2]}, {alumno[3]}\n"
            self.lista_alumnos.text += info_alumno

    def limpiar_campos(self):
        self.nombre_input.text = ""
        self.edad_input.text = ""
        self.email_input.text = ""

class AlumnoCRUDApp(App):
    def build(self):
        return AlumnoCRUD()

if __name__ == '__main__':
    AlumnoCRUDApp().run()