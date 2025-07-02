## utilities/structures_datatypes

# def get_valid_datatypes(file_name: str) -> dict:
#     if file_name == "cmdr_log_auditoria.xlsx":
#         return {
#             "log_name": "object",
#             "event": "object",
#             "description": "object",
#             "causer_id": "int64",
#             "subject_type": "object",
#             "subject_id": "int64",
#             "claim_id": "int64",
#             "properties": "object",
#             "created_at": "datetime64[ns]",
#             "updated_at": "datetime64[ns]"
#         }
#     return {}

def get_valid_datatypes(file_name: str) -> dict:
    if file_name == "cmdr_glosas_parciales_adres.xlsx":
        return {
            "numero_paquete": "int64",  # Usa 'Int64' con mayúscula si hay NULLs
            "id_reclamacion": "int64",
            "numero_radicado": "int64",
            "id_item": "int64",
            "codigo_glosa": "int64",
            "anotacion": "object",  # 'text' en SQL → 'string' en pandas moderno
            "cantidad_aprobado": "int64",
            "valor_unitario_aprobado": "float64",
            "valor_total_aprobado": "float64",
            "valor_total_glosado": "float64",
            "id_componente": "int64",
            "estado": "int64",
            "created_at": "datetime64[ns]"
        }
    return {}

# def get_valid_datatypes(file_name: str) -> dict:
#     if file_name == "cmdr_glosas_totales_masivas.xlsx":
#         return {
#             "id_entrega": "int64",  
#             "id_reclamacion": "int64",
#             "numero_radicado": "int64",
#             "codigo_glosa": "int64",
#             "anotacion": "object",  
#             "id_componente": "int64"
#         }
#     return {}