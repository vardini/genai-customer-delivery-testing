def get_order_details(order_id: str) -> dict | None:
    """
    Simulates an order management system.
    This is controlled test data (VERY IMPORTANT for GenAI testing).
    """

    mock_orders = {
        "ORD123": {
            "order_id": "ORD123",
            "status": "Shipped",
            "delivery_date": "2025-02-10",
            "items": ["Laptop", "Mouse"],
            "shipping_address": "Bangalore"
        },
        "ORD999": {
            "order_id": "ORD999",
            "status": "Delayed",
            "delivery_date": "2025-02-15",
            "items": ["Phone"],
            "shipping_address": "Chennai"
        }
    }

    return mock_orders.get(order_id)
