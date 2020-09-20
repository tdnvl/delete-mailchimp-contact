# Delete MailChimp contact
This tiny script lets you delete contacts through the MailChimp API (v. 3.0.1). Admiteddly unscubscribed ones.  
You should save some 💰 on your MailChimp plan.

## Installation

This section supposes that you have Python 3+ installed on your machine (see [Downloads](https://www.python.org/downloads/) if it isn't).

From your terminal:
1. Clone this repo: `git clone https://github.com/tdnvl/delete-mailchimp-contact.git`
2. `cd` into the cloned repo directory
3. `python3 -m venv venv` to make the virtual environment
4. `source venv/bin/activate` to activate the virtual environment
5. `pip install mailchimp3` to install [Python MailChimp](https://github.com/VingtCinq/python-mailchimp) the required package

You will then need to obtain:
- your [Audience ID](https://mailchimp.com/help/find-audience-id/)
- your [API key](https://mailchimp.com/help/about-api-keys/#Find_or_generate_your_API_key)
- your username (it should be listed under on your profile page)

Once you have these items, edit the script:
`nano delete.py`
and replace the placeholders with your own values.

> ⚠ Do not push the script to a public repo with these values added. This would make your list vulnerable to attacks. You might also incur some charges if the attacker decides to _add_ contacts to your audience.

Run the script and follow the instruction. You'll be asked for the contact's email address.  
`python3 delete.py`

This script will delete one contact at a time, but you could delete contacts recursively by adding them to a segment and looping through the segment members. See [MailChimp's API documentation](https://mailchimp.com/developer/api/marketing/list-segment-members/) on `Segment Members`.

## Support
If you are having issues, please open one here, or submit a pull request.

## License
The script is licensed under the MIT License.
