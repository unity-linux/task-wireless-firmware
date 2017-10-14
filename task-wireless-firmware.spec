Name:		task-wireless-firmware
Version:	0.1.0
Release:	2%{?dist}
Summary:	Metapackage to install all wireless firmware
Group:		Graphical desktop/Other
License:	GPL
URL:		http://unity-linux.org/

Requires:       ipw2100-firmware
Requires:       ipw2200-firmware
Requires:	iwlwifi-agn-ucode
Requires:       iwlwifi-3945-ucode
Requires:       iwlwifi-4965-ucode
Requires:       atmel-firmware
Requires:       b43-openfwwf

BuildArch:	noarch

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for installing wireless firmware.

%files
