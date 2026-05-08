from src.app import answer_customer_question

policy = open("data/delivery_policy.txt").read()

response = answer_customer_question(
    order_id="ORD123",
    question="When will my order be delivered?",
    policy_text=policy
)

print(response)


