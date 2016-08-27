SUMMARY = "Face Detection script"
DESCRIPTION = "Firmware of face detection fan with raspberrypi3"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COREBASE}/meta/COPYING.MIT;md5=3da9cfbcb788c80a0384361b4de20420"

SRC_URI = "file://face_detection.py"

S = "${WORKDIR}"

do_install () {
	install -d ${D}/home/root
	install -m 0644 ${WORKDIR}/face_detection.py ${D}/home/root
}

FILES_${PN} = "/home/root/*"

