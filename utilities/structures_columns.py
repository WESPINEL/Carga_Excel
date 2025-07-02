# utilities/structures_columns

def get_valid_columns(file_name: str) -> list[str]: 
    if file_name == "cmdr_glosas_parciales_adres.xlsx":
        return [
            "numero_paquete",
            "id_reclamacion",
            "numero_radicado",
            "id_item",
            "codigo_glosa",
            "anotacion",
            "cantidad_aprobado",
            "valor_unitario_aprobado",
            "valor_total_aprobado",
            "valor_total_glosado",
            "id_componente",
            "estado",
            "created_at"
        ]
    elif file_name == "cmdr_glosas_totales_masivas.xlsx":
        return [
            "id_entrega",
            "id_reclamacion",
            "numero_radicado",
            "codigo_glosa",
            "anotacion",
            "id_componente"
        ]
    elif file_name == "cmdr_log_auditoria.xlsx":
        return [
            "log_name", "event", "description", "causer_id", "subject_type",
            "subject_id", "claim_id", "properties", "created_at", "updated_at"
        ]
    return []
