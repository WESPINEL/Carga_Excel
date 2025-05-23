def get_valid_columns(file_name: str) -> list[str]:
    if file_name == "cmdr_log_auditoria.xlsx":
        return [
            "log_name", "event", "description", "causer_id", "subject_type",
            "subject_id", "claim_id", "properties", "created_at", "updated_at"
        ]
    return []
