import hashlib
import json
from datetime import datetime

ledger = []


def log_action(action, user):
    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "action": action,
        "user": user
    }
    record_hash = hashlib.sha256(json.dumps(record).encode()).hexdigest()
    ledger.append({"record": record, "hash": record_hash})
    print(f"Action logged: {record_hash}")


# Example
log_action("SYSTEM_START", "Ervin Remus Radosavlevici")