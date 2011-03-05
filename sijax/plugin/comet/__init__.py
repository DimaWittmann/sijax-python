# -*- coding: utf-8 -*-

"""
    sijax.plugin.comet
    ~~~~~~~~~~~~~~~~~~

    Provides helpers to register Comet functions.

    :copyright: (c) 2011 by Slavi Pantaleev.
    :license: BSD, see LICENSE.txt for more details.
"""


from .CometResponse import CometResponse


def _prepare_options(sijax_instance, options):
    param_response_class = sijax_instance.__class__.PARAM_RESPONSE_CLASS
    if param_response_class not in options:
        options[param_response_class] = CometResponse

    return options


def register_comet_callback(sijax_instance, public_name, callback, **options):
    """Helps you easily register Comet functions with Sijax.

    This is the analogue of
    :meth:`sijax.Sijax.Sijax.register_callback`,
    but makes the registered function support Comet functionality.

    Comet functions need to be called from the browser using::

        sjxComet.request('function_name');

    instead of the regular::

        Sijax.request('function_name');
    
    :param sijax_instance: the :class:`sijax.Sijax.Sijax` instance to register callbacks with
    :param public_name: the name of the function that the client will use to call it
    :param callback: the actual function that would get called to process the request
    :param options: options to pass to :meth:`sijax.Sijax.Sijax.register_callback`
    """
    options = _prepare_options(sijax_instance, options)
    sijax_instance.register_callback(public_name, callback, **options)


def register_comet_object(sijax_instance, obj, **options):
    """Helps you easily register all "public" callable attributes of an object.

    This is the analogue of
    :meth:`sijax.Sijax.Sijax.register_object`,
    but makes the registered functions support Comet functionality.

    :param sijax_instance: the :class:`sijax.Sijax.Sijax` instance to register callbacks with
    :param obj: the object whose methods to register with Sijax
    :param options: options to pass to :meth:`sijax.Sijax.Sijax.register_callback`
    """
    options = _prepare_options(sijax_instance, options)
    sijax_instance.register_object(obj, **options)
        
