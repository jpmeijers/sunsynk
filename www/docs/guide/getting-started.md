# Getting Started

## Installation

1. Add this repository to your HA Supervisor

   [![Open your Home Assistant instance and show the add add-on repository dialog with a specific repository URL pre-filled.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fkellerza%2Fsunsynk)

   `https://github.com/kellerza/sunsynk`

2. Install the Sunsynk Add-On **(multi)** from the **Add-On Store** and configure through the UI

   ![Install Sunsynk Addon](https://github.com/kellerza/sunsynk/raw/main/images/addon-install.png)


## Available addons

### mbusd gateway

An mbusd TCP to RTU gateway. See more [here](./mbusd)

### Sunsynk Inverter Add-on (multi)

The recommended version of the addon, supporting multiple sensor definitions and ready for multiple inverters

::: warning
Multiple inverters can be specified in the config, but not working yet.

See [this](https://github.com/kellerza/sunsynk/issues/39) issue if you want to contribute.
:::

### Sunsynk Inverter Add-on (dev)

The developer version of the addon - not being updated

Full support for writable sensors

::: danger
This is an older version of the addon and does not suport all the features & sensors mentioned on this website
:::


### Sunsynk Inverter Add-on

The original addon - not being updated

Limited support for writable sensors

::: danger
This is an older version of the addon and does not suport all the features & sensors mentioned on this website
:::
