# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Media.caption'
        db.alter_column(u'instagram_api_media', 'caption', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):

        # Changing field 'Media.caption'
        db.alter_column(u'instagram_api_media', 'caption', self.gf('django.db.models.fields.CharField')(max_length=1000))

    models = {
        u'instagram_api.comment': {
            'Meta': {'object_name': 'Comment'},
            'created_time': ('django.db.models.fields.DateTimeField', [], {}),
            'fetched': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'media': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'to': u"orm['instagram_api.Media']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'media_comments'", 'to': u"orm['instagram_api.User']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'to': u"orm['instagram_api.User']"})
        },
        u'instagram_api.media': {
            'Meta': {'object_name': 'Media'},
            'actions_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'comments_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'created_time': ('django.db.models.fields.DateTimeField', [], {}),
            'fetched': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_low_resolution': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'image_standard_resolution': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'image_thumbnail': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'likes_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'likes_users': ('m2m_history.fields.ManyToManyHistoryField', [], {'related_name': "'likes_media'", 'symmetrical': 'False', 'to': u"orm['instagram_api.User']"}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '300'}),
            'remote_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'media_feed'", 'to': u"orm['instagram_api.User']"}),
            'video_low_bandwidth': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'video_low_resolution': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'video_standard_resolution': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'instagram_api.user': {
            'Meta': {'object_name': 'User'},
            'bio': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fetched': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'followers': ('m2m_history.fields.ManyToManyHistoryField', [], {'to': u"orm['instagram_api.User']", 'symmetrical': 'False'}),
            'followers_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'media_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'profile_picture': ('django.db.models.fields.URLField', [], {'max_length': '300'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['instagram_api']