# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 19:33:37 2019

@author: ben94

This function is used only to determine the coinbase unique id
for your bank account.

From the Create Function screen in Google Cloud Console - Cloud Functions
Name:  get_cbp_funding_sources
Memory allocated: 128 MB
Trigger: HTTP
Allow unauthenticated invocations: check
Source Code: Inline editor
Runtime: Python 3.xx
Function to execute: print_cbpro_funding_accounts
"""

import cbpro

""" paste your coinbase api info into into the variables below within
the quote marks. """
cbpro_apikey = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
cbpro_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
cbpro_passphrase = 'your_passphrase'
""" To run your script against the sandbox (not production), set this to True
Get API keys from https://public.sandbox.pro.coinbase.com/
"""
cbpro_sandbox = False

def print_cbpro_funding_accounts(requests):

    cbpro_apiurl = "https://api-public.sandbox.pro.coinbase.com" if cbpro_sandbox else "https://api.pro.coinbase.com/"
    cbpro_api = cbpro.AuthenticatedClient(cbpro_apikey,
                                          cbpro_secret,
                                          cbpro_passphrase,
                                          api_url=cbpro_apiurl)

    for funding_account in cbpro_api.get_payment_methods():
        print('the id number for {} is: {}'.format(funding_account['name'],
              funding_account['id']))
