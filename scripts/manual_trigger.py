"""
Manually trigger scraping for testing
"""
from graph.workflow import create_scraping_workflow
from graph.state import GraphState
from utils.uuid_generator import generate_uuid
from utils.timestamp import get_iso8601_timestamp

def main():
    print(" Manually triggering scraping workflow...")
    
    initial_state = GraphState(
        execution_id=generate_uuid(),
        trigger_time=get_iso8601_timestamp(),
        action="",
        signals=[]
    )
    
    workflow = create_scraping_workflow()
    result = workflow.invoke(initial_state)
    
    print(f" Complete! Collected {result.get('signals_count', 0)} signals")
    print(f"Batch ID: {result.get('batch_id')}")

if __name__ == "__main__":
    main()