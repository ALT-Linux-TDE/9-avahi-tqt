#
# spec file for package avahi-tqt (version R14)
#
# Copyright (c) 2014 Trinity Desktop Environment
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http://www.trinitydesktop.org/
#

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.3
%endif

%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?pclinuxos}
%define libavahi %{_lib}avahi
%else
%define libavahi libavahi
%endif

Name: tde-avahi-tqt
#Epoch: %tde_epoch
Version: 14.1.3
Release: alt1
Summary: Avahi TQt integration library
Group: System/Libraries
Url: http://www.trinitydesktop.org/

License: LGPL-2.0+

#Vendor:		Trinity Project
#Packager:	Francois Andriot <francois.andriot@free.fr>

Source0: tde-avahi-tqt.tar.gz

BuildRequires: libtqt4-devel >= %tde_version

BuildRequires: tde-rpm-macros
BuildRequires: tde-cmake >= %tde_version
BuildRequires: gcc-c++
BuildRequires: pkg-config
BuildRequires: libtool

# GLIB2 support
BuildRequires: glib2-devel

# GETTEXT support
BuildRequires: gettext-devel

# Xi support
BuildRequires: libX11-devel

# DBUS support
BuildRequires: libdbus-devel

# PCAP support
BuildRequires: libcap-devel

# AVAHI support
BuildRequires: libavahi-devel

# EXPAT support
BuildRequires: libexpat-devel

# NAS support
BuildRequires: libaudio-devel

# XT support
BuildRequires: libXt-devel

%description
Avahi is a fully LGPL framework for Multicast DNS Service Discovery.
It allows programs to publish and discover services and hosts
running on a local network with no specific configuration. For
example you can plug into a network and instantly find printers to
print to, files to look at and people to talk to.
 .
This library contains the interface to integrate the Avahi libraries
into a TQt main loop application.

##########

%package -n %libavahi-tqt1
Summary: Avahi TQt integration library
Group: System/Libraries
Provides: libavahi-tqt1 = %{?epoch:%epoch:}%version-%release

Obsoletes: trinity-avahi-tqt < %{?epoch:%epoch:}%version-%release
Provides: trinity-avahi-tqt = %{?epoch:%epoch:}%version-%release

%description -n %libavahi-tqt1
Avahi is a fully LGPL framework for Multicast DNS Service Discovery.
It allows programs to publish and discover services and hosts
running on a local network with no specific configuration. For
example you can plug into a network and instantly find printers to
print to, files to look at and people to talk to.
 .
This library contains the interface to integrate the Avahi libraries
into a TQt main loop application.

%post -n %libavahi-tqt1
/sbin/ldconfig || :

%postun -n %libavahi-tqt1
/sbin/ldconfig || :

%files -n %libavahi-tqt1
%_libdir/libavahi-tqt.so.1
%_libdir/libavahi-tqt.so.1.0.0

##########

%package -n %libavahi-tqt-devel
Summary: Avahi TQt integration library (Development Files)
Group: Development/Libraries/C and C++
Provides: libavahi-tqt-devel = %{?epoch:%epoch:}%version-%release

Requires: %libavahi-tqt1 = %{?epoch:%epoch:}%version-%release
Requires: libtqt4-devel >= %tde_epoch:4.2.0
%{?avahi_devel:Requires: %avahi_devel}

Obsoletes: trinity-avahi-tqt-devel < %{?epoch:%epoch:}%version-%release
Provides: trinity-avahi-tqt-devel = %{?epoch:%epoch:}%version-%release

%description -n %libavahi-tqt-devel
Avahi is a fully LGPL framework for Multicast DNS Service Discovery.
It allows programs to publish and discover services and hosts
running on a local network with no specific configuration. For
example you can plug into a network and instantly find printers to
print to, files to look at and people to talk to.
 .
This library contains the interface to integrate the Avahi libraries
into a TQt main loop application.

%post -n %libavahi-tqt-devel
/sbin/ldconfig || :

%postun -n %libavahi-tqt-devel
/sbin/ldconfig || :

%files -n %libavahi-tqt-devel
%_includedir/avahi-tqt/
%_libdir/libavahi-tqt.a
%_libdir/libavahi-tqt.so
%_libdir/libavahi-tqt.la
%_pkgconfigdir/avahi-tqt.pc

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0

%endif

##########

%prep
#%setup -n %name-%tde_version%{?preversion:~%preversion}
%setup -q -n tde-avahi-tqt
cd tde-avahi-tqt

%build
unset QTDIR QTINC QTLIB

#было:
#if ! rpm -E %%cmake|grep -e 'cd build\|cd ${CMAKE_BUILD_DIR:-build}'; then
#  mkdir -p build
#  cd build
#fi
#стало:

%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_SKIP_RPATH=ON \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DLIB_INSTALL_DIR="%_libdir" \
  ..

%make_build || %__make

%install
rm -rf %{?buildroot}
%make_install install DESTDIR="%{?buildroot}" -C build


rm -rf %{?buildroot}

%changelog
* Sun Jan 26 2025 Petr Akhlamov <ahlamovpm@basealt.ru> 2:0.6.30-14.1.2_1
- initial build for ALT Sisyphus

