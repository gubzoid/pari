from django.db.models import Q
from django.utils.timezone import now

from mezzanine.core.models import CONTENT_STATUS_PUBLISHED
from mezzanine.core.managers import DisplayableManager


class PublishedMixin(object):
    def get_query_set(self):
        return super(PublishedMixin, self).get_query_set().filter(
            Q(publish_date__lte=now()) | Q(publish_date__isnull=True),
            Q(expiry_date__gte=now()) | Q(expiry_date__isnull=True),
            Q(status=CONTENT_STATUS_PUBLISHED))


class ArticleManager(PublishedMixin, DisplayableManager):
    def get_query_set(self):
        return super(ArticleManager, self).get_query_set().filter(is_topic=False)


class TopicManager(PublishedMixin, DisplayableManager):
    def get_query_set(self):
        return super(TopicManager, self).get_query_set().filter(is_topic=True)
