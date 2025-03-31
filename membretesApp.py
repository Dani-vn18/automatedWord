import streamlit as st
import mysql.connector
import os

# Configurar conexión usando el endpoint privado
db_host = os.environ.get("RAILWAY_PRIVATE_DOMAIN")
db_user = os.environ.get("MYSQL_USER")
db_password = os.environ.get("MYSQL_PASSWORD")
db_database = os.environ.get("MYSQL_DATABASE")

try:
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_database
    )
    cursor = conn.cursor()
    st.success("Conexión establecida con la base de datos.")
except Exception as e:
    st.error(f"Error de conexión: {e}")
    st.stop()

query_string = st.text_area("Ingresa tu consulta SQL:")

if st.button("Ejecutar Query"):
    if query_string.strip() == "":
        st.warning("Por favor, ingresa una consulta SQL.")
    else:
        try:
            cursor.execute(query_string)
            # Si es un SELECT, muestra resultados
            if query_string.strip().upper().startswith("SELECT"):
                results = cursor.fetchall()
                st.write("Resultados:", results)
            else:
                conn.commit()
                st.success("Query ejecutada exitosamente.")
        except Exception as e:
            st.error(f"Error al ejecutar la query: {e}")

