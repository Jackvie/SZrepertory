class Celety_test(object):
    """队列秒杀"""
    flag = False
    @celery_app.task(bind=True, name="buy_goods")
    @classmethod
    def buy_goods(cls, *args, **kwargs):
        if cls.flag:
            return JsonResponse({"errmsg":"已售完"})
        # 查询并修改数据库
        with transaction.actomic():
            saveId = transaction.savepoint()
            count = request.GET.get("count")
            sku = SKU.objects.get(id=sku_id)
            if sku.stock > count:
                return JsonResponse({"errmsg":"库存不足"})
            # 购买保存订单
            pass
            if ...
                rollback ...

        tansaction.commitpoint()
        cls.flag = True


# Celery_test.buy_goods.delay(sku_id, count)
