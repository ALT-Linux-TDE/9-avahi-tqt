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

BuildRequires(pre): cmake
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

Patch0: libraries_path.patch
Patch1: library_types.patch

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
%_libdir/libavahi-tqt.so.1
%_libdir/libavahi-tqt.so.1.0.0

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
%_libdir/libavahi-tqt.so
%_pkgconfigdir/avahi-tqt.pc

##########

%prep
%setup -n %name
mkdir -p %buildroot%_prefix
mkdir -p %buildroot%_includedir
mkdir -p %buildroot%_libdir

pwd
echo "Проверяем, есть ли путь на данном месте (для patch)"
ls -l CMakeLists.txt
%patch0 -p1
%patch1 -p1

%build
#ls -l $RPM_BUILD_ROOT
RPM_BUILD_ROOT=/usr/src/RPM/BUILD

%cmake .. -DBIN_INSTALL_DIR=%_bindir \
  -DCMAKE_INSTALL_PREFIX=%_prefix \
  -DINCLUDE_INSTALL_DIR=%_includedir \
  -DLIB_INSTALL_DIR=%_libdir \
  -DCMAKE_VERBOSE_MAKEFILE=ON

%cmake_build

%install
#VБыло
#mkdir -p %buildroot%_libdir
#mkdir -p %buildroot%_includedir
#mkdir -p %buildroot%_pkgconfigdir
mkdir -p %{buildroot}%{_prefix}
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}
#VБыло
#%make_install DESTDIR="%buildroot%{_prefix}" -C build/x86_64-alt-linux
#%make_install DESTDIR="%buildroot" -C build

# Проверяем, что библиотеки попали в %_libdir
if [ ! -f "%buildroot%_libdir/libavahi-tqt.so.1" ]; then
    echo "Ошибка: библиотека не скопировалась в %_libdir" >&2
	else
    echo "Внимание!: библиотека скопировалась в %_libdir"
    exit 1
fi

export CMAKE_INSTALL_PREFIX=%{buildroot}/usr
%cmake -DCMAKE_INSTALL_PREFIX=%{buildroot}/usr
%__make install DESTDIR="%{?buildroot}" -C build
# Копируем библиотеки в правильное место
install -m 755 build/x86_64-alt-linux/avahi-tqt/libavahi-tqt.so %buildroot%_libdir/
install -m 755 build/x86_64-alt-linux/avahi-tqt/libavahi-tqt.so.1 %buildroot%_libdir/
install -m 755 build/x86_64-alt-linux/avahi-tqt/libavahi-tqt.so.1.0.0 %buildroot%_libdir/
# Копируем pkg-config файл
install -m 644 build/x86_64-alt-linux/avahi-tqt.pc %buildroot%_pkgconfigdir/

%changelog
* Sun Jan 26 2025 Petr Akhlamov <ahlamovpm@basealt.ru> 2:%version-%release
- Initial build for ALT Sisyphus
