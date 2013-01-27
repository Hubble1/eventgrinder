from django import forms
from django.forms.util import ErrorList
from django.template.defaultfilters import slugify
from eventsite import get_site
from eventsite.models import SitesMailchimp

from tz_helper import common_timezones_set

timezones=sorted(zip(common_timezones_set,common_timezones_set))

class SiteCreateForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    timezone=forms.ChoiceField(choices=timezones)


    
class SiteDetailsForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    timezone=forms.ChoiceField(choices=timezones)
    twitter=forms.CharField(max_length=255, required=False)
    offline=forms.BooleanField(required=False)

    
    
    def clean_hostnames(self):
        cd=self.cleaned_data
        return [h.strip().lower() for h in cd['hostnames'].split(',')]



class LogoUploadForm(forms.Form):
    upload=forms.FileField(required=True)
    
class MailChimpApiKey(forms.Form):
    mailchimp_api_key = forms.CharField(max_length=255, required=True)
    
    def save(self):
        site=get_site()
        mc=SitesMailchimp(parent=site, apikey=self.cleaned_data['mailchimp_api_key'])
        mc.put()
        return mc
        
        


        
        