from ..models import Client, Product, Order
import random
from datetime import datetime, timedelta, timezone


def create_fake(request):
    for i in range(5):
        Client.objects.create(name=f'Client {i}', email=f'email{i}@example.com', number=f'123456789{i}', address=f'address{i}')

    for i in range(5):
        Product.objects.create(name=f'Product {i}', description=f'description{i}', price=f'{i}', count=i)


def generate_orders():
    # Определение диапазона значений для id и client_id
    id_range = range(1, 6)
    client_id_range = range(1, 6)

    # Генерация 20 записей
    for _ in range(20):
        order = Order()
        order.id = random.choice(list(id_range))
        order.client_id = random.choice(list(client_id_range))
        order.total_price = random.randint(100, 1000)

        # Генерация случайной даты в последних 365 днях
        end_date = timezone.now().date()
        start_date = end_date - timedelta(days=365)
        random_date = datetime.fromordinal(random.randint(start_date.toordinal(), end_date.toordinal()))
        order.date_ordered = random_date

        # Сохранение записи в базе данных
        order.save()


if __name__ == '__main__':
    generate_orders()
