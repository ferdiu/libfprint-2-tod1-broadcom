%global debug_package       %{nil}
%define major_version       6.1.26
%define release_version     4
%define cs3dir              libfprint-2-tod1-broadcom
%define cspkus3dir          %{cs3dir}-cv3plus

Name:           libfprint-2-tod1-broadcom
Version:        %{major_version}
Release:        %{release_version}%{?dist}
Summary:        Broadcom fingerprint driver for libfprint
Requires:       openssl-libs, glibc, libfprint-tod
Provides:       libfprint-2-tod1-broadcom libfprint-2-tod1-broadcom-cv3plus
Group:          Hardware/Mobile
License:        NonFree
URL:            https://git.launchpad.net/~oem-solutions-engineers/libfprint-2-tod1-broadcom/+git/libfprint-2-tod1-broadcom
# Source0:        %{name}-%{major_version}.tar.gz

BuildRequires:  git, tar, gzip, systemd, pkgconfig(udev)
ExclusiveArch:  x86_64
Supplements:    modalias(usb:v0A5Cp5842d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0A5Cp5843d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0A5Cp5844d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0A5Cp5845d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0A5Cp5864d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0A5Cp5865d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0A5Cp5866d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0A5Cp5867d*dc*dsc*dp*ic*isc*ip*)

%description
This package provides the Broadcom fingerprint driver required
for several Dell Latitude laptops.

%prep
# Clone latest for CV3
git clone --depth 1 --branch ubuntu/latest %{URL} %{_builddir}/%{cs3dir}
# Clone latest for CV3plus
git clone --depth 1 --branch jammy %{URL} %{_builddir}/%{cspkus3dir}
# NOTE: at the time of writing, the CV3plus libraries where on jammy branch (commit f73dea98646c562f4660c900716ea4dae7b153a7)
# TODO: maybe add "source" at some point
# cd libfprint-2-tod1-broadcom
# git archive --format=tar --prefix=%{name}-%{major_version}/ HEAD | gzip > ../%{name}-%{major_version}.tar.gz

%build

%install
# CV3 (from dir libfprint-2-tod1-broadcom)
install -D -m 0644 %{cs3dir}/lib/udev/rules.d/60-libfprint-2-device-broadcom.rules %{buildroot}%{_udevrulesdir}/60-libfprint-2-device-broadcom.rules
install -D -m 0755 %{cs3dir}/usr/lib/x86_64-linux-gnu/libfprint-2/tod-1/libfprint-2-tod-1-broadcom.so %{buildroot}%{_libdir}/libfprint-2/tod-1/libfprint-2-tod-1-broadcom.so
install -D -m 0644 %{cs3dir}/var/lib/fprint/fw/bcm_cv_clearscd.bin %{buildroot}%{_sharedstatedir}/fprint/fw/bcm_cv_clearscd.bin
install -D -m 0755 %{cs3dir}/var/lib/fprint/fw/key.pem %{buildroot}%{_sharedstatedir}/fprint/fw/key.pem
install -D -m 0644 %{cs3dir}/var/lib/fprint/fw/bcmCitadel_1.otp %{buildroot}%{_sharedstatedir}/fprint/fw/bcmCitadel_1.otp
install -D -m 0644 %{cs3dir}/var/lib/fprint/fw/bcmCitadel_7.otp %{buildroot}%{_sharedstatedir}/fprint/fw/bcmCitadel_7.otp
install -D -m 0644 %{cs3dir}/var/lib/fprint/fw/bcmDeviceFirmwareCitadel_1.bin %{buildroot}%{_sharedstatedir}/fprint/fw/bcmDeviceFirmwareCitadel_1.bin
install -D -m 0644 %{cs3dir}/var/lib/fprint/fw/bcmDeviceFirmwareCitadel_7.bin %{buildroot}%{_sharedstatedir}/fprint/fw/bcmDeviceFirmwareCitadel_7.bin
install -D -m 0644 %{cs3dir}/var/lib/fprint/fw/bcm_cv_current_version.txt %{buildroot}%{_sharedstatedir}/fprint/fw/bcm_cv_current_version.txt
install -D -m 0644 %{cs3dir}/var/lib/fprint/fw/bcmsbiCitadelA0_1.otp %{buildroot}%{_sharedstatedir}/fprint/fw/bcmsbiCitadelA0_1.otp
install -D -m 0644 %{cs3dir}/var/lib/fprint/fw/bcmsbiCitadelA0_7.otp %{buildroot}%{_sharedstatedir}/fprint/fw/bcmsbiCitadelA0_7.otp
# CV3plus  (from dir libfprint-2-tod1-broadcom-cv3plus)
install -D -m 0644 %{cspkus3dir}/lib/udev/rules.d/60-libfprint-2-device-broadcom-cv3plus.rules %{buildroot}%{_udevrulesdir}/60-libfprint-2-device-broadcom-cv3plus.rules
install -D -m 0755 %{cspkus3dir}/usr/lib/x86_64-linux-gnu/libfprint-2/tod-1/libfprint-2-tod-1-broadcom-cv3plus.so %{buildroot}%{_libdir}/libfprint-2/tod-1/libfprint-2-tod-1-broadcom-cv3plus.so
install -D -m 0644 %{cspkus3dir}/var/lib/fprint/fw/cv3/bcmCitadel_1.otp %{buildroot}%{_sharedstatedir}/fprint/fw/cv3/bcmCitadel_1.otp
install -D -m 0644 %{cspkus3dir}/var/lib/fprint/fw/cv3/bcmCitadel_7.otp %{buildroot}%{_sharedstatedir}/fprint/fw/cv3/bcmCitadel_7.otp
install -D -m 0644 %{cspkus3dir}/var/lib/fprint/fw/cv3/bcmDeviceFirmwareCitadel_1.bin %{buildroot}%{_sharedstatedir}/fprint/fw/cv3/bcmDeviceFirmwareCitadel_1.bin
install -D -m 0644 %{cspkus3dir}/var/lib/fprint/fw/cv3/bcmDeviceFirmwareCitadel_7.bin %{buildroot}%{_sharedstatedir}/fprint/fw/cv3/bcmDeviceFirmwareCitadel_7.bin
install -D -m 0644 %{cspkus3dir}/var/lib/fprint/fw/cv3/bcm_cv_clearscd.bin %{buildroot}%{_sharedstatedir}/fprint/fw/cv3/bcm_cv_clearscd.bin
install -D -m 0644 %{cspkus3dir}/var/lib/fprint/fw/cv3/bcm_cv_current_version.txt %{buildroot}%{_sharedstatedir}/fprint/fw/cv3/bcm_cv_current_version.txt
install -D -m 0644 %{cspkus3dir}/var/lib/fprint/fw/cv3/bcmsbiCitadelA0_1.otp %{buildroot}%{_sharedstatedir}/fprint/fw/cv3/bcmsbiCitadelA0_1.otp
install -D -m 0644 %{cspkus3dir}/var/lib/fprint/fw/cv3/bcmsbiCitadelA0_7.otp %{buildroot}%{_sharedstatedir}/fprint/fw/cv3/bcmsbiCitadelA0_7.otp
install -D -m 0755 %{cspkus3dir}/var/lib/fprint/fw/cv3/key.pem %{buildroot}%{_sharedstatedir}/fprint/fw/cv3/key.pem
install -D -m 0644 %{cspkus3dir}/var/lib/fprint/fw/cv3plus/bcmCitadel_1.otp %{buildroot}%{_sharedstatedir}/fprint/.broadcomCv3plusFW/bcmCitadel_1.otp
install -D -m 0644 %{cspkus3dir}/var/lib/fprint/fw/cv3plus/bcmCitadel_7.otp %{buildroot}%{_sharedstatedir}/fprint/.broadcomCv3plusFW/bcmCitadel_7.otp
install -D -m 0644 %{cspkus3dir}/var/lib/fprint/fw/cv3plus/bcmDeviceFirmwareCitadel_1.bin %{buildroot}%{_sharedstatedir}/fprint/.broadcomCv3plusFW/bcmDeviceFirmwareCitadel_1.bin
install -D -m 0644 %{cspkus3dir}/var/lib/fprint/fw/cv3plus/bcmDeviceFirmwareCitadel_7.bin %{buildroot}%{_sharedstatedir}/fprint/.broadcomCv3plusFW/bcmDeviceFirmwareCitadel_7.bin
install -D -m 0644 %{cspkus3dir}/var/lib/fprint/fw/cv3plus/bcm_cv_clearscd.bin %{buildroot}%{_sharedstatedir}/fprint/.broadcomCv3plusFW/bcm_cv_clearscd.bin
install -D -m 0644 %{cspkus3dir}/var/lib/fprint/fw/cv3plus/bcm_cv_current_version.txt %{buildroot}%{_sharedstatedir}/fprint/.broadcomCv3plusFW/bcm_cv_current_version.txt
install -D -m 0644 %{cspkus3dir}/var/lib/fprint/fw/cv3plus/bcmsbiCitadelB0_1.otp %{buildroot}%{_sharedstatedir}/fprint/.broadcomCv3plusFW/bcmsbiCitadelB0_1.otp
install -D -m 0644 %{cspkus3dir}/var/lib/fprint/fw/cv3plus/bcmsbiCitadelB0_7.otp %{buildroot}%{_sharedstatedir}/fprint/.broadcomCv3plusFW/bcmsbiCitadelB0_7.otp
install -D -m 0755 %{cspkus3dir}/var/lib/fprint/fw/cv3plus/key.pem %{buildroot}%{_sharedstatedir}/fprint/.broadcomCv3plusFW/key.pem


%files
# CV3
%attr(644, -, -) %license libfprint-2-tod1-broadcom/LICENCE.broadcom
%attr(644, -, -) %{_udevrulesdir}/60-libfprint-2-device-broadcom.rules
%attr(755, -, -) %{_libdir}/libfprint-2/tod-1/libfprint-2-tod-1-broadcom.so
%attr(644, -, -) %{_sharedstatedir}/fprint/fw/bcm_cv_clearscd.bin
%attr(755, -, -) %{_sharedstatedir}/fprint/fw/key.pem
%attr(644, -, -) %{_sharedstatedir}/fprint/fw/bcmCitadel_1.otp
%attr(644, -, -) %{_sharedstatedir}/fprint/fw/bcmCitadel_7.otp
%attr(644, -, -) %{_sharedstatedir}/fprint/fw/bcmDeviceFirmwareCitadel_1.bin
%attr(644, -, -) %{_sharedstatedir}/fprint/fw/bcmDeviceFirmwareCitadel_7.bin
%attr(644, -, -) %{_sharedstatedir}/fprint/fw/bcm_cv_current_version.txt
%attr(644, -, -) %{_sharedstatedir}/fprint/fw/bcmsbiCitadelA0_1.otp
%attr(644, -, -) %{_sharedstatedir}/fprint/fw/bcmsbiCitadelA0_7.otp
# CV3plus
%attr(644, -, -) %{_udevrulesdir}/60-libfprint-2-device-broadcom-cv3plus.rules
%attr(755, -, -) %{_libdir}/libfprint-2/tod-1/libfprint-2-tod-1-broadcom-cv3plus.so
%attr(644, -, -) %{_sharedstatedir}/fprint/fw/cv3/bcmCitadel_1.otp
%attr(644, -, -) %{_sharedstatedir}/fprint/fw/cv3/bcmCitadel_7.otp
%attr(644, -, -) %{_sharedstatedir}/fprint/fw/cv3/bcmDeviceFirmwareCitadel_1.bin
%attr(644, -, -) %{_sharedstatedir}/fprint/fw/cv3/bcmDeviceFirmwareCitadel_7.bin
%attr(644, -, -) %{_sharedstatedir}/fprint/fw/cv3/bcm_cv_clearscd.bin
%attr(644, -, -) %{_sharedstatedir}/fprint/fw/cv3/bcm_cv_current_version.txt
%attr(644, -, -) %{_sharedstatedir}/fprint/fw/cv3/bcmsbiCitadelA0_1.otp
%attr(644, -, -) %{_sharedstatedir}/fprint/fw/cv3/bcmsbiCitadelA0_7.otp
%attr(755, -, -) %{_sharedstatedir}/fprint/fw/cv3/key.pem
%attr(644, -, -) %{_sharedstatedir}/fprint/.broadcomCv3plusFW/bcmCitadel_1.otp
%attr(644, -, -) %{_sharedstatedir}/fprint/.broadcomCv3plusFW/bcmCitadel_7.otp
%attr(644, -, -) %{_sharedstatedir}/fprint/.broadcomCv3plusFW/bcmDeviceFirmwareCitadel_1.bin
%attr(644, -, -) %{_sharedstatedir}/fprint/.broadcomCv3plusFW/bcmDeviceFirmwareCitadel_7.bin
%attr(644, -, -) %{_sharedstatedir}/fprint/.broadcomCv3plusFW/bcm_cv_clearscd.bin
%attr(644, -, -) %{_sharedstatedir}/fprint/.broadcomCv3plusFW/bcm_cv_current_version.txt
%attr(644, -, -) %{_sharedstatedir}/fprint/.broadcomCv3plusFW/bcmsbiCitadelB0_1.otp
%attr(644, -, -) %{_sharedstatedir}/fprint/.broadcomCv3plusFW/bcmsbiCitadelB0_7.otp
%attr(755, -, -) %{_sharedstatedir}/fprint/.broadcomCv3plusFW/key.pem

%changelog
* Fri Apr 18 2025 Federico Manzella <ferdiu.manzella@gmail.com> 6.1.26-4
- Add missing CV3plus libraries

* Wed Feb 5 2025 Federico Manzella <ferdiu.manzella@gmail.com> 6.1.26-2
- Change path of the installed libraries

* Wed Feb 5 2025 Federico Manzella <ferdiu.manzella@gmail.com> 6.1.26-1
- First release
%autochangelog
