# This module is automatically generated by autogen.sh. DO NOT EDIT.

from . import _OnPrem


class _Certificates(_OnPrem):
    _type = "certificates"
    _icon_dir = "resources/onprem/certificates"


class CertManager(_Certificates):
    _icon = "cert-manager.png"


class LetsEncrypt(_Certificates):
    _icon = "lets-encrypt.png"


# Aliases