# 写我们的任务
# 任务必须要celery的实例对象装饰器task装饰
# 任务包的唔唔需要celery调用自检检查函数

from celery_tasks.main import app
from ronglian_sms_sdk import SmsSDK


@app.task
def celery_send_sms_code(mobile, sms_code):
    print(11111111111111111111111111111)
    accId = '8aaf0708762cb1cf0176c60392973587'
    accToken = 'a099e3b6a8a14e09bae6d133051decb9'
    appId = '8aaf0708762cb1cf0176c603936b358e'
    sdk = SmsSDK(accId, accToken, appId)
    print(22222222222222222222222222222)
    tid = '1'  # 因为是测试用户 所以我们发送短信的模板只能是1
    mobile = f'{mobile}'
    datas = (sms_code, 10)  # 涉及到模板的变量
    # 您的验证码为 1 请于 2 分钟内输入
    resp = sdk.sendMessage(tid, mobile, datas)
    print(resp)
    # return JsonResponse({'code': 0, 'errmsg': '验证码发送成功'})
