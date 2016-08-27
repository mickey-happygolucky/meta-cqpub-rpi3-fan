This README file contains information on the contents of the
cqpub-rpi3-fan layer.

Please see the corresponding sections below for details.

Summary
=======

This layer support to create firmware of face detection fan on raspberrypi3 which is example in the magazine "Interface(CQ Publishing) 11,2016"(temporary).


Dependencies
============

This layer depends on:

  URI: git://git.openembedded.org/meta-openembedded
  layers: openembedded-layer
  branch: krogoth

  URI: git://git.yoctoproject.org/meta-raspberrypi
  branch: master

  URI: https://github.com/mickey-happygolucky/meta-rpi3-bt-support.git
  branch: master

  URI: https://github.com/mickey-happygolucky/meta-hdmi5inch-rpi.git
  branch: master

Patches
=======

Please submit any patches against the cqpub-rpi3-fan layer to 
the maintainer:

Maintainer: Yusuke MITSUKI <mickey.happygolucky@gmail.com>



Adding the cqpub-rpi3-fan layer to your build
=================================================

In order to use this layer, you need to make the build system aware of
it.

Assuming the cqpub-rpi3-fan layer exists at the top-level of your
yocto build tree, you can add it to the build system by adding the
location of the cqpub-rpi3-fan layer to bblayers.conf, along with any
other layers needed. e.g.:

  BBLAYERS ?= " \
    /path/to/yocto/meta \
    /path/to/yocto/meta-poky \
    /path/to/yocto/meta-yocto-bsp \
	/path/to/yocto/meta-openembedded/meta-oe \
	/path/to/yocto/meta-raspberrypi \
	/path/to/yocto/meta-rpi3-bt-support \
	/path/to/yocto/meta-hdmi5inch-rpi \
    /path/to/yocto/meta-cqpub-rpi3-fan \
    "
