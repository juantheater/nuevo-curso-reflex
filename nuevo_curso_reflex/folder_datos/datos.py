import reflex as rx
import sqlmodel
from datetime import datetime
from typing import List,Optional,Dict
from .model import Dato


class DatoState(rx.State):
    """Estado para nuestra aplicacion de tareas"""

    new_title:str=""
    new_description:str=""

    #Lista de tareas
    datos=List[Dict]=[]

    #Variable de identificacion
    editing_id:Optional[int]=None

    def load_datos(self):
        """Carga las tareas desde la base de datos"""

        try:
            with rx.session() as session:
                #Obtener todas las tareas de la base de datos
                db_datos=session.exec(sqlmodel.select(Dato)).all()

                #Convertir en diccionario
                formatted_datos=[]
                for item in db_datos:
                    dato_dict=item.model_dump()
                    dato_dict["formatted_date"]=(
                        item.created_at.strftime("%d/%m/%Y %H:%M")
                        if item.created_at
                        else ""
                    )

                    formatted_datos.append(dato_dict)
                self.datos=formatted_datos
        except Exception as e:
            print(f"Error al cargar datos: {e}")
            self.datos


    def add_datos(self,form_data:dict):
        """Agrega una nueva tarea"""
        title=form_data.get("title","").strip()
        description=form_data.get("description","").strip()

        if not title:
            return rx.window_alert("El titulo no puede estar vacio")
        
        try:
            with rx.session() as session:
                dato=Dato(
                    title=title,
                    description=description if description else None,
                    created_at=datetime.now()
                )
                session.add(dato)
                session.commit()

                #Recargar tareas
                self.load_datos()

                #Mensaje de confirmacion
                return [
                    rx.call_script("document.getElementById('dato_form').reset();"),
                    rx.window_alert("Tarea agregada correctamente")
                ]
        except Exception as e:
            return rx.window_alert(f"Error al guardar la tarea: {str(e)}")
        

    def delete_dato(self,dato_id:int):
        """Funcion para borrar datos"""
        try:
            with rx.session() as session:
                dato=session.query(Dato).filter(Dato.id==dato.id).first()

                if dato:
                    session.delete(dato)
                    session.commit()
                    self.load_datos()
        except Exception as e:
            return rx.window_alert(f"No se pudo eliminar la tarea: {str(e)}")