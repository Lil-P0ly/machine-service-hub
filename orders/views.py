from itertools import product
from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render
from carts.models import Cart

from goods.models import Products
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem


def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)

                    if cart_items.exists():
                        # Создать заказ
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            organisation_info=form.cleaned_data['organisation_info'],

                            # requires_delivery=form.cleaned_data['requires_delivery'],
                            # delivery_address=form.cleaned_data['delivery_address'],
                            # payment_on_get=form.cleaned_data['payment_on_get'],
                        )
                        # Создать заказанные товары
                        for cart_item in cart_items:
                            service=cart_item.service
                            # product=cart_item.product
                            name=cart_item.service.name
                            duration=cart_item.service.duration
                            quantity=cart_item.quantity


                            # if product.quantity < quantity:
                            #     raise ValidationError(f'Недостаточное количество товара {name} на складе\
                            #                            В наличии - {product.quantity}')

                            OrderItem.objects.create(
                                order=order,
                                # product=product,
                                name=name,
                                duration=duration,
                                quantity=quantity,
                            )
                            # product.quantity -= quantity
                            # product.save()

                        # Очистить корзину пользователя после создания заказа
                        cart_items.delete()

                        messages.success(request, 'Заказ оформлен!')
                        return redirect('user:profile')
            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('cart:order')
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            }

        form = CreateOrderForm(initial=initial)

    context = {
        'title': 'Machine Service Hub - Оформление заказа',
        'form': form,
    }
    return render(request, 'orders/create_order.html', context=context)