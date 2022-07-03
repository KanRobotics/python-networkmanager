# SPDX-License-Identifier: LGPL-2.1-or-later
# This file was generated by tools/generate-settings-dataclasses.py,
# if possible, please make changes by also updating the script.
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from .base import NetworkManagerSettingsMixin


@dataclass
class WifiP2PSettings(NetworkManagerSettingsMixin):
    """Wi-Fi P2P Settings"""

    peer: Optional[str] = field(
        metadata={'dbus_name': 'peer', 'dbus_type': 's'},
        default=None,
    )
    """The P2P device that should be connected to. Currently, this is the only way
    to create or join a group."""
    wfd_ies: Optional[bytes] = field(
        metadata={'dbus_name': 'wfd-ies', 'dbus_type': 'ay'},
        default=None,
    )
    """The Wi-Fi Display (WFD) Information Elements (IEs) to set. Wi-Fi Display
    requires a protocol specific information element to be set in certain Wi-Fi
    frames. These can be specified here for the purpose of establishing a
    connection. This setting is only useful when implementing a Wi-Fi Display
    client."""
    wps_method: Optional[int] = field(
        metadata={'dbus_name': 'wps-method', 'dbus_type': 'u'},
        default=None,
    )
    """Flags indicating which mode of WPS is to be used. There's little point in
    changing the default setting as NetworkManager will automatically determine
    the best method to use."""
