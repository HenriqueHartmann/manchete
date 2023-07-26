from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, Permission

from app_news.models import News

def create_groups():
    writer_group = Group(name='writer')
    editor_group = Group(name='editor')

    writer_group.save()
    editor_group.save()

    news_content_type = ContentType.objects.get_for_model(News)

    add_permission = Permission.objects.filter(content_type=news_content_type, codename="add_news").first()
    change_permission = Permission.objects.filter(content_type=news_content_type, codename="change_news").first()
    delete_permission = Permission.objects.filter(content_type=news_content_type, codename="delete_news").first()

    writer_group.permissions.add(add_permission)
    editor_group.permissions.add(change_permission, delete_permission)
