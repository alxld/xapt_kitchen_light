"""Platform for light integration"""
from __future__ import annotations
import sys
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from . import DOMAIN

sys.path.append("custom_components/new_light")
from new_light import NewLight


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the light platform."""
    # We only want this platform to be set up via discovery.
    if discovery_info is None:
        return
    ent = XaptKitchenLight()
    add_entities([ent])


class XaptKitchenLight(NewLight):
    """Xapt Kitchen Light."""

    def __init__(self) -> None:
        """Initialize Xapt Kitchen Light."""
        super(XaptKitchenLight, self).__init__(
            "Kitchen Light", domain=DOMAIN, debug=False, debug_rl=False
        )

        self.entities["light.kitchen_group"] = None
        self.switch = "Kitchen Switch"
        # self.motion_sensors.append("Dining Room Motion Sensor")

        self.has_brightness_threshold = True
        self.brightness_threshold = 191
        self.motion_sensor_brightness = 128
