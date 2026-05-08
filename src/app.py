from src.order_context.order_service import get_order_details
from src.llm.prompt_templates import delivery_prompt
from src.llm.llm_client import get_llm_response

def answer_customer_question(order_id: str, question: str, policy_text: str) -> str:
    """
    System Under Test (SUT)

    - Fetch order context
    - Build GenAI prompt
    - Call LLM
    - Return response
    """
    order = get_order_details(order_id)

    if not order:
        return "Order not found."

    prompt = delivery_prompt(
        order=order,
        policy=policy_text,
        question=question
    )

    return get_llm_response(prompt)
