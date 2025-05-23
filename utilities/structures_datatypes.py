def get_valid_datatypes(file_name: str) -> dict:
    if file_name == "cmdr_log_auditoria.xlsx":
        return {
            "log_name": "object",
            "event": "object",
            "description": "object",
            "causer_id": "int64",
            "subject_type": "object",
            "subject_id": "int64",
            "claim_id": "int64",
            "properties": "object",
            "created_at": "datetime64[ns]",
            "updated_at": "datetime64[ns]"
        }
    return {}

