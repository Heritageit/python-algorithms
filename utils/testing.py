#!/usr/bin/env python
# -*- coding: utf8 -*-
#                        _             _    _                     _    _  _     
#  ___ ___  _ __   ___  | |_  ___  ___| |_ (_) _ _   __ _   _  _ | |_ (_)| | ___
# (_-</ _ \| '  \ / -_) |  _|/ -_)(_-<|  _|| || ' \ / _` | | || ||  _|| || |(_-<
# /__/\___/|_|_|_|\___|  \__|\___|/__/ \__||_||_||_|\__, |  \_,_| \__||_||_|/__/
#                                                   |___/
# 2012 - Federico Mendez

def saveit(instance, name=None):
    if name is None:
        instance.find_element_by_class_name('btn').click()
    else:
        #print "input[value='{0}']".format(name)
        instance.find_element_by_css_selector(
                "input[name='{0}']".format(name)).click()

def select_multiple_options(*args, **kwargs):
    """ selects an option from a multiple select widget.
    Depends on selenium webdriver object (self.browser)
    """
    instance = kwargs['instance']
    select = instance.find_element_by_id(kwargs['id'])
    for option in select.find_elements_by_tag_name('option'):
        if option.text == kwargs['lookup']:
            option.click()
            if kwargs['id'].endswith('_from'):
                # if it ends with '_from' it means we are in 
                # a FilteredSelectMultiple, so we need to click
                # the Choose button too
                instance.find_element_by_class_name("selector-add").click()


def can_jump(instance, start, end):
    '''Returns False if it is redirected to 403 page, 
    else it returns the current url'''
    instance.get(start + end)
    if '403-error' in instance.current_url:
        return False
    else:
        return instance.current_url


def print_response(resp):
    print '#################################\n'
    print resp.content
    print '#################################\n'

