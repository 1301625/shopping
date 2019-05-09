from time import time
from django.conf import settings
from django.templatetags.static import StaticNode
from django import template


register = template.Library()

class FreshStaticNode(StaticNode):
    def url(self, context): #현재 static이라는 템플릿태그를 호출 했을떄에 대한 url를 계산
        url = super().url(context)#StaticNode에서 이미 url를 계산하기 때문에 부모호출에서 url를 획득
        if settings.DEBUG: #개발모드가 참일때 DEBUG=True일때만 
            url += '?_{}'.format(int(time())) #현재 url뒤에다가 쿼리스트링을위해서 ?를붙이고 _(의미없는 문자줘도 됨)키를 붙이고 = 붙이는데 그값{} 은 현재time스탬프로 시간처리
        return url #처리하고 리턴
# 실제 FreshStaticNode를 templatetags에 등록하기 위해서
# 별도로 do_static함수를 만들어서
#fresh_static이라는 이름으로 레지스터 등록
@register.tag('fresh_static')
def do_static(parser,token):
    return FreshStaticNode.handle_token(parser,token)