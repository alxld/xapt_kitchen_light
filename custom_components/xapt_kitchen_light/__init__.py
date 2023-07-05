"""The new xapt_kitchen_light integration."""
from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

DOMAIN = "xapt_kitchen_light"


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Your controller/hub specific code."""
    hass.helpers.discovery.load_platform("light", DOMAIN, {}, config)

    return True
