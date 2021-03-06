# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'events_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('start', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('host', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='events', null=True, to=orm['authtools.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('description_html', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=750)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('max_attendees', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('max_guests', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('cost', self.gf('django.db.models.fields.CharField')(default='', max_length=150, blank=True)),
            ('shortid', self.gf('django.db.models.fields.CharField')(default='', max_length=10, blank=True)),
        ))
        db.send_create_signal(u'events', ['Event'])

        # Adding model 'RSVP'
        db.create_table(u'events_rsvp', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rsvps', to=orm['events.Event'])),
            ('num_guests', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('response', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rsvps', to=orm['authtools.User'])),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'events', ['RSVP'])

        # Adding unique constraint on 'RSVP', fields ['event', 'user']
        db.create_unique(u'events_rsvp', ['event_id', 'user_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'RSVP', fields ['event', 'user']
        db.delete_unique(u'events_rsvp', ['event_id', 'user_id'])

        # Deleting model 'Event'
        db.delete_table(u'events_event')

        # Deleting model 'RSVP'
        db.delete_table(u'events_rsvp')


    models = {
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
        u'authtools.user': {
            'Meta': {'ordering': "[u'name', u'email']", 'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'events.event': {
            'Meta': {'ordering': "['start', 'end', 'title']", 'object_name': 'Event'},
            'cost': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'events'", 'null': 'True', 'to': u"orm['authtools.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '750'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'max_attendees': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'max_guests': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'shortid': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10', 'blank': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'events.rsvp': {
            'Meta': {'unique_together': "(('event', 'user'),)", 'object_name': 'RSVP'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rsvps'", 'to': u"orm['events.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'num_guests': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'response': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rsvps'", 'to': u"orm['authtools.User']"})
        }
    }

    complete_apps = ['events']