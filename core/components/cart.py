from decimal import Decimal

from django_unicorn.components import UnicornView

from core.models import Cart, Product


class CartView(UnicornView):
    user: int

    products: list = []
    cart_items: list = []
    total: Decimal = Decimal("0.00")
    user_name: str = ""

    def get_user_name(self, user_name):
        return user_name

    def mount(self):
        self.load_products()
        self.load_cart()

    # ---------- LOADERS ----------

    def load_products(self):
        self.products = list(Product.objects.values("id", "name", "price"))

    def load_cart(self):
        items = Cart.objects.filter(user_id=self.user).select_related("product")

        self.cart_items = [
            {
                "id": item.id,
                "product_id": item.product.id,
                "name": item.product.name,
                "price": item.product.price,
                "quantity": item.quantity,
                "subtotal": item.product.price * item.quantity,
            }
            for item in items
        ]

        self.total = sum(item["subtotal"] for item in self.cart_items)

    # ---------- ACTIONS ----------

    def add_item(self, product_id: int):
        item, created = Cart.objects.get_or_create(
            user_id=self.user,
            product_id=product_id,
        )
        if not created:
            item.quantity += 1
            item.save()

        self.load_cart()

    def remove_item(self, product_id: int):
        item = Cart.objects.get(user_id=self.user, product_id=product_id)
        if item.quantity > 1:
            item.quantity -= 1
            item.save()
        else:
            item.delete()

        self.load_cart()

    def clear_cart(self):
        Cart.objects.filter(user_id=self.user).delete()
        self.load_cart()
