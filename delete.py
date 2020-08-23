# This script relies on the mailchimp3 python package. See: https://github.com/VingtCinq/python-mailchimp
# You will need an API key. See: https://mailchimp.com/help/about-api-keys/#Find_or_generate_your_API_key
# Access your MailChimp profile to find your username 
# You will need your audience ID. See: https://mailchimp.com/help/find-audience-id/
# This tiny script was written by Thomas Deneuville
# https://thomasdeneuville.com | @tdnvl

import hashlib
from mailchimp3 import MailChimp

client = MailChimp(mc_api='YOUR-API-KEY', mc_user='YOUR-MAILCHIMP-USER-NAME')

loop = True

while loop:

    id = input("what's the contact's email address?\n")
    hash = hashlib.md5(id.encode('utf-8')).hexdigest()
    client.lists.members.delete_permanent(list_id='YOUR-AUDIENCE-ID-HERE', subscriber_hash=hash)
    print ("The contact was deleted.\n")
