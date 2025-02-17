# spec file for package tde-avahi-tqt (version R14)
#
# Copyright (c) 2014-2025 Trinity Desktop Environment
#
# This file is licensed under the LGPL-2.0+ unless otherwise noted.
#
# Please submit bugfixes or comments via http://www.trinitydesktop.org/
#

# TDE variables
%define tde_epoch 2
%define tde_version 14.1.3

Name: tde-avahi-tqt
Version: %tde_version
Release: alt1
Summary: Avahi TQt integration library
Group: System/Libraries
License: LGPL-2.0+
Url: http://www.trinitydesktop.org/

Source0: %name.tar.gz

BuildRequires: tde-rpm-macros
BuildRequires: tde-cmake >= %tde_version
BuildRequires: gcc-c++
BuildRequires: pkg-config
BuildRequires: libtool
BuildRequires: libtqt4-devel >= %tde_version
BuildRequires: glib2-devel
BuildRequires: gettext-devel
BuildRequires: libX11-devel
BuildRequires: libdbus-devel
BuildRequires: libcap-devel
BuildRequires: libavahi-devel
BuildRequires: libexpat-devel
BuildRequires: libaudio-devel
BuildRequires: libXt-devel

%description
Avahi is a fully LGPL framework for Multicast DNS Service Discovery.
It allows programs to publish and discover services and hosts
running on a local network with no specific configuration.
This library contains the interface to integrate the Avahi libraries
into a TQt main loop application.

##########

%package -n libavahi-tqt1
Summary: Avahi TQt integration library
Group: System/Libraries
Provides: libavahi-tqt1 = %version-%release
Obsoletes: trinity-avahi-tqt < %version-%release

%description -n libavahi-tqt1
Avahi is a fully LGPL framework for Multicast DNS Service Discovery.
It allows programs to publish and discover services and hosts
running on a local network with no specific configuration.
This library contains the interface to integrate the Avahi libraries
into a TQt main loop application.

%post -n libavahi-tqt1 -p /sbin/ldconfig
%postun -n libavahi-tqt1 -p /sbin/ldconfig

%files -n libavahi-tqt1
%_libdir/libavahi-tqt.so.1*

##########

%package -n libavahi-tqt-devel
Summary: Avahi TQt integration library (Development Files)
Group: Development/Libraries/C and C++
Requires: libavahi-tqt1 = %version-%release
Requires: libtqt4-devel >= %tde_epoch:4.2.0
Obsoletes: tde-avahi-tqt-devel < %version-%release

%description -n libavahi-tqt-devel
Avahi is a fully LGPL framework for Multicast DNS Service Discovery.
It allows programs to publish and discover services and hosts
running on a local network with no specific configuration.
This library contains the interface to integrate the Avahi libraries
into a TQt main loop application.

%files -n libavahi-tqt-devel
%_includedir/avahi-tqt/
%_libdir/libavahi-tqt.*
%_pkgconfigdir/avahi-tqt.pc

##########

%prep
%setup -q -n %name

%build
unset QTDIR QTINC QTLIB

#if ! rpm -E %%cmake|grep -e 'cd build\|cd ${CMAKE_BUILD_DIR:-build}'; then
#  %__mkdir_p build
#  cd build
#fi


#mkdir /tmp/avahi-tqt.build
#cd /tmp/avahi-tqt.build
#cmake /usr/src/RPM/BUILD/tde-avahi-tqt [arguments...]

%cmake \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_C_FLAGS="%optflags" \
  -DCMAKE_CXX_FLAGS="%optflags" \
  -DCMAKE_SKIP_RPATH=ON \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=OFF \
  -DLIB_INSTALL_DIR=%_libdir

%cmake_insource
rm /usr/src/RPM/BUILD/tde-avahi-tqt/CMakeCache.txt
%cmake_build

%install
#rm -rf %buildroot
#make install -C build
%cmakeinstall_std

%files
%doc README AUTHORS COPYING

%changelog
* Sun Jan 26 2025 Petr Akhlamov <ahlamovpm@basealt.ru> 2:%version-%release
- Initial build for ALT Sisyphus
