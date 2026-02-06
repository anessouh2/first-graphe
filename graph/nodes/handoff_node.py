from graph.state import GraphState
from storage.redis_client import save_last_scrape_time
from storage.rabbitmq_client import publish_batch
from datetime import datetime
import uuid


def handoff_node(state: GraphState) -> GraphState:
    batch_id = f"batch_{uuid.uuid4().hex}"

    save_last_scrape_time(datetime.utcnow())

    publish_batch({
        "batch_id": batch_id,
        "signals_count": len(state["signals"]),
        "signals": state["signals"]
    })

    return {
        "batch_id": batch_id
    }
