# -*- coding: utf8 -*-
import datetime
from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext_noop
from django.contrib.auth.models import User

if "notification" in settings.INSTALLED_APPS:
    from notification import models as notification
else:
    notification = None

from django_messages.models import Message
from django_messages.fields import CommaSeparatedUserField
from ajax_select.fields import AutoCompleteSelectMultipleField, AutoCompleteSelectField
from ajax_select import make_ajax_field

class ComposeForm(forms.ModelForm):
    recipient = AutoCompleteSelectMultipleField('destinatarios', required=False, help_text=u'Por favor, ingrese al menos 4 caracteres para autocompletar. Puede agregar múltiples contactos.', label='Destinatarios')
    con_copia = AutoCompleteSelectMultipleField('destinatarios', required=False, help_text=u'Por favor, ingrese al menos 4 caracteres para autocompletar. Puede agregar múltiples contactos.')
    class Meta:
        model = Message
        exclude = ('sender','parent_msg','sent_at','read_at','replied_at','sender_deleted_at','recipient_deleted_at','status','tipo','leido_por')
    '''

    def save(self, sender, parent_msg=None):
        recipients = self.cleaned_data['recipient']
        subject = self.cleaned_data['subject']
        body = self.cleaned_data['body']
        con_copia = self.cleaned_data['con_copia']
        message_list = []

        for r in recipients:
            msg = Message(
                sender = sender,
                recipient = r,
                subject = subject,
                body = body,
            )

            if parent_msg is not None:
                msg.parent_msg = parent_msg
                parent_msg.replied_at = datetime.datetime.now()
                parent_msg.save()
            #msg.save()
            message_list.append(msg)
        return message_list
    '''

'''
class Compos_eForm(forms.Form):
    """
    A simple default form for private messages.
    """
    #recipient = CommaSeparatedUserField(label=_(u"Recipient"))
    recipient = AutoCompleteSelectMultipleField('destinatarios', required=True)
    subject = forms.CharField(label=_(u"Subject"), max_length=120)
    body = forms.CharField(label=_(u"Body"),
        widget=forms.Textarea(attrs={'rows': '12', 'cols':'55'}))
    
        
    def __init__(self, *args, **kwargs):
        recipient_filter = kwargs.pop('recipient_filter', None)
        super(ComposeForm, self).__init__(*args, **kwargs)
        if recipient_filter is not None:
            self.fields['recipient']._recipient_filter = recipient_filter
    
                
    def save(self, sender, parent_msg=None):
        recipients = self.cleaned_data['recipient']
        subject = self.cleaned_data['subject']
        body = self.cleaned_data['body']
        message_list = []
        for r in recipients:
            msg = Message(
                sender = sender,
                recipient = r,
                subject = subject,
                body = body,
            )
            if parent_msg is not None:
                msg.parent_msg = parent_msg
                parent_msg.replied_at = datetime.datetime.now()
                parent_msg.save()
            msg.save()
            message_list.append(msg)
            if notification:
                if parent_msg is not None:
                    notification.send([sender], "messages_replied", {'message': msg,})
                    notification.send([r], "messages_reply_received", {'message': msg,})
                else:
                    notification.send([sender], "messages_sent", {'message': msg,})
                    notification.send([r], "messages_received", {'message': msg,})
        return message_list
'''
