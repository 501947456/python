使用自定义模板标签

最新文章模板标签

blog/templatetags/blog_tags.py

from django import template
from ..models import Post

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]
    
