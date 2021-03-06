# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.title_as'
        db.add_column(u'article_article', 'title_as',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.title_bn'
        db.add_column(u'article_article', 'title_bn',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.title_kn'
        db.add_column(u'article_article', 'title_kn',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.title_ml'
        db.add_column(u'article_article', 'title_ml',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.title_or'
        db.add_column(u'article_article', 'title_or',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.title_ta'
        db.add_column(u'article_article', 'title_ta',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.description_as'
        db.add_column(u'article_article', 'description_as',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.description_bn'
        db.add_column(u'article_article', 'description_bn',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.description_kn'
        db.add_column(u'article_article', 'description_kn',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.description_ml'
        db.add_column(u'article_article', 'description_ml',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.description_or'
        db.add_column(u'article_article', 'description_or',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.description_ta'
        db.add_column(u'article_article', 'description_ta',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.content_as'
        db.add_column(u'article_article', 'content_as',
                      self.gf('mezzanine.core.fields.RichTextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.content_bn'
        db.add_column(u'article_article', 'content_bn',
                      self.gf('mezzanine.core.fields.RichTextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.content_kn'
        db.add_column(u'article_article', 'content_kn',
                      self.gf('mezzanine.core.fields.RichTextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.content_ml'
        db.add_column(u'article_article', 'content_ml',
                      self.gf('mezzanine.core.fields.RichTextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.content_or'
        db.add_column(u'article_article', 'content_or',
                      self.gf('mezzanine.core.fields.RichTextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.content_ta'
        db.add_column(u'article_article', 'content_ta',
                      self.gf('mezzanine.core.fields.RichTextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.strap_as'
        db.add_column(u'article_article', 'strap_as',
                      self.gf('django.db.models.fields.CharField')(max_length=600, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.strap_bn'
        db.add_column(u'article_article', 'strap_bn',
                      self.gf('django.db.models.fields.CharField')(max_length=600, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.strap_kn'
        db.add_column(u'article_article', 'strap_kn',
                      self.gf('django.db.models.fields.CharField')(max_length=600, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.strap_ml'
        db.add_column(u'article_article', 'strap_ml',
                      self.gf('django.db.models.fields.CharField')(max_length=600, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.strap_or'
        db.add_column(u'article_article', 'strap_or',
                      self.gf('django.db.models.fields.CharField')(max_length=600, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.strap_ta'
        db.add_column(u'article_article', 'strap_ta',
                      self.gf('django.db.models.fields.CharField')(max_length=600, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.featured_image_caption_as'
        db.add_column(u'article_article', 'featured_image_caption_as',
                      self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.featured_image_caption_bn'
        db.add_column(u'article_article', 'featured_image_caption_bn',
                      self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.featured_image_caption_kn'
        db.add_column(u'article_article', 'featured_image_caption_kn',
                      self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.featured_image_caption_ml'
        db.add_column(u'article_article', 'featured_image_caption_ml',
                      self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.featured_image_caption_or'
        db.add_column(u'article_article', 'featured_image_caption_or',
                      self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.featured_image_caption_ta'
        db.add_column(u'article_article', 'featured_image_caption_ta',
                      self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Article.title_as'
        db.delete_column(u'article_article', 'title_as')

        # Deleting field 'Article.title_bn'
        db.delete_column(u'article_article', 'title_bn')

        # Deleting field 'Article.title_kn'
        db.delete_column(u'article_article', 'title_kn')

        # Deleting field 'Article.title_ml'
        db.delete_column(u'article_article', 'title_ml')

        # Deleting field 'Article.title_or'
        db.delete_column(u'article_article', 'title_or')

        # Deleting field 'Article.title_ta'
        db.delete_column(u'article_article', 'title_ta')

        # Deleting field 'Article.description_as'
        db.delete_column(u'article_article', 'description_as')

        # Deleting field 'Article.description_bn'
        db.delete_column(u'article_article', 'description_bn')

        # Deleting field 'Article.description_kn'
        db.delete_column(u'article_article', 'description_kn')

        # Deleting field 'Article.description_ml'
        db.delete_column(u'article_article', 'description_ml')

        # Deleting field 'Article.description_or'
        db.delete_column(u'article_article', 'description_or')

        # Deleting field 'Article.description_ta'
        db.delete_column(u'article_article', 'description_ta')

        # Deleting field 'Article.content_as'
        db.delete_column(u'article_article', 'content_as')

        # Deleting field 'Article.content_bn'
        db.delete_column(u'article_article', 'content_bn')

        # Deleting field 'Article.content_kn'
        db.delete_column(u'article_article', 'content_kn')

        # Deleting field 'Article.content_ml'
        db.delete_column(u'article_article', 'content_ml')

        # Deleting field 'Article.content_or'
        db.delete_column(u'article_article', 'content_or')

        # Deleting field 'Article.content_ta'
        db.delete_column(u'article_article', 'content_ta')

        # Deleting field 'Article.strap_as'
        db.delete_column(u'article_article', 'strap_as')

        # Deleting field 'Article.strap_bn'
        db.delete_column(u'article_article', 'strap_bn')

        # Deleting field 'Article.strap_kn'
        db.delete_column(u'article_article', 'strap_kn')

        # Deleting field 'Article.strap_ml'
        db.delete_column(u'article_article', 'strap_ml')

        # Deleting field 'Article.strap_or'
        db.delete_column(u'article_article', 'strap_or')

        # Deleting field 'Article.strap_ta'
        db.delete_column(u'article_article', 'strap_ta')

        # Deleting field 'Article.featured_image_caption_as'
        db.delete_column(u'article_article', 'featured_image_caption_as')

        # Deleting field 'Article.featured_image_caption_bn'
        db.delete_column(u'article_article', 'featured_image_caption_bn')

        # Deleting field 'Article.featured_image_caption_kn'
        db.delete_column(u'article_article', 'featured_image_caption_kn')

        # Deleting field 'Article.featured_image_caption_ml'
        db.delete_column(u'article_article', 'featured_image_caption_ml')

        # Deleting field 'Article.featured_image_caption_or'
        db.delete_column(u'article_article', 'featured_image_caption_or')

        # Deleting field 'Article.featured_image_caption_ta'
        db.delete_column(u'article_article', 'featured_image_caption_ta')


    models = {
        'article.article': {
            'Meta': {'ordering': "('-publish_date',)", 'object_name': 'Article'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'allow_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_featured_image': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'articles'", 'to': "orm['article.Author']"}),
            'capsule_video': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'carousel_order': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'category_list': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'articles'", 'symmetrical': 'False', 'to': "orm['article.Category']"}),
            u'comments_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'content_as': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'content_bn': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'content_en': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'content_hi': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'content_kn': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'content_ml': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'content_mr': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'content_or': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'content_ta': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'content_te': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date_of_publication': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_as': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_bn': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_hi': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_kn': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_ml': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_mr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_or': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_ta': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_te': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'featured_audio': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'featured_image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'featured_image_caption': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'featured_image_caption_as': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'featured_image_caption_bn': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'featured_image_caption_en': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'featured_image_caption_hi': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'featured_image_caption_kn': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'featured_image_caption_ml': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'featured_image_caption_mr': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'featured_image_caption_or': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'featured_image_caption_ta': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'featured_image_caption_te': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'featured_video': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_topic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['article.Location']", 'symmetrical': 'False', 'blank': 'True'}),
            'pin_to_home': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'related_posts': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related_posts_rel_+'", 'blank': 'True', 'to': "orm['article.Article']"}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'strap': ('django.db.models.fields.CharField', [], {'max_length': '600', 'null': 'True', 'blank': 'True'}),
            'strap_as': ('django.db.models.fields.CharField', [], {'max_length': '600', 'null': 'True', 'blank': 'True'}),
            'strap_bn': ('django.db.models.fields.CharField', [], {'max_length': '600', 'null': 'True', 'blank': 'True'}),
            'strap_en': ('django.db.models.fields.CharField', [], {'max_length': '600', 'null': 'True', 'blank': 'True'}),
            'strap_hi': ('django.db.models.fields.CharField', [], {'max_length': '600', 'null': 'True', 'blank': 'True'}),
            'strap_kn': ('django.db.models.fields.CharField', [], {'max_length': '600', 'null': 'True', 'blank': 'True'}),
            'strap_ml': ('django.db.models.fields.CharField', [], {'max_length': '600', 'null': 'True', 'blank': 'True'}),
            'strap_mr': ('django.db.models.fields.CharField', [], {'max_length': '600', 'null': 'True', 'blank': 'True'}),
            'strap_or': ('django.db.models.fields.CharField', [], {'max_length': '600', 'null': 'True', 'blank': 'True'}),
            'strap_ta': ('django.db.models.fields.CharField', [], {'max_length': '600', 'null': 'True', 'blank': 'True'}),
            'strap_te': ('django.db.models.fields.CharField', [], {'max_length': '600', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'title_as': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'title_bn': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'title_hi': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'title_kn': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'title_ml': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'title_mr': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'title_or': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'title_ta': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'title_te': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'types': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'articles'", 'symmetrical': 'False', 'to': "orm['article.Type']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'articles'", 'to': u"orm['auth.User']"})
        },
        'article.articlecarouselimage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'ArticleCarouselImage'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'article': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carousel_images'", 'to': "orm['article.Article']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('mezzanine.core.fields.FileField', [], {'max_length': '200'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        'article.author': {
            'Meta': {'object_name': 'Author'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        'article.category': {
            'Meta': {'ordering': "('_order', 'title')", 'object_name': 'Category'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        'article.location': {
            'Meta': {'object_name': 'Location'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'location': ('geoposition.fields.GeopositionField', [], {'max_length': '42'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        'article.type': {
            'Meta': {'object_name': 'Type'},
            'icon_class': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['article']