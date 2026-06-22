from datetime import datetime, timedelta
from decimal import Decimal

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

from core.models import Cart, Product, get_users_created_after_date


class ProductModelTest(TestCase):
    """Testes para o modelo Product"""

    def setUp(self):
        """Configuração inicial para os testes de Product"""
        self.product = Product.objects.create(
            name="Test Product", price=Decimal("10.50")
        )

    def test_product_creation(self):
        """Testa a criação de um produto"""
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.price, Decimal("10.50"))
        self.assertEqual(str(self.product), "Test Product")

    def test_product_field_validation(self):
        """Testa a validação dos campos do produto"""
        # Testa preço negativo (deve falhar)
        with self.assertRaises(ValidationError):
            product = Product(name="Negative Price Product", price=Decimal("-5.00"))
            product.full_clean()

    def test_product_max_length(self):
        """Testa o comprimento máximo do campo nome"""
        long_name = "A" * 101  # Um caractere a mais que o permitido
        product = Product(name=long_name, price=Decimal("10.00"))

        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_product_price_decimal_places(self):
        """Testa a precisão decimal do preço"""
        product = Product.objects.create(
            name="Precise Price Product", price=Decimal("10.123")
        )
        # O Django deve arredondar para 2 casas decimais
        retrieved_product = Product.objects.get(id=product.id)
        self.assertEqual(retrieved_product.price, Decimal("10.12"))

    def test_product_update(self):
        """Testa a atualização de um produto"""
        self.product.name = "Updated Product"
        self.product.price = Decimal("20.00")
        self.product.save()

        updated_product = Product.objects.get(id=self.product.id)
        self.assertEqual(updated_product.name, "Updated Product")
        self.assertEqual(updated_product.price, Decimal("20.00"))

    def test_product_deletion(self):
        """Testa a exclusão de um produto"""
        product_id = self.product.id
        self.product.delete()

        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(id=product_id)


class CartModelTest(TestCase):
    """Testes para o modelo Cart"""

    def setUp(self):
        """Configuração inicial para os testes de Cart"""
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.product = Product.objects.create(
            name="Cart Test Product", price=Decimal("15.75")
        )
        self.cart_item = Cart.objects.create(
            product=self.product, user=self.user, quantity=2
        )

    def test_cart_item_creation(self):
        """Testa a criação de um item no carrinho"""
        self.assertEqual(self.cart_item.product, self.product)
        self.assertEqual(self.cart_item.user, self.user)
        self.assertEqual(self.cart_item.quantity, 2)
        self.assertEqual(str(self.cart_item), "Cart Test Product")

    def test_cart_item_default_quantity(self):
        """Testa a quantidade padrão de um item no carrinho"""
        cart_item = Cart.objects.create(product=self.product, user=self.user)
        self.assertEqual(cart_item.quantity, 1)

    def test_cart_item_calculate_subtotal(self):
        """Testa o cálculo do subtotal (embora não esteja implementado automaticamente no modelo)"""
        expected_subtotal = self.product.price * self.cart_item.quantity
        # O subtotal não é calculado automaticamente, então precisaria ser feito manualmente ou com uma propriedade
        self.assertEqual(expected_subtotal, Decimal("31.50"))

    def test_cart_item_foreign_key_relationships(self):
        """Testa as relações de chave estrangeira"""
        self.assertEqual(self.cart_item.product.name, "Cart Test Product")
        self.assertEqual(self.cart_item.user.username, "testuser")

    def test_cart_item_update(self):
        """Testa a atualização de um item no carrinho"""
        self.cart_item.quantity = 5
        self.cart_item.subtotal = Decimal("78.75")  # 5 * 15.75
        self.cart_item.save()

        updated_cart_item = Cart.objects.get(id=self.cart_item.id)
        self.assertEqual(updated_cart_item.quantity, 5)
        self.assertEqual(updated_cart_item.subtotal, Decimal("78.75"))

    def test_cart_item_deletion(self):
        """Testa a exclusão de um item no carrinho"""
        cart_item_id = self.cart_item.id
        self.cart_item.delete()

        with self.assertRaises(Cart.DoesNotExist):
            Cart.objects.get(id=cart_item_id)

    def test_cascade_deletion_product(self):
        """Testa a exclusão em cascata quando o produto é excluído"""
        product_id = self.product.id
        self.product.delete()

        with self.assertRaises(Cart.DoesNotExist):
            Cart.objects.get(id=self.cart_item.id)

    def test_cascade_deletion_user(self):
        """Testa a exclusão em cascata quando o usuário é excluído"""
        user_id = self.user.id
        self.user.delete()

        with self.assertRaises(Cart.DoesNotExist):
            Cart.objects.get(id=self.cart_item.id)


class GetUserCreatedAfterDateTest(TestCase):
    """Testes para a função get_users_created_after_date"""

    def setUp(self):
        """Configuração inicial para os testes da função"""
        # Cria usuários em diferentes datas
        past_date = timezone.now() - timedelta(days=2)
        self.old_user = User.objects.create_user(
            username="olduser", password="testpass", date_joined=past_date
        )

        future_date = timezone.now() + timedelta(
            days=1
        )  # Isso será ajustado para agora para fins de teste
        self.new_user = User.objects.create_user(
            username="newuser", password="testpass"
        )  # Este terá data de agora

    def test_get_users_created_after_date(self):
        """Testa a função get_users_created_after_date"""
        # Define uma data intermediária
        reference_date = timezone.now() - timedelta(days=1)

        # Apenas o novo usuário deve aparecer (considerando que ele foi criado após a data de referência)
        # Precisamos recriar os usuários com datas específicas para o teste
        User.objects.all().delete()

        # Usuários criados antes da data de referência
        old_user1 = User.objects.create_user(
            username="olduser1",
            password="testpass",
            date_joined=timezone.make_aware(datetime(2020, 1, 1)),
        )
        old_user2 = User.objects.create_user(
            username="olduser2",
            password="testpass",
            date_joined=timezone.make_aware(datetime(2021, 1, 1)),
        )

        # Usuários criados após a data de referência
        new_user1 = User.objects.create_user(
            username="newuser1",
            password="testpass",
            date_joined=timezone.make_aware(datetime(2023, 1, 1)),
        )
        new_user2 = User.objects.create_user(
            username="newuser2",
            password="testpass",
            date_joined=timezone.make_aware(datetime(2024, 1, 1)),
        )

        # Busca por usuários criados após 31/12/2022
        users_after_2022 = get_users_created_after_date(2022, 12, 31)

        # Verifica que apenas os usuários criados após a data estão na lista
        self.assertEqual(users_after_2022.count(), 2)
        self.assertIn(new_user1, users_after_2022)
        self.assertIn(new_user2, users_after_2022)
        self.assertNotIn(old_user1, users_after_2022)
        self.assertNotIn(old_user2, users_after_2022)

    def test_get_users_created_after_date_edge_case(self):
        """Testa caso limite da função get_users_created_after_date"""
        User.objects.all().delete()

        # Usuário criado exatamente na data de referência
        exact_date_user = User.objects.create_user(
            username="exactdateuser",
            password="testpass",
            date_joined=timezone.make_aware(datetime(2023, 6, 15)),
        )

        # Outro usuário criado após a data de referência
        after_date_user = User.objects.create_user(
            username="afterdateuser",
            password="testpass",
            date_joined=timezone.make_aware(datetime(2023, 6, 16)),
        )

        # Busca por usuários criados após 15/06/2023
        users_after_date = get_users_created_after_date(2023, 6, 15)

        # O usuário criado exatamente na data NÃO deve estar incluído
        # Somente o usuário criado após a data deve estar incluído
        self.assertEqual(users_after_date.count(), 1)
        self.assertIn(after_date_user, users_after_date)
        self.assertNotIn(exact_date_user, users_after_date)
