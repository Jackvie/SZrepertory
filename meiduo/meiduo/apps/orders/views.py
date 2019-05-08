from django.shortcuts import render
from django.views import View
from django_redis import get_redis_connection
from decimal import Decimal

from meiduo.utils.view import LoginRequiredMixin
from users.models import Address
from goods.models import SKU
# Create your views here.

class OrderSettlementView(LoginRequiredMixin, View):
    """结算订单"""

    def get(self, request):
        """提供订单结算页面"""

        # 获取登录用户
        user = request.user
        # 查询地址信息
        try:
            addresses = Address.objects.filter(user=user, is_deleted=False)
        except Address.DoesNotExist:
            # 如果地址为空，渲染模板时会判断，并跳转到地址编辑页面
            addresses = None

        # 从Redis购物车中查询出被勾选的商品信息
        redis_conn = get_redis_connection("carts")
        redis_cart = redis_conn.hgetall("carts_%s" % user.id)  # {sku_id: count, sku_id2: count2}
        cart_selected = redis_conn.smembers("selected_%s" % user.id)  # {sku_id, sku_id2}

        cart = {}
        for sku_id in cart_selected:
            cart[int(sku_id)] = int(redis_cart.get(sku_id))  # cart = {sku_id: count}
        # cart字典包含被勾选的商品id与count

        # 准备初始值
        total_count = 0  # 商品结算时总数
        total_amount = Decimal(0.00)  # 商品结算时总价
        # 查询商品信息
        skus = SKU.objects.filter(id__in=cart.keys())
        for sku in skus:
            sku.count = cart.get(sku.id)  # 当前sku绑定数量
            sku.amount = sku.count * sku.price  # 当前sku总计
            # 计算总数量和总金额
            total_count += sku.count
            total_amount += sku.amount

        # 补充运费
        freight = Decimal('10.00')

        # 渲染界面
        context = {
            'addresses': addresses,
            'skus': skus,
            'total_count': total_count,
            'total_amount': total_amount,
            'freight': freight,
            'payment_amount': total_amount + freight
        }

        return render(request, 'place_order.html', context)